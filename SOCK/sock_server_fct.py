#---------------------------------------------
from SOCK import sock_client
from param import param_hu

import socket


def thread_socket_l1_server():
    port = param_hu.state_hu["self"]["sock_server_l1_port"]
    param_hu.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_hu.sock_server_l1.bind(("", port))
    param_hu.sock_server_l1.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            data, (address, port) = param_hu.sock_server_l1.recvfrom(4096)
            param_hu.state_hu["pywardium"]["sock_l1_connected"] = True
            process_l1_data(data)
        except:
            param_hu.state_hu["pywardium"]["sock_l1_connected"] = False

    param_hu.sock_server_l1.close()

def thread_socket_l2_server():
    port = param_hu.state_hu["self"]["sock_server_l2_port"]
    param_hu.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server_l2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_hu.sock_server_l2.bind(("", port))
    param_hu.sock_server_l2.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            data, (address, port) = param_hu.sock_server_l2.recvfrom(4096)
            param_hu.state_hu["pywardium"]["sock_l2_connected"] = True
            process_l2_data(data)
        except:
            param_hu.state_hu["pywardium"]["sock_l2_connected"] = False

    param_hu.sock_server_l2.close()

def process_l1_data(data):
    if(param_hu.state_hu["self"]["sock_server_l1_source"] == "lidar_1"):
        sock_client.send_packet_l1(data)
    elif(param_hu.state_hu["self"]["sock_server_l1_source"] == "lidar_2"):
        sock_client.send_packet_l2(data)

def process_l2_data(data):
    if(param_hu.state_hu["self"]["sock_server_l2_source"] == "lidar_1"):
        sock_client.send_packet_l1(data)
    elif(param_hu.state_hu["self"]["sock_server_l2_source"] == "lidar_2"):
        sock_client.send_packet_l2(data)
