import socket
HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        q = input()
        s.sendall(str.encode(q))
        data = s.recv(1024)
        print('Received', data.decode())
        if q == "exit":
            break


