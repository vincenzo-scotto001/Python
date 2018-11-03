# Chapter III problem VII color mixer by Vincenzo Scotto Di Uccio

primary_color1 = input(" Please type the first primary color(red, blue or yellow): " )
primary_color2 = input(" Please type the second primary color(red, blue or yellow: " )

if primary_color1 == "red" or "blue" and primary_color2 == "red" or "blue":
    print ( " The color is purple")
elif primary_color1 == "red" or "yellow" and primary_color2 == "red" or "yellow":
    print (" The color is orange")
elif primary_color1 == "blue" or "yellow" and primary_color2 == "blue" or "yellow":
    print ("The color is green")
elif primary_color1 == primary_color2:
    print ( " Color is the same")
else:
    print ("Error")
    
