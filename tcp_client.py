#! /usr/bin/env python3

import socket

def main():
    target_host = input("host: ").strip()
    target_port = int(input("port: ").strip())
    server_address = (target_host, target_port)

    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(server_address)
    client.send(b"GET / HTTP/1.1\r\n\r\n")
    response = client.recv(4096)
    print(response.decode("utf-8"))
    client.close()
    return

if __name__ == "__main__":
    main()

