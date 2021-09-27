Height=float(input("Input your Height in Centimeters: "))

Weight=float(input("Input your Weight in Kgs: "))

Height = Height/100

BMI=Weight/(Height*Height)

print("Your Body Mass Index(BMI) is: ",BMI)

if(BMI>0):

    if(BMI<=16):
       print("You are severely underweight!!")

    elif(BMI<=18.5):
        print("You are underweight!!")
            
    elif(BMI<=25):
        print("You are  perfectly Healthy! Keep it up :)")

    elif(BMI<=25.6):
        print("You have a little bit fat but overall you are healthy!!")    
        
    elif(BMI<=30):
        print("You are overweight!!")

    else: print("You are severely overweight!!")
else:("enter valid details!!")