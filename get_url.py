import requests
import re
import logging
import random
import traceback
import gc

header_close = {"Connection":"close"}

def get_csu_url():
    obj=[]
    try:
        a=requests.get(url='http://www.csu.edu.cn/xyxk1/ejxy.htm',timeout=10)
        a.close()
    except Exception:
        # logging.error(traceback.format_exc)
        logging.exception("Exception in get_csu_url!")
        logging.debug(traceback.format_exc())
        return obj
    # a.close()
    obj.append('http://www.csu.edu.cn')
    obj=re.findall(r'http://.*?\.csu\.edu\.cn',a.text)
    obj=obj[:-2]
    random.shuffle(obj)
    res=obj[:10]
    del a
    del obj
    gc.collect()
    return res


if __name__=='__main__':
    urllist = get_csu_url()
    LOG_FORMAT = "[%(asctime)s] - [%(levelname)s] - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    truelist = []
    for url in urllist:
        if url == 'http://netclass.csu.edu.cn' or url == 'http://career.csu.edu.cn' or url == 'http://sce.csu.edu.cn' or url == 'http://gra.its.csu.edu.cn':
            continue
        test = requests.get(url)
        if test.status_code == 200:
            truelist.append(url)
            logging.info(url)
    print(truelist)