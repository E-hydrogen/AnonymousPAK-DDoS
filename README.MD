# 匿名DDoS工具

这个DDoS工具是Muneeb Khurram写的（宇涵翻译的），并且这个脚本只能用于教育目的，请参阅许可证。现在添加了一个只依赖于Pyfiglet和GoLang的GUI.

## 安装

#### - 依赖于
a) pyttsx3 (Text-to-Speech) Just to make it cooler. Not Neccesary for GUI.
```
pip3 install pyttsx3
```
b) pyfiglet (Cause its Neccesary to be Cooler)
Install Figlet in Kali Linux as some results show that pyfiglet doesnt show anything.
```
sudo apt-get install figlet
```
```
pip3 install pyfiglet
```
c) colorama (Another Step towards CLI Beauty)
```
pip3 install colorama
````
d) os (Already in Python3)
```
pip3 install os
```
e) socket (For an Upcomming Release)
```
pip3 install socket
```
f) wheel (To make wheel of colorama) 
```
pip3 install wheel
```
e) GoLang (Download for your OS form Golang.org/dl/) 

### MacOS

> https://medium.com/golang-learn/quick-go-setup-guide-on-mac-os-x-956b327222b8

### Windows

> https://www.geeksforgeeks.org/how-to-install-go-on-windows/

### Linux

> https://tecadmin.net/install-go-on-ubuntu/
```
sudo apt-get install golang
```
or
```
sudo apt-get install golang-go
```

### Kali Linux

Kali has GoLang Pre-Installed.
Check by typing;

```
go 
```
If not Follow, the above shown for Linux/Ubuntu


## 其它
Use Install_Dependancies.py to Install all of these except GoLang (it has to be downloaded Manually)
````
python3 Install_Dependancies.py
````
## 用法
````
python3 Python-Script.py
````
## GUI 要求

> 如上所述，安装Pyfiglet和GoLang，这些你已经准备好了。如果您还没安装，请使用此方法安装。此DDoS工具很容易使用，建议初学者使用Windows系统。如果你在Linux Distro上运行它并且收到了“tkinter not found”，请安装tkinter. 

```
python3 DDoS_GUI.py
```
## 测试 OS/ENV

- Linux Stable Release 2020

- Kali Linux 2019.3

- Google Colab

- Windows 10

- MacOS X 10.10.5 Onwards (OS X Yosmite)

> 这个应该可以在所有的环境下运行，即使是在最旧的系统也要保证上述依赖性完成。

## 图像

展示一些接口和其互动环境。

![AnonymousDDoS_GUI](https://munublogs.files.wordpress.com/2020/05/screen-shot-2020-05-13-at-8.11.04-pm.png)

![Terminal_Photos](https://munublogs.files.wordpress.com/2020/05/screen-shot-2020-05-13-at-8.09.41-pm.png)

![Terminal_Photos2](https://munublogs.files.wordpress.com/2020/05/screen-shot-2020-05-13-at-8.10.30-pm.png)

## 许可证
版权归Muneeb Khurram所有, HULK-DoS工具也归其作者所有。
这里所有的脚本都是开玩笑的，欢迎来到DDoS天堂。
使用前请参照许可证
