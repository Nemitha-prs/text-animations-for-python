import os
import time

text = "I'm Nemitha Prabashwara.\nI'm Interested in software developing"
x = len(text)
y=int(0)
n = ""

while x>y:
    z = text[y]
    os.system('cls') #you can remove or add cls funtion to change blinking speed
    os.system('cls')
    n = n + z
    print(n)
    time.sleep(0.1)
    y = y+1
    

