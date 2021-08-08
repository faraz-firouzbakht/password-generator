import random

lower= "abcdefghijklmnopqrstvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTVWXYZ"
number= "1234567890"
symbol= "@#$%^&*()_-[]}{/><,."
all= lower+ upper+ number+ symbol
length=14
password= "".join(random.sample(all, length))
password2=random.sample(all, length)


print(password)


