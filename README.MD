# 匿名DDoS工具

这个DDoS工具是Muneeb Khurram写的（我翻译的），并且这个脚本只能用于教育目的，请参阅许可证。现在添加了一个只依赖于Pyfiglet和GoLang的GUI.

## 安装

#### - 依赖于
a) pyttsx3 (文本到语音)只是为了让它变得更酷。不需要GUI。
```
pip3 install pyttsx3
```
b) pyfiglet (因为有必要更酷)
在Kali Linux中安装Figlet因为一些结果表示pyfiglet不显示任何东西。
```
sudo apt-get install figlet
```
```
pip3 install pyfiglet
```
c) colorama (迈向CLI Beauty的又一步)
```
pip3 install colorama
````
d) os (Python3中已经准备了)
```
pip3 install os
```
e) socket (为了升级释放)
```
pip3 install socket
```
f) wheel (使wheel有更多颜色) 
```
pip3 install wheel
```
e) GoLang (从 Golang.org/dl/ 下载你的系统) 

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

Kali有GoLang Pre-Installed.
打字检查;

```
go 
```
如果不遵循，上面显示的是Linux/Ubuntu


## 其它
用Install_Dependancies.py来安装除了GoLang以外的缩影东西(GoLang必须手动下载)
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
