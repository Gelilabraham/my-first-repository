import  random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
     top_of_range = int(top_of_range)
     gusses=0

     if top_of_range <=0:
          print("please type a number greater than zero")
          quit()

else:
     print("please type a number next time")
     quit()

random_number=random.randrange(top_of_range)
while True:

     user_guess = input("make a guess: ")
     if user_guess.isdigit():
          user_guess=int(user_guess)

          if user_guess != random_number:
               print("not correct")
               if user_guess > random_number:
                    print("hint: it is larger")
               elif user_guess < random_number:
                    print("hint: it is lower")
               else:
                    print("not correct")         
               gusses+=1
               continue
          else:
               print("you just got it!")
               print(f"you got it by {gusses} gusses")
               break
     else:
          print('enter a valid number')    

               
            
     


