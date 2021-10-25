import socket
import psycopg2


def getAll():
    cursor.execute("SELECT * from toys")
    record = str(cursor.fetchall())
    print(record)
    return record;


def addNew(name):
    cursor.execute("INSERT INTO toys(name) VALUES ('" + name + "');")


def updateUsage(name, usages):
    cursor.execute("UPDATE toys SET usage = " + usages + "WHERE \"name\" = '" + name + "';")


def deleteItem(name):
    cursor.execute("DELETE FROM toys WHERE \"name\" = '" + name + "';")

db_connect = psycopg2.connect(
        dbname="tivrqfmh",
        user="tivrqfmh",
        password="DuC4aZIVPJYpUOWC9toKqum6LfuYR416",
        host="ella.db.elephantsql.com")

cursor = db_connect.cursor()



HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
ans = "";
with conn:
    while True:
        data = conn.recv(1024)
        if data == b'get':
            ans = getAll()
        if data == b'add':
            addNew("new2")
            ans = "added new"
        if data == b'update':
            updateUsage("машинка", "3")
            ans = "updated usage"
        if data == b'delete':
            deleteItem("ведёрко")
            ans = "deleted ведёрко"
        if data == b'exit':
                break
        conn.send(str.encode(ans))

cursor.close()
db_connect.close()