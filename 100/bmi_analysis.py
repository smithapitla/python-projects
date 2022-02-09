def getBMI():

    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    bmi = weight / (height * height)
    return float(bmi)

bmi = getBMI()
BMI = str(round(bmi))
if(bmi < 18.5):
    print(f"Your BMI is "+BMI+", you are underweight ")
elif(18.5 < bmi < 25):
    print(f"Your BMI is "+BMI+", you have a normal weight ")
elif(25 < bmi < 30):
    print(f"Your BMI is "+BMI+", you are slightly overweight ")
elif(30 < bmi < 35):
    print(f"Your BMI is "+BMI+", you are obese ")
elif(bmi > 35):
    print(f"Your BMI is "+BMI+", you are clinically obese ")
