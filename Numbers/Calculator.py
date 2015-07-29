#Make a calculator.
#choice = input("Pick Addition/Subtraction/Multiplication/Division: ")
#num1 = input("Pick a number: ")
#num2 = input("Pick a second number: ")


class Addition():
    
    def __init__(self):
    
        print("Addition")
             
    def add(self,num1,num2):
        print(int(num1) + int(num2))
    
class Subtraction():
    def __init__(self):

        print("Subtraction")
    def sub(self,num1,num2):
        print(int(num1) - int(num2))

class Multiplication():
    def __init__(self):
    
        print("Multiplication")
    def mult(self,num1,num2):
        print(int(num1) * int(num2))

class Division():
    def __init__(self):
    
        print("Division")
    def div(self,num1,num2):
        print(int(num1) / int(num2))



def user_Calc():
    while True:
        choice = input("Select either Addition/Subtraction/Multiplication/Division or Exit to quit: ")
        if choice == "Exit":
            print("Program terminated...")
            break
        print("Give me two numbers: ")
        num1 = input("1) ")
        num2 = input("2) ")
        if choice == "Addition":
            add = Addition()
            add.add(num1,num2)
        elif choice == "Subtraction":
            sub = Subtraction()
            sub.sub(num1,num2)
        elif choice == "Multiplication":
            mult = Multiplication()
            mult.mult(num1,num2)
        elif choice == "Division":
            div = Division()
            div.div(num1,num2)
        
user_Calc()
