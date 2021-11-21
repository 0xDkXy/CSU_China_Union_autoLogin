import requests
import time
import socket
import random
import get_url
import traceback
import logging
import gc
import os


# urlconn = requests.models.Response


header_close = {'Connection': 'keep-alive'}


class autoLogin():
    __url = 'http://www.baidu.com'
    __status = -1
    __loginUrl = 'http://119.39.119.2'
    __initFlag = False

    def getTime3(self):
        return time.localtime(time.time())[3]

    def isInit(self) -> bool:
        return self.__initFlag
    # def printNowTime(self):
    #     print(time.strftime("%Y-%m-%d %H:%M:%S :", time.localtime()),end=' ')

    def __del__(self):
        del self.__session
        logging.warning("Object autoLogin deleted!")

    def __init__(self):
        self.__status = -1
        self.__initFlag = False
        self.__session = requests.session()

    def check(self)->bool:
        # self.__urlptr %= self.__urlsize
        # test =
        returnVal = False
        try:
            Connection = self.__session.get(
                url=self.__url, timeout=5, headers=header_close)
            if Connection.status_code == 200 and Connection.url != 'http://119.39.119.2':
                del Connection
                returnVal = True
            else:
                del Connection
                # returnVal = False
        except:
            logging.warning(traceback.format_exc())
        finally:
            gc.collect()
            return returnVal

    def login(self):
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " Try Reconnect!")
        logging.info('Try Login!')
        post_test = 'http://119.39.119.2/a70.htm'
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
        post_data = {
            'DDDDD': '028208191008@zndx',  # 填账户
            'upass': '47352089',  # 填密码
            'R1': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456'
        }
        if post_data['DDDDD'] == '':
            logging.error("Wrong UserName!")
            exit()
        if post_data['upass'] == '':
            logging.error('Wrong Password!')
            exit()
        while True:
            try:
                # loginGet = requests.get(url=post_test, timeout=20)
                loginPost = self.__session.post(
                url=post_test, headers=post_header, data=post_data,timeout=10)
                checkFlag = loginPost.headers["Content-length"]
                if loginPost.status_code == 200 and checkFlag == '4036':
                    logging.info('Login Succeed!')
                else:
                    logging.info('Login Failed!')
                # del loginGet
                del loginPost
                break
            except:
                logging.warning(traceback.format_exc())
            time.sleep(1)

    def run(self):
        # self.printNowTime()
        logging.info('Start Running!')
        time_st = time.time()
        while True:
            if self.check() == True:
                logging.info('Connected!')
                sleepTime = random.randint(10, 60)
                logging.info(f'Sleep Time : {sleepTime}')
                time.sleep(sleepTime)
            else:
                try:
                    self.login()
                except Exception:
                    # logging.info("Exception in start!")
                    logging.warning(traceback.format_exc())
                finally:
                    time.sleep(random.randint(0, 10))
            gc.collect()
            if time.time() - time_st >= 3600.0:
                logging.info("Exit Run!")
                break


def main():
    LOG_FORMAT = "[%(asctime)s] - [%(levelname)s] - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    while True:
        try:
            autologin = autoLogin()
            autologin.run()
            del autologin
        except Exception:
            logging.warning(traceback.format_exc())
        finally:
            gc.collect()


if __name__ == "__main__":
    main()