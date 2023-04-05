import webbrowser
import random
import time
import os

try:
    with open("/usr/share/dict/words", 'r', encoding='utf-8') as f:
        data_win = f.read().splitlines()
        ostype="UNIX"

except:
    with open(("words"), 'r', encoding='utf-8')as f:
        data = d.read().splitlines()
        ostype="WIN"

try :
    a=ostype
    n = int(input("no. of tabs you want to open: "))
    seconds=int(input("lag between each tab: "))
    while n!= 0:
        if (a=="UNIX"):
            with open("/usr/share/dict/words", 'r', encoding='utf-8') as f:
                data = f.read().splitlines()
            w = data[random.randint(0, len(data))]
            x = data[random.randint(0, len(data))]
            webbrowser.register('edge', None,webbrowser.BackgroundBrowser("/usr/bin/microsoft-edge-stable"))
            webbrowser.get('edge').open_new_tab("https://www.bing.com/search?q="+w+"+"+x)
            n -= 1
            time.sleep(seconds)
            if n==0 :
                os.system("pkill msedge")
                
        elif (a=="WIN"):
            w = data_win[random.randint(0, len(data_win)-1)]
            webbrowser.register('edge', None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
            webbrowser.get('edge').open_new_tab("https://www.bing.com/search?q="+w)
            n -= 1
            time.sleep(seconds)
            if n==0 :
                os.system("taskkill /im msedge.exe")
        else:
            print("we hate mac")
            break
except KeyboardInterrupt:
    print("unt, Stopped")