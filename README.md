# CSU_China_Union_autoLogin
中南大学联通掉线自动重连脚本

运行命令
```bash
python3 -u autoLogin.py
挂在后台运行命令
python3 -u ./autoLogin.py > ./log.txt 2>./log.txt &
```


![](https://gitee.com/NoobInCsu_0xDkXy/photos/raw/master/img/20210914214419.png)
此处填写账户

## 获取账户和密码

- 首先在浏览器访问 [登陆网址](http://119.39.119.2/a70.htm)

- 按F12，弹出DevTool

- 选择网络 并点击清除
![](https://gitee.com/NoobInCsu_0xDkXy/photos/raw/master/img/20210914214815.png)

- 登陆你的账号，并在DevTool中选中**a70.htm**
![](https://gitee.com/NoobInCsu_0xDkXy/photos/raw/master/img/20210914215043.png)
其中DDDDD是账号
upass是密码

把他粘贴到autoLogin.py中，脚本就能正常运行了