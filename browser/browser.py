import webbrowser
import random
import time
import os

try:
    with open("/usr/share/dict/words", 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        ostype="UNIX"

except:
    data_win = ["nor", "norm", "normal", "normalcy", "normalcy's", "normality", "normality's", "normalization", "normalization's", "normalize", "normalized", "normalizes", "normalizing", "normally", "normal's", "normative", "norm's", "norms", "north", "northbound", "northeast", "northeaster", "northeasterly", "northeastern", "northeaster's", "northeasters", "northeast's", "northeastward", "northerlies", "northerly", "northerly's", "northern", "northerner", "northerner's", "northerners", "northernmost", "north's", "northward", "northwards", "northwest", "northwesterly", "northwestern", "northwest's", "northwestward", "no's", "nos", "nose", "nosebleed", "nosebleed's", "nosebleeds", "nosed", "nosedive", "nosedived", "nosedive's", "nosedives", "nosediving", "nosedove", "nosegay", "nosegay's", "nosegays", "nose's", "noses", "nosey", "nosh", "noshed", "noshes", "noshing", "nosh's", "nosier", "nosiest", "nosiness", "nosiness's", "nosing", "nostalgia", "nostalgia's", "nostalgic", "nostalgically", "nostril", "nostril's", "nostrils", "nostrum", "nostrum's", "nostrums", "nosy", "not", "notable", "notable's", "notables", "notably", "notaries"]
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
            webbrowser.open_new_tab("https://www.bing.com/search?q="+w)
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
    print(" Stopped")