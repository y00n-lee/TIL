#별 찍기 - 4
n = int(input())

for i in range(n):
    print(" "* i, end="")
    print("*"*(n-i))
