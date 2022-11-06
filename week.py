# finding the number of seconds in a day
seconds_day = 60 * 60 * 24
print(seconds_day)
# finding the number of seconds in a week
seconds_week = seconds_day * 7
print(seconds_week)
# finding the number of seconds in a month
seconds_month = seconds_day * 30
print(seconds_month)
# finding the number of seconds in a year
seconds_year = seconds_day * 365
print(seconds_year)
# using conditionals
marks=int(input("Enter the marks of the student:"))
#
#
# designing a simple chatbot using if else
print("Hello,I am a chartbot")
print("How may I help you?\n")
print("Hit 1 for software installation request")
print("Hit 2 for software update request")
print("hit 3 for software uninstall request")
print("Hit 4 for software request for repair request")
print("Hit 5 for other request")
# accepting the user input
userinput = int(input("Enter yor choice:"))
# using if else to procces the user input
if userinput == 1:
    softwareneeded = input("please provide the software name")
elif userinput == 2:
    softwareupdate = input("provide the software name to be updated")
elif userinput == 3:
    softwareuninstall = input("provide the software name to be unistalled")
elif userinput == 4:
    softwarerepair = input("provide the software name to be repaired")
else:
    otherrequest = input("provide the details of your request")
print("thank you for using our service, our team will be back in soon")