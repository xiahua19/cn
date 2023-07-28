import socket

class MyClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def start(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((self.server_ip, self.server_port))

            while True:
                message = input("请输入要发送的消息：")
                client_socket.send(message.encode('utf-8'))

                response = client_socket.recv(1024).decode('utf-8')
                print("服务器回复:", response)

                if message == "exit":
                    break

        except Exception as e:
            print("发生异常:", e)

        finally:
            client_socket.close()

if __name__ == '__main__':
    server_ip = '127.0.0.1'  # 服务器IP地址
    server_port = 12345      # 服务器端口号

    client = MyClient(server_ip, server_port)
    client.start()
