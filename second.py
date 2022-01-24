import sys


class except1(Exception):
    pass


try:
    s = 0
    c = 0
    ly = len(sys.argv)
    if ly == 1:
        raise except1
    for i in range(1, ly):
        if sys.argv[i] // 1 == sys.argv[i]:
            c += 1
            if c % 2:
                s += int(sys.argv[i])
            else:
                s -= int(sys.argv[i])
    print(s)
except except1:
    print("NO PARAMS")
except Exception as excepting:
    print(type(excepting).__name__)