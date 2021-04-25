from pwn import *

ip = "120.114.62.214"
port = 2403

r = remote(ip, port)

for i in range(1, 100 + 1):
    #r.sendlineafter('you say?\n', str(i))
    r.recvuntil("wave")
    r.recvuntil("?")
    r.sendline(str(i))


res = r.recv()
print(res)

r.interactive()