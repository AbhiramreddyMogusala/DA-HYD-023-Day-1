'''
products = list(map(int, input().split(',')))

total = 0

for price in products:
    total += price

print("Total cart value =", total)

#Password analyzer
password = input("Enter password: ")
upper = 0
lower = 0
digit = 0
special = 0
for i in password:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Special characters:", special)

#Domain
email = input().split()
for mail in email:
    print(mail.split('@')[1])
'''





