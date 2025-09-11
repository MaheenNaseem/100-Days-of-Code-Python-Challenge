height= float(input("Height: "))
weight= float(input("Weight: "))

if height > 30:
    raise ValueError("Human heights should not be over 3 meters")

bmi = weight/height ** 2
print(bmi)