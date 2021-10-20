# Solution by Tuan Vuong

width = int(input())
cheese = int(input())

if width == 3 and cheese >= 95:
    print ("C.C. is absolutely satisfied with her pizza.")
elif width == 1 and cheese <= 50:
    print ("C.C. is fairly satisfied with her pizza.")
else:
    print ("C.C. is very satisfied with her pizza.")
