import time
tt=time.strftime('%H:%M:%S')
print(tt)
t=time.strftime("%H")
t=int(t)
# print(t)
if t>=0 and t<12:
    print("good morning sir!")
elif t>=12 and t<17:
    print("good afternoom sir!")
elif t>=17 and t<19:
    print("good evening sir!")
else:
    print("good night sir!")