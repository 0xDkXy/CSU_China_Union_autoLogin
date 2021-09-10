import requests
import re


def get_csu_url():
    a=requests.get(url='http://www.csu.edu.cn/xyxk1/ejxy.htm')
    obj=re.findall(r'http://.*?\.csu\.edu\.cn',a.text)
    obj=obj[:-2]
    obj.append('http://www.csu.edu.cn')
    return obj


if __name__=='__main__':
    get_csu_url()