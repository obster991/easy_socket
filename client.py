from easy_socket.core import send_data_as_client, receive_data_as_server

data_to_send = {"test_key":"test_value"}

# Client send
send_data_as_client(data_to_send, "127.0.0.1", 49152, max_buffer_size=4)
print(f"Client message sent {data_to_send}")

# Client receive
data_final = receive_data_as_server("127.0.0.1", 49153, max_buffer_size=4)
print(f"Client receive: {data_final}")