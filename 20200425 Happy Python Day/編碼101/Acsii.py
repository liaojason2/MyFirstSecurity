rawdata = "66 114 101 97 107 65 76 76 67 84 70 123 65 109 118 48 117 68 121 101 114 118 80 116 109 86 114 57 83 83 83 75 125"
data = rawdata.split(" ")
ans = ""
for i in range(0,len(data)):
    ans += chr(int(data[i]))
print(ans)