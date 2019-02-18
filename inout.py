#prompting user to put there date of birth.
dop = input("please enter your year of birth")
#change input immediately to integer since its captured as string.
year = int (dop)
age = 2019 - year
if age<18:
    print("user is a minor")
elif age >= 18 and age <= 36:
    print("user is youth")
else:
    print("user is an elder")
