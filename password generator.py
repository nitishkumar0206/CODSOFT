# Password generator 
import random #for generating random values we use import random 
def generatepassword():#function define 

    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+123456789"

    password=""

    for i in range(n):
        #random characters
        password=password+random.choice(characters)

    return password
    
if __name__=="__main__":
    n=10
     #length of python(no. of times loop run)
    password=generatepassword()#fuction call
    print("The password is :",password)

    #End 