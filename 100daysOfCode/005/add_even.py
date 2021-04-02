# Add all even numbers from 1 to 100
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num

print("evens")
print(total)

# for fun
total2 = 0
for num in range(1, 101):
    if num % 2 != 0:
        total2 += num

print("Odds")
print(total2)
print("Add it all up")
print(total + total2) # Will be 5050