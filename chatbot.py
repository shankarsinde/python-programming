# designing a shivamogga helpline service chartbot
print("Welcome to shivamogga help line service")
print("How can we help you")
print("press 1 for Electicity problem")
print("Press 2 for Road problem")
print("Press 3 for Drainage problem")
print("Press 4 for Neighbour's problem")
print("press 5 for other problems")
# accepting the user input
userinput = int(input("Select your problem number"))
# using nested if condition for taking the user input
if (userinput == 1):
  userinput = int(input("enter your electicity problem"))
  print("Hit 1 for House electicity problem")
  print("Hit 2 for Street light problem")
  if userinput == 1:
      input("tell me the problem your facing with electricity ")
  if userinput == 2:
      input("tell me the street light problem")
      breakpoint()
elif userinput == 2:
    input(" give us a photo copy of your road condition")
elif userinput == 3:
    input(" what damage has happen to your drainage ")
elif userinput == 4:
    input(" tell us what they are doing and give their name")
else:
    other_problems = input(" tell us your other problems")
print("thank you , our team  will try to fix your problem")






