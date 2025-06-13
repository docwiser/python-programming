import random
computerNumber = random.randint(1,9)
round = 1
totalRound = int(input("How many rounds you want to play?"))
while round <= totalRound:
 print(f"Current round: {round}. You have {totalRound-round} rounds left.")
 userInput = int(input("Choose a number, will see you can match my chosen number or not:"))
 if userInput < computerNumber:
  print("Sorry, your number is les than my number")
 elif userInput > computerNumber:
  print("Sorry, your number is grator than my number")
 else:
  print("Wel done! you've chosed the correct number!")
  break
 round += 1
