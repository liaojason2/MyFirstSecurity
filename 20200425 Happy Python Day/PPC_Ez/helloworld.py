from pwn import *

ip = "120.114.62.214"
port = 2405

r = remote(ip, port)

res = r.recv()
print(res)

r.interactive()