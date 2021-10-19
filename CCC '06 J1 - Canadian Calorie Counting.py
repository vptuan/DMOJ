#Solution by Tuan Vuong

calories = 0
burges = [0,461,431,420,0]
sides = [0,100,57,70,0]
drinks = [0,130,160,118,0]
desserts = [0,167,266,75,0]

calories = burges[int(input())]+ sides[int(input())] + drinks[int(input())]+ desserts[int(input())]

print("Your total Calorie count is " + str(calories) + ".")
