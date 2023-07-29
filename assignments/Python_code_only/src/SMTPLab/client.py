import socket
import base64

# Choose a mail server (e.g. Google mail server) and call it mailserver
smtp_server = 'smtp.163.com'
smtp_port = 25

# Create socket called client_socket and establish a TCP connection with mailserver
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((smtp_server, smtp_port))

# Receiver response from the mail server
recv = client_socket.recv(1024).decode()
print('connect: ' + recv)

# Send HELO command and print server response
hello_command = 'HELO Alice\r\n'
client_socket.send(hello_command.encode())
response = client_socket.recv(1024).decode()
print('HELO: ' + response)

# 发送认证命令（例如，使用用户名和密码进行身份验证）
client_socket.sendall(b'AUTH LOGIN\r\n')
response = client_socket.recv(1024)
print('AUTH LOGIN: ' + response.decode())

# 发送经过Base64编码的用户名
username = 'xhua188@163.com'
client_socket.sendall(base64.b64encode(username.encode()) + '\r\n'.encode())
response = client_socket.recv(1024)
print('Username: ' + response.decode())

# 发送经过Base64编码的密码
password = 'AFVGKOXAZZPFQMBB'
client_socket.sendall(base64.b64encode(password.encode()) + '\r\n'.encode())
response = client_socket.recv(1024)
print('Password: ' + response.decode())

# 设置发件人
from_address = 'xhua188@163.com'
client_socket.sendall(('MAIL FROM:<' + from_address + '>\r\n').encode())
response = client_socket.recv(1024)
print('Mail From: ' + response.decode())

# 设置收件人
to_address = 'xhua188@163.com'
client_socket.sendall(('RCPT TO:<' + to_address + '>\r\n').encode())
response = client_socket.recv(1024)
print('RCPT TO: ' + response.decode())

# 发送数据命令
client_socket.sendall(b'DATA\r\n')
response = client_socket.recv(1024).decode()
print(response)

# 构建邮件内容并发送
mail_content = f'''\
From: {from_address}
To: {to_address}
Subject: Example Email

This is the content of the email.
'''
client_socket.sendall(mail_content.encode())

# 发送结束符号
client_socket.sendall(b'\r\n.\r\n')
response = client_socket.recv(1024).decode()
print('Mail Content End: ' + response)

# 发送结束命令
client_socket.sendall(b'QUIT\r\n')
response = client_socket.recv(1024).decode()
print('QUIT: ' + response)

# 最后关闭套接字连接
client_socket.close()