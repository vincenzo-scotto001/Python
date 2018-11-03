myStr = input("Input a string: ")
indxInt = 0
resultStr = ''    #empty string
while indxInt < (len(myStr)):					# Line 1
	if myStr[indxInt] > myStr[indxInt + 1]:
		resultStr = resultStr + myStr[indxInt]
	else:
		resultStr = resultStr * 2
	indxInt += 1						#Line2
print(resultStr)							#Line3
