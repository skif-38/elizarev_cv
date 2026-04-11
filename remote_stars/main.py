import socket
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def receive_all(connection, total_bytes):
    buffer = bytearray()
    while len(buffer) < total_bytes:
        chunk = connection.recv(total_bytes - len(buffer))
        if not chunk:
            return None
        buffer.extend(chunk)
    return buffer

def find_brightest_pixel(img: np.ndarray, labels: np.ndarray, target_label: int):
    coords = np.unravel_index(np.argmax(img * (labels == target_label)), img.shape)
    return coords

def euclidean_distance(point_a: list[int, int], point_b: list[int, int]) -> float:
    return ((point_a[1] - point_b[1])**2 + (point_a[0] - point_b[0])**2)**0.5

def process_image(img: np.ndarray) -> float:
    labels = label(img > 0)
    first_center = find_brightest_pixel(img, labels, 1)
    second_center = find_brightest_pixel(img, labels, 2)
    return euclidean_distance(first_center, second_center)

HOST = "84.237.21.36"
PORT = 5152

def run_client() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((HOST, PORT))
        client_sock.send(b"124ras1")
        print(client_sock.recv(10))

        status = b"nope"
        while status != b"yep":
            client_sock.send(b"get")
            raw_data = receive_all(client_sock, 40002)

            img_array = np.frombuffer(raw_data[2:40002], dtype="uint8").reshape(raw_data[0], raw_data[1])
            calculated = round(process_image(img_array), 1)

            print("my ans", calculated)
            client_sock.send(str(calculated).encode())
            print(client_sock.recv(10))
            client_sock.send(b"beat")
            status = client_sock.recv(10)

if __name__ == "__main__":
    run_client()