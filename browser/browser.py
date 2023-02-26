import webbrowser
import random
import time

data = ["nor", "norm", "normal", "normalcy", "normalcy's", "normality", "normality's", "normalization", "normalization's", "normalize", "normalized", "normalizes", "normalizing", "normally", "normal's", "normative", "norm's", "norms", "north", "northbound", "northeast", "northeaster", "northeasterly", "northeastern", "northeaster's", "northeasters", "northeast's", "northeastward", "northerlies", "northerly", "northerly's", "northern", "northerner", "northerner's", "northerners", "northernmost", "north's", "northward", "northwards", "northwest", "northwesterly", "northwestern", "northwest's", "northwestward", "no's", "nos", "nose", "nosebleed", "nosebleed's", "nosebleeds", "nosed", "nosedive", "nosedived", "nosedive's", "nosedives", "nosediving", "nosedove", "nosegay", "nosegay's", "nosegays", "nose's", "noses", "nosey", "nosh", "noshed", "noshes", "noshing", "nosh's", "nosier", "nosiest", "nosiness", "nosiness's", "nosing", "nostalgia", "nostalgia's", "nostalgic", "nostalgically", "nostril", "nostril's", "nostrils", "nostrum", "nostrum's", "nostrums", "nosy", "not", "notable", "notable's", "notables", "notably", "notaries"]

a=input("is this unix(1) or windows(2)?: ")
if (a=="1"):
    n = 10
    while n!= 0:
        w = data[random.randint(0, len(data))]
        webbrowser.open_new_tab("https://www.bing.com/search?q="+w)
        n -= 1
        time.sleep(2)
elif (a=="2"):
    n = 10
    while n!= 0:
        w = data[random.randint(0, len(data))]
        webbrowser.register('edge', None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
        webbrowser.get('edge').open_new_tab("https://www.bing.com/search?q="+w)
        n -= 1
        time.sleep(2)
else:
    print("we hate mac")