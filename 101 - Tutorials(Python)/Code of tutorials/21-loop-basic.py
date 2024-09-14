# while loop basic
# -----------------------------------------
i = 0
while i < 10:
    # print('Number is:', i)
    i += 1


# for loop basic
# syntax: for var_name in range(start, end, step)
# ---------------------------------------------------
for i in range(0, 10, 2):
    # print('Number is:', i)
    x = i


# negative step, time.sleep(second_late)-used to wait
# ---------------------------------------------------
import time
for i in range(10, 0, -2):
    # print(i)
    time.sleep(1.2)
# print('Times Lap end')


# nested loop- loop inside the another loop(for, while anything can be)
# --------------------------------------------------------------------
for i in range(3):
    for j in range(5):
        print('*', end = ' ')
    print()