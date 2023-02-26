import webbrowser
import random
import time

with open("words", 'r', encoding='utf-8') as f:
    data = f.read().splitlines()
n = 10
while n!= 0:
    w = data[random.randint(0, len(data))]
    webbrowser.open_new_tab("https://www.bing.com/search?q="+w)
    n -= 1
    time.sleep(2)