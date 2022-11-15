import time
h=0
min=0
s=0

for h in range(24):
    for m in range(60):
        for s in range (60):
            print (f"{h}:{m}:{s}")
            for i in range(7):
                print()
            time.sleep(1)