import base64
import requests
url = 'https://raw.fastgit.org/Ezhhes/clancey/master/proxy.base64'
headers = {
    'user-agent':'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'
}
response = requests.post(url=url,headers=headers).content
de_base = base64.decodebytes(response)
link = de_base.decode('utf-8').split('\n')
v2ray = ''
for line in link:
    if 'vmess' in line:
        v2ray = v2ray + line + '\n'
final = base64.encodebytes(v2ray.encode('utf-8'))
f_res = final.decode('utf-8').replace('\n','')
with open('./vmess3.txt',mode='w',encoding='utf-8') as fp:
    fp.write(f_res)