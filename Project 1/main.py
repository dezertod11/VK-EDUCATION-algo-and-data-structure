n = int(input())
g = list(map(int, input().split()))
count3, count4 = 0,0
sum = 0
for i in g:
    if i == 3:
        count3 += 1
    if i == 4:
        count4 += 1
    if count3 == 2:
        print("Blue")
        exit()
        break
if((count3+count4) * 4 <= n):
    print("Red")
elif count3 < 2:
    print("Blue")
