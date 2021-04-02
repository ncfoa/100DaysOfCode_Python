your_name = input("Enter your name: \n")
crush_name = input("Enter your crush's name: \n")

true = ["t","r","u","e",]
love = ["l","o","v","e"]
your_name = your_name.lower()
crush_name = crush_name.lower()
true1 = 0
love1 = 0

for i in true:
    true1 = true1 + your_name.count(i)
    true1 = true1 + crush_name.count(i)

for i in love:
    love1 = love1 + your_name.count(i)
    love1 = love1 + crush_name.count(i)

true_love = int(str(true1) + str(love1))

if true_love <= 10 or true_love >= 90:
    print(f"Your score is {true_love}%. You go together like Coke and Mentos.... Explosive")
elif true_love >= 40 and true_love <= 60:
    print(f"Your score is {true_love}%. You would do well together..")
else:
    print(f"Your score is {true_love}%.")
