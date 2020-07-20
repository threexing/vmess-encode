import base64
from urllib.request import urlopen

resp = urlopen("https://raw.githubusercontent.com/IEGMickey/V2ray/master/node.txt")
line = '初始化'
file = ''
while line:
    line = resp.readline().decode('utf-8')
    if 'vmess' in line:
        file += line
final = base64.encodebytes(file.encode('utf-8'))
f_res = final.decode('utf-8').replace('\n','')
with open('vmess2.txt',mode='w') as f:
    f.write(f_res)
    

if __name__ == "__main__":
    main()

