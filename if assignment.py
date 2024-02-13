height=float(input("Enter Height:"))
weight=float(input("Enter Weight:"))

print("Your BMI is equal to:",  weight/height)

BMI=float(input("Enter your BMI:"))

if BMI >=18.5 and BMI <=25:
    print("You are healthy")
elif BMI>=25 and BMI<=30:
    print("You are indeed overweight bro")
elif BMI>=30 and BMI<=50:
    print("You are obese")

else:
    print("You are Underweight")

