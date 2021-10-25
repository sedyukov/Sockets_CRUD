import socket
import psycopg2

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    db_connect = psycopg2.connect(
        dbname="wxnwioxo",
        user="wxnwioxo",
        password="MkITccNXZXQMlPijxFXv_XLutiO9ovHV",
        host="hattie.db.elephantsql.com")
    cursor = db_connect.cursor()
    cursor.execute("SELECT * from userdata_users")

    record = str(cursor.fetchall())
    print(record)
    cursor.close()
    db_connect.close()

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
                break
        conn.send(str.encode(record))