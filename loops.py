print("Showing Even and Odd numbers seperately")

count_five = 0
count_ten = 0
for i in range(1, 101):
    if i%2 == 0:
        if i%5 == 0:
            count_five += 1
        if i%10 == 0:
            count_ten += 1
        print(f"{i} is even")
    else:
        if i%5 == 0:
            count_five += 1
        if i%10 == 0:
            count_ten += 1
        print(f"{i} is odd")

print(f"multiples of 5: {count_five}")
print(f"multiples of 10: {count_ten}")

for i in range(1, 100):
    if i%5 == 0:
        print(f"{i} is multiple of 5")
    
    if i%10 == 0:
        print(f"{i} is multiple of 10")
