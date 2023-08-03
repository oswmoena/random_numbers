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
def verify_type():
    if len(sys.argv) == 2:
        return 1
    else:
        return 2


def verify_num(num):
    if num in selected_nums:
        return True
    else:
        return False


def add_num():
    max_rang = 42 if game_type == 1 else 26
    new_num = random.randrange(1, max_rang)
    if verify_num(new_num):
        return False
    else:
        selected_nums.append(new_num)
def rand_num():
    max_num = 6 if game_type == 1 else 14
    print("Tiro N°", count +1)
    while len(selected_nums) < max_num:
        add_num()
    selected_nums.sort()

game_type = int(verify_type())
times = int(verify_times())
while times > count:
    rand_num()
    count += 1
print("Resultado:", selected_nums)
