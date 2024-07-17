# Simple Calculator by Python Programming
#Defining functions
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select operation you want to run in calculator:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#loop
while True:
    choice=input("Enter choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
      try:  
        num1=float(input("Enter first number :"))
        num2=float(input("Enter second number :"))
      except ValueError:
        print("Error.Please enter valid number.")   
        continue 
      if choice =='1':
         print(num1,"+",num2,"=",add(num1,num2))  #declaring functions
      elif choice =='2':
         print(num1,"-",num2,"=",subtract(num1,num2))      
      elif choice =='3':
         print(num1,"*",num2,"=",multiply(num1,num2))  
      elif choice =='4':
         print(num1,"/",num2,"=",divide(num1,num2))      
      answer=input("Did you get your answer (yes/no):")
      if answer=="yes":
         print("Thank you ")
         break
      else:
         print("Invalid input")