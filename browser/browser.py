import webbrowser
import random
import time

a=input("is this unix(1) or windows(2)?: ")
if (a=="1"):
    with open("browser/words", 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    n = 10
    while n!= 0:
        w = data[random.randint(0, len(data))]
        webbrowser.open_new_tab("https://www.bing.com/search?q="+w)
        n -= 1
        time.sleep(2)
elif (a=="2"):
    with open("browser\words", 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    n = 10
    while n!= 0:
        w = data[random.randint(0, len(data))]
        webbrowser.get("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe").open_new_tab("https://www.bing.com/search?q="+w)
        n -= 1
        time.sleep(2)
else:
    print("we hate mac")