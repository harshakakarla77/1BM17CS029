import random
import string
passw=" "
nos=string.digits
spec=string.punctuation
alpha=string.ascii_letters
tot=nos+spec+alpha

n=int(input("Enter no of characters in password:"))
for i in range(n):
    passw=passw+random.choice(tot)
print(passw)
