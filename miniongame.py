def minion_game(string):
    string=string.upper()
    Kevin = 0
    Stuart = 0
    for i in range(len(s)):
        if string[i] in "AEIOU":
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    if Kevin == Stuart :
        print("Draw")
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print("Kevin", Kevin)
