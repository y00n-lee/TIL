h, m = map(int, input().split())

if m - 45 < 0:
    if h-1<0:
        print(23, m + 15) # 60 + (m - 45) == m + 15
    else:
        print(h - 1, m + 15)  # 60 + (m - 45) == m + 15

else: print(h, m-45)