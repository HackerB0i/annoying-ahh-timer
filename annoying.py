import time
from win10toast import ToastNotifier
toast = ToastNotifier()
# testing windows notifications

duration = int(input("how long do you want to wait (seconds): "))
timestart = time.time()

while time.time() - timestart < duration:
    print(time.time() - timestart)

while time.time() - timestart < duration * 5:
    toast.show_toast(
    "timer is done",
    f"your {duration} second timer is completed",
    duration = 0,
    threaded = True,
)