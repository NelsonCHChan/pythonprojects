print("hello, welcome to nelson trivia!")

ans = input("are you ready to play (yes/no):")

score = 0
total_q = 4

if ans.lower() == "yes":
    print("winner winner chicken dinner")
else:
    print("you suck")

ans = input("1. What is my favourite japanese dish?")
if ans.lower() == "katsu curry":
    score += 1
    print("correct")
else:
    print("you suck")

ans = input("2. What is 2 + 9 + 8 x 7?")
if ans == str(67):
    score += 1
    print("correct")
else:
    print("you suck")

ans = input("3. What is better AWS or Azure?")
if ans == "AWS":
    score += 1
    print("correct")
else:
    print("you suck")

ans = input("4. What is my dogs name?")
if ans.lower() == "miso":
    score += 1
    print("correct")
else:
    print("you suck")
