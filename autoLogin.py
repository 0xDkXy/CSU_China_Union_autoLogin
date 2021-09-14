import requests
import time
import socket
import random
import get_url
import traceback
import logging
import gc


urlconn = requests.models.Response


header_close = {'Connection': "close"}


class auto_login():
    __connect = requests.Session()
    __check_connect_url = 'http://www.baidu.com'
    __url_list = []
    __status = int
    __urlptr = 0
    __urlsize = int
    __loginUrl = 'http://119.39.119.2'
    __url_list_flag = 0

    def getTime3(self):
        return time.localtime(time.time())[3]

    # def printNowTime(self):
    #     print(time.strftime("%Y-%m-%d %H:%M:%S :", time.localtime()),end=' ')

    def __init__(self):
        flag = 0
        while flag == 0:
            try:
                urlconn = requests.get(
                    url=self.__check_connect_url, timeout=10, headers=header_close)
                # if urlconn.url == "http://119.39.119.2"
                self.__status = urlconn.status_code
                flag = 1
            except Exception as exc:
                # urlconn.close()
                logging.warn(self.__check_connect_url + ' timeout')
                self.__status = 0
                break
            finally:
                del urlconn
                gc.collect()
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
        # test =
        temp_flag = 0
        for url in self.__url_list:
            try:
                conn = requests.get(url=url, timeout=5,headers = header_close)
                if conn.status_code == 200 and conn.url != 'http://119.39.119.2':
                    temp_flag = 1
                    break
                del conn
                gc.collect()
                # conn.close()
            except socket.timeout:
                logging.info("Timeout! in line 67 conn = requests.get [{}]".format(url))
                logging.debug(traceback.format_exc())
                self.__url_list.remove(url)
            except TimeoutError:
                logging.info("TimeoutError! in line 67 conn = requests.get [{}]".format(url))
                logging.debug(traceback.format_exc())
                # conn.close()
            except requests.ConnectTimeout:
                logging.info("ConnectTimeout! in line 67 conn = requests.get [{}]".format(url))
                logging.debug(traceback.format_exc())
                self.__url_list.remove(url)
            except requests.ReadTimeout:
                logging.info("ReadTimeout! in line 67 conn = requests.get [{}]".format(url))
                logging.debug(traceback.format_exc())
                self.__url_list.remove(url)
            except Exception:
                logging.info("Exception in check!")
                logging.debug(traceback.format_exc())
        if temp_flag == 1:
            return True
        else:
            return False

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
        login = requests.Session()
        login_get = login.get(url=post_test, timeout=20)
        # print("get_status_code:{}".format(login_get.status_code))

        post_data = {
            'DDDDD': '',  # 填账户
            'upass': '',  # 填密码
            'R1': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456'
        }
        if post_data['DDDDD'] == '':
            logging.error("账号错误!")
            return
        if post_data['upass'] == '':
            logging.error('密码错误!')
            return

        login_post = login.post(
            url=post_test, headers=post_header, data=post_data)
        checkFlag = login_post.headers["Content-length"]
        # print("post_status_code:{}".format(login_post.status_code))
        if login_post.status_code == 200 and checkFlag == '4036':
            # print("Connected!")
            logging.info('Succeed!')
            self.__url_list_flag = len(self.__url_list)
            if self.__url_list_flag == 0:
                self.__url_list = get_url.get_csu_url()
                self.__url_list_flag = len(self.__url_list)
        # print("status_code:{}".format(login.status_code));
        else:
            logging.info('failed!')
        login_post.close()
        login_get.close()
        login.close()
        del login_get
        del login_post
        del login
        gc.collect()

    def __update_list(self):
        self.__url_list = get_url.get_csu_url()

    def start(self):
        # self.printNowTime()
        logging.info('Start!')
        time_st = time.time()
        while True:
            if self.check() == True:
                logging.info('Connected!')
                if time.time() - time_st >= 3600.0:
                    self.__update_list()
                    logging.info("update url_list!")
                time.sleep(10)
            else:
                try:
                    self.login()
                except Exception:
                    logging.info("Exception in start!")
                    logging.debug(traceback.format_exc())
            gc.collect()


def main():
    LOG_FORMAT = "[%(asctime)s] - [%(levelname)s] - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    autologin = auto_login()
    autologin.start()


if __name__ == "__main__":
    main()


# Content-length: 3494
