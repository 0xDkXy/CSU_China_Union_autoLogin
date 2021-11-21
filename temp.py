import requests

a=requests.post(url='http://119.39.119.2/a70.htm',headers={
            'Host': '119.39.119.2',
            'Connection': 'keep-alive',
            'Content-Length': '164',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://119.39.119.2',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://119.39.119.2/a70.htm',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Server': 'DrcomServer1.0',
            # 'Accept-Ranges': 'bytes',
            # 'Connection': 'keep-alive',
            # 'Content-type': 'text/html; charset=gbk',
            # 'Cache-Control': 'no-cache',
            # 'Content-length': '4036',
        },data={
            'DDDDD': '028208191008@zndx',  # 填账户
            'upass': '47352089',  # 填密码
            'R1': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456'
        },timeout=5)
print(a.text)