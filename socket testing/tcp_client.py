import socket


def connection():
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while True:

        file_name = input('Enter the file you would like to send or q when you are done >>> ')
        if file_name.lower() == 'q':
            break
        try:
            open_file = open(file_name, 'r')
            data = open_file.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = open_file.read()
            open_file.close()

        except IOError:
            print('invalid file name')


if __name__ == '__main__':
    connection()
