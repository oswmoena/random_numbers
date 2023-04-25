import random
import sys

selected_nums = []
times = 1
count = 0


def verify_times():
    if len(sys.argv) == 1:
        return 1
    else:
        return sys.argv[1]


def verify_num(num):
    if num in selected_nums:
        return True
    else:
        return False


def add_num():
    new_num = random.randrange(1, 42)
    if verify_num(new_num):
        return False
    else:
        selected_nums.append(new_num)


def rand_num():
    print("Tiro N°:", count + 1)
    while len(selected_nums) < 6:
        add_num()
    selected_nums.sort()


times = int(verify_times())
while times > count:
    rand_num()
    count += 1
print("Resultado:", selected_nums)
