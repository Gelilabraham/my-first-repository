print("welcome to my computer quiz")

playing = input("do you wnat to play?(yes  or q to quit) ").lower()
if playing != "yes":
    quit()
else:
    score = 0
    print("oay let's play!")
    answer = input("1.what RAM stands for? ")
    if answer.lower() == "random access memory":
        print("correct")
        score +=1
    else:
        print("not correct!")

    answer = input("2.what CPU stands for? ")
    if answer.lower() == "central processing unit":
        print("correct")
        score +=1
    else:
        print("not correct")

    answer = input("3.what ICMP stands for")
    if answer.lower() == "internet control message protocol":
        print("correct")
        score +=1
    else:
        print("not correct!")

    answer = input("4.what DNS stands for? ")
    if answer.lower() == "domain name system":
        print("correct")
        score +=1
    else:
        print("not correct")

    answer = input("5.what UDP stands for? ")
    if answer.lower() == "user datagram protocol":
        print("correct")
        score+=1
    else:
        print("not correct!")

    answer = input("6.what OSINT stands for? ")
    if answer.lower() == "open source intelegence":
        print("correct")
        score +=1
    else:
        print("not correct")

    answer = input("7.what OSI stands for?")
    if answer.lower() == "open source interconnection":
        print("correct")
        score +=1
    else:
        print("not correct!")

    answer = input("8.what SSH stands for? ")
    if answer.lower() == "secure shell":
        print("correct")
        score +=1
    else:
        print("not correct")

    answer = input("9.what GHD stands for? ")
    if answer.lower() == "google hacking database":
        print("correct")
        score +=1
    else:
        print("not correct!")

    answer = input("10.what OS stands for? ")
    if answer.lower() == "opareting system":
        print("correct")
        score +=1
    else:
        print("not correct")

    print(f"you got {score} out of 10")
    if score <5:
        print("you're failed try again :( ")

    