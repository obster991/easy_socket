import socket
import json
import time

############################### CLIENT ###############################
# Client sends as first message the lenght of the message it will send after
def send_data_as_client(data: dict,
                        host: str,
                        port: int,
                        max_buffer_size: int = 1024*64,
                        encoding: str = "utf-8",
                        sock: socket.socket = None,
                        timeout = 100):
    
    if port not in range(49152,65535):
        raise Exception("Port number not available. Must be in range [49152,65535]")
    
    # Check if is avilable a reusable socket object, 
    # otherwise instanciate new socket object and bind for the connection
    if sock == None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    start_timeout = time.time()
    counter_timeout = 0
    while counter_timeout < timeout:
        try:
            sock.connect((host, port))
        except:
            time.sleep(1)
            counter_timeout = time.time() - start_timeout
            continue
        break
    
    # Send lenght as first message
    total_len = str(len(json.dumps(data))).encode(encoding)
    sock.send(total_len)
    
    # Receive ack for lenght
    ack = sock.recv(max_buffer_size)
    ack = ack.decode(encoding)
    if ack == "ok":
        pass
    else:
        raise Exception("Ack for leght is incorrect")

    # Send all data
    data = json.dumps(data)
    data = data.encode(encoding)
    sock.send(data)

    if sock == None:
        sock.close()


############################### SERVER ###############################
# Server must receive the lenght of the message it will receive from Client as first independent message
def receive_data_as_server(host: str,
                           port: int,
                           max_buffer_size: int = 1024*64,
                           encoding: str = "utf-8",
                           connection: socket.socket = None) -> dict:
    
    if port not in range(49152,65535):
        raise Exception("Port number not available. Must be in range [49152,65535]")
    
    # Initialize socket object and bind for the connection
    if connection == None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen()
        connection, address = sock.accept()

    # Receive lenght as first message
    total_len = connection.recv(max_buffer_size)
    total_len = int(total_len.decode(encoding))
    
    # Send ack for lenght (otherwise message is put in one unique buffer)
    ack = "ok".encode(encoding)
    connection.send(ack)

    # Receive all data in segments as bytes
    buffer_data = b""
    acquired_len = 0
    while acquired_len < total_len:
        segment_data = connection.recv(max_buffer_size)
        buffer_data += segment_data
        acquired_len += len(segment_data.decode(encoding))
    
    if connection == None:
        connection.close()

    # Parse to json dict
    data = buffer_data.decode(encoding)
    data = json.loads(data)

    return data