import random

computersnumb = random.randrange(0,100)

attempts = 0

print("I have thought of my number!")

guessno = False

while guessno == False:
    wdyti = float(input("What do you think my number is?: "))
   
    attempts = attempts + 1

    if wdyti == computersnumb:
        wdyti = True
        print("Well done!")
    elif wdyti>100:
        print("Please keep in mind the number must be between 1 and 100!")
    elif wdyti<0:
        print("Please keep in mind the number must be between 1 and 100!")
    elif wdyti>computersnumb:
        print("Try one more time, a bit lower")
    else:
      wdyti < computersnumb
      print("Try one more time, a bit higher")

while attempts < 10:
    print("Good Job, it took you",attempts,"attempts!")
