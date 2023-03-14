# Formulae for calculating BMI values is BMI = weight(kg)/height^2 (m^2)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
print("BMI calculation is : " , int(bmi))