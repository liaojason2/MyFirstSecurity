from pwn import *

ip = "140.110.112.22"
port = 2400

r = remote(ip, port)
r.recvuntil("Now You Turn")
r.recvuntil(" : ")
res = r.recvline()[:-1]
res = list(map(int, res.split()))
res.sort()
#r.recvline("answer :")
r.sendline(str(res[-3]))
#print(res)

r.interactive()