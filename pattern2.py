n=input("Enter a string:")
opt=" "
for x in n:
    if x.isalpha():
        opt+=x
        prev=x
    else:
        opt=opt+prev*(int(x)-1)
print(opt)
