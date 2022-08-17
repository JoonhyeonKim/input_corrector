from pwn import *

host = input("Enter the host address: ")
user = input("Enter the user name: ")
port = input("Enter the target port: ")
password = input("Enter the password: ")

def inputs(host,user,port,password):
    host = list(host)
    user = list(user)
    port = list(port)
    password = list(password)
    host.remove('\n')
    user.remove('\n')
    port.remove('\n')
    password.remove('\n')
    host=''.join(host)
    user=''.join(user)
    port=''.join(port)
    password=''.join(password)
    return host, user, port, password

a = inputs(host, user, port, password)    
s = ssh(user=a[1], host=a[0], port=int(a[2]) ,password=a[3])

s.process('/bin/sh', env={'PS1':''})
s.process(['/bin/echo', b'\xff']).recvall()

