import random


def comands():
    fst_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
    scd_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
    win_tour = [(fst_command[i] if fst_command[i] > scd_command[i] else scd_command[i]) for i in range(20)]
    print(fst_command)
    print(scd_command)
    print(win_tour)


if __name__ == '__main__':
    comands()
