a = int(input())

if a % 3 == 0:
    print("YES")
    if a % 5 == 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")
    if a % 5 == 0:
        print("YES")
    else:
        print("NO")