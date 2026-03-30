s1=input("Enter a string: ")
s2=input("Enter another string: ")
if len(s1)==len(s2):
    s1=s1.lower()
    s2=s2.lower()
    if sorted(s1)==sorted(s2):
        print("The strings are anagram...")
    else:
        print("The strings are not anagram...")
