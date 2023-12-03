import pyautogui
import time

a = "Salom"
b = 10
print("Boshlandi")
while b != 0:
    time.sleep(1)
    print(b, "s qoldi")
    b -= 1
print("Start")
i = 0
# while True:
for i in range(1, 10):
    pyautogui.typewrite(a + "\n")
    print(i, "jo'natildi")
    i += 1
