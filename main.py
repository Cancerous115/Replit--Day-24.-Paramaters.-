import random
side=int(input("How many sides should your dice have?"))

playgame="yes"
def rollDice(side):
  print("you rolled",random.randint(1,side))
while playgame=="yes":
  rollDice(side)
  playgame=input("Roll again?")
