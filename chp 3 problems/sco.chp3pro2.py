# Chapter III problem II programming exercises by Vincenzo Scotto Di Uccio

x = int(input( " Give x a value: "))
y = int(input( " Give y a value: "))
area_z = x*y

b = int(input( "Give b a value: "))
c = int(input ( "Give c a value:"))
area_d = b*c

if area_z > area_d:
    print(" The rectangle 'xy' is greater than the rectangle 'bc'")
elif area_d > area_z:
        print (" The rectangle 'bc' os greater than the rectangle 'xy'")

elif area_d == area_z:
        print (" The rectangle 'xy' and 'bc' are the same")
        
