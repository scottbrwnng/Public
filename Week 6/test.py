name1 = "Y K"
height1 = 2
weight1 = 90

name2= "YK's sister"
height2 = 1.8
weight2 = 70

name3 = "Yk's brother"
height3 = 2.5
weight3 = 160

def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg // (height_m **2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calc(name1, height1, weight1)
result2 = bmi_calc(name2, height2, weight2)
result3 = bmi_calc(name3, height3, weight3)
print(result1,result2,result3)
