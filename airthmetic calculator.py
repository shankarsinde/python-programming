# calculator using if else condition
import ch as ch

print("1.Add")
print("2.substract")
print("3. multiply")
print("4.Divide")
#input choice
ch=int(input("Enter choice : "))
if ch == 1:
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = a+b
    print("sum =",c)
elif ch == 2:
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = a-b
    print("Difference = ",c)
elif ch == 3:
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = a*b
    print("product = ",c)
elif ch == 4:
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = a/b
    print("quotient = ",c)
else:
    print("Invalid Choice")

