from easy_socket.core import send_data_as_client, receive_data_as_server

def simulate_pipeline_modification(data: dict):
    data["modified"] = "ok"
    return data

# Server receive
data_received = receive_data_as_server("127.0.0.1", 49152)
print(f"Server receive message {data_received}")
# Server modify
data_modified = simulate_pipeline_modification(data_received)
# Server resend
send_data_as_client(data_modified, "127.0.0.1", 49153)
print(f"Server message sent {data_modified}")