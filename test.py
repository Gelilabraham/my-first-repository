print("welcme to my computer quiz")
player = input("Do you want to play a game?(type yes to continue) ").lower()
if player != "yes":
    print("you're just quit")
    quit()
else:
    print("OK, let's just start:)")
score = 0
answer = input("1.what does RAM refers to? ").lower()
if answer == "random access memory":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")
answer = input("2.what does CPU refers to? ").lower()
if answer == "central processing unit":
    print("CORRECT")
    score+=10
else:
    print("NOT CORRECT")
answer = input("3.what is the capital of German? ").lower()
if answer == "berlin":
    print("CORRECT")
    score+=10
else:
    print("NOT CORRECT")

answer = input("4.who is the inventor if dynamo? ").lower()
if answer == "michael faraday":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")

answer = input("5.which metal is liquid at room temprature? ").lower()
if answer == "mercury":
    print("CORRECT")
    score+=10
else:
    print("NOT CORRECT")

answer = input("6.what does GPU refers to? ").lower()
if answer == "graphical processing unit":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")

answer = input("7.which planet is known as the red planet? ").lower()
if answer == "michael faraday":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")

answer = input("8.what  is the tallest mountain in the world? ").lower()
if answer == "mount everest":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")

answer = input("9.who wrote the novel 1984? ").lower()
if answer == "gorge orwell":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")

answer = input("10.In what year was the first iphone released? ").lower()
if answer == "2007":
    print("CORRECT")
    score += 10
else:
    print("NOT CORRECT")
print("you got",score,"out of 100")



