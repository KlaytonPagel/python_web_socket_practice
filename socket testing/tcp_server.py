import socket


def connection():
    host = '127.0.0.1'
    port = 8080
    client_amount = int(input('Enter the number of client connections >>> '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(client_amount)

    connections = []
    print('Connecting to clients')
    for client in range(client_amount):
        conn = sock.accept()
        connections.append(conn)
        print('connected to client {}'.format(client + 1))

    file_number = 0
    client_number = 0
    for conn in connections:
        client_number += 1
        data = conn[0].recv(1024).decode()

        if not data:
            continue

        file_name = 'file_{}.txt'.format(str(file_number))
        file_number += 1
        open_file = open(file_name, 'w')
        while data:
            if not data:
                break
            else:
                open_file.write(data)
                data = conn[0].recv(1024).decode()

        print('Received file {}'.format(file_name))
        open_file.close()

    for conn in connections:
        conn[0].close()


if __name__ == '__main__':
    connection()
