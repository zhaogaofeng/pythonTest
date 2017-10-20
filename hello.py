height = input("请输入您的身高")
weight = input("请输入体重")
height = float(height)
weight = float(weight)
bmi = weight / (height * height)
if bmi < 18.5:
    result = "过轻"
elif bmi < 25:
    result = "正常"
elif bmi < 28:
  	result ='过重'
else :
	result='肥胖'
print(result)