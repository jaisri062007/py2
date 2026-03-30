pw=input("Enter your Password:")
digit=0
lower=0
upper=0
special=0
no_space=1
length=0
if len(pw)>=8 and len(pw)<=15:
    length=1
for ch in pw:
    if ch.isdigit():
        digit=1
    if ch.islower():
        lower=1
    if ch.isupper():
        upper=1
    if ch.isalnum()==0 and ch.isspace()==0:
        special=1
    if ch.isspace():
        no_space=0
if length and digit and lower and upper and special and no_space:
   print("Valid Password")
else:
    print("Invalid Password")
