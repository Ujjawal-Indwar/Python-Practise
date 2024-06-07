even = 0
for i in range(0,101):
    if i%2 == 0:
        even += i

print(f"The even numbers sum from 1 to 100 is  {even}")

total = 0
for no in range(2,101,2):
    total+= no

print(f"The even numbers sum from 2 to 100 is  {total}")