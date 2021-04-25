import base64
rawdata = "BreakallCTF{happyhackinghighhaaha}".encode()
ans = base64.b64encode(rawdata)
print(ans)
'''
print(len(rawdata))
ans = ""
for i in range(0, len(rawdata)):
    ans += base64.encodestring(rawdata)
print(ans)
'''
