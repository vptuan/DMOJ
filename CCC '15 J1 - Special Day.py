# Solution by Tuan Vuong

month = int(input())
day = int(input())

special = 218

if (month*100+day == special):
    print("Special")
elif (month*100+day < special):
    print("Before")
elif (month*100+day > special):
    print("After")
