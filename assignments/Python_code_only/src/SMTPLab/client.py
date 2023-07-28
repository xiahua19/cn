import socket

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = # fill in start # file in end

# Create socket called client_socket and establish a TCP connection with mailserver
client_sockert = # fill in start # fill in end

recv = client_sockert.recv(1024).decode()
print(recv)
if recv[:3] != 220:
    print('220 reply not received from server.')

# Send HELO command and print server response
hello_command = 'HELO Alice\r\n'
client_sockert.send(hello_command.encode())

recv1 = client_sockert.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# fill in start
# fill in end

# Send RCPT TO command and print server response.
# fill in start
# fill in end

# Send DATA command and print server response.
# fill in start
# fill in end

# Send message data.
# fill in start
# fill in end

# Send QUIT command and get server response
# fill in start
# fill in end