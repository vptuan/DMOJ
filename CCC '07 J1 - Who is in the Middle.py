# Solution by Tuan Vuong

bow1 = int(input())
bow2 = int(input())
bow3 = int(input())

if bow1<=bow2<=bow3:
    print(bow2)
elif bow1<=bow3<=bow2:
    print(bow3)
elif bow2<=bow1<=bow3:
    print(bow1)
elif bow2<=bow3<=bow1:
    print(bow3)
elif bow3<=bow1<=bow2:
    print(bow1)
elif bow3<=bow2<=bow1:
    print(bow2)

