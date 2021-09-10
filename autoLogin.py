import requests
import time
import socket
import random
import get_url
import traceback
import logging


class auto_login():
    __connect = requests.Session()
    __check_connect_url = 'https://cn.bing.com'
    __url_list = []
    __status = int
    __urlptr = 0
    __urlsize = int
    __loginUrl = 'http://119.39.119.2'
    __url_list_flag = 1

    def getTime3(self):
        return time.localtime(time.time())[3]

    # def printNowTime(self):
    #     print(time.strftime("%Y-%m-%d %H:%M:%S :", time.localtime()),end=' ')

    def __init__(self):
        flag = 0
        while flag == 0:
            try:
                temp = requests.get(self.__check_connect_url)
                self.__status = temp.status_code
                flag = 1
            except Exception as exc:
                continue
            finally:
                temp.close()
                # raise exc
        if self.__status == 200:
            self.__url_list = get_url.get_csu_url()
            self.__urlsize = len(self.__url_list)
            logging.info(str(self.__urlsize))
            logging.info(str(self.__url_list))

    def is_connected(self):
        if self.__status == 200:
            return True
        else:
            return False

    def check(self):
        # self.__urlptr %= self.__urlsize
        try:
            flag = 0
            while flag != 200:
                if len(self.__url_list) == 0:
                    test = requests.get('https://www.baidu.com')
                    self.__url_list_flag = 0;
                else: 
                    test = requests.get(random.choice(self.__url_list))
                flag = test.status_code
        except Exception:
            traceback.print_exc()
        else:
        # finally:
        #     self.__urlptr += 1
        #     self.__urlptr %= __urlsize
            if test.url != 'http://119.39.119.2':
                # print("connected!")
                return True
            else:
                if test.status_code == 200:
                    logging.info("Disconnected!")
                # print("disconnected!")
                else:
                    logging.error(test.url+' '+str(test.status_code))
                return False
        finally:
            test.close()

    def login(self):
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " Try Reconnect!")
        logging.info('Try Login!')
        post_test = 'http://119.39.119.2'
        # print("Try login")
        post_header = {
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
        }
        user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
                        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                        ]
        post_header['User-Agent'] = random.choice(user_agent_list)
        login = requests.Session()
        # login_get = login.get(url=post_test,headers=post_header)
        # print("get_status_code:{}".format(login_get.status_code))

        post_data = {
            'DDDDD': '028208191008@zndx',
            'upass': '47352089',
            'R1': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456'
        }

        login_post = login.post(url=post_test, headers=post_header, data=post_data)
        # print("post_status_code:{}".format(login_post.status_code))
        if login_post.status_code == 200:
            # print("Connected!")
            logging.info('Succeed!')
            if self.__url_list_flag == 0:
                self.__url_list = get_url.get_csu_url()
                self.__url_list_flag = 1
        # print("status_code:{}".format(login.status_code));
        else:
            logging.info('failed!')
        login.close()

    def start(self):
        # self.printNowTime()
        logging.info('Start!')
        while True:
            if self.check() == True:
                logging.info('Connected!')
                time.sleep(5)
            else:
                self.login()


def main():
    LOG_FORMAT = "[%(asctime)s] - [%(levelname)s] - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    autologin = auto_login()
    autologin.start()


if __name__ == "__main__":
    main()
