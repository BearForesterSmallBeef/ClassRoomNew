x1, y1, w1, h1 = [int(i) for i in input().split()]
x2, y2, w2, h2 = [int(i) for i in input().split()]
s = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2
flag = False
x11 = x1 + w1
x22 = x2 + w2
y11 = y1 + h1
y22 = y2 + h2
if x1 <= x2 and x11 >= x2 or x1 <= x22 and x11 >= x22 or x2 <= x1 and x22 >= x1 or x2 <= x11 and x22 >= x11:
    if y1 <= y2 and y11 >= y2 or y1 <= y22 and y11 >= y22 or y2 <= y1 and y22 >= y1 or y2 <= y11 and y22 >= y11:
        flag = True
if flag:
    print("YES")
else:
    print("NO")