#Chapter III problem VIII hot dog cookout by Vincenzo Scotto Di Uccio

attendance = int(input("How many people will be coming to this cookout? "))
eaters = int(input(" How many hot dogs per person? "))

hot_dogs = 10
buns = 8
leftover_dogs = 0
leftover_buns = 0


dog_amount = attendance * eaters

package_dogs = (dog_amount // hot_dogs)
package_dogsr = dog_amount % hot_dogs
if package_dogsr !=0:
    package_dogs = package_dogs + 1
    package_dogsr = hot_dogs - package_dogsr

package_buns = dog_amount // buns
package_bunsr = dog_amount % buns
if package_bunsr != 0:
    package_buns = package_buns + 1
    package_bunsr = buns - package_bunsr

#leftover_dogs = (package_dogs *10) - dog_amount

#leftover_buns = (package_buns *8) - dog_amount

print(" This is the what you need: ")

print(" Total amount of hot dogs: ", dog_amount)

print (" Total amount of hot dog packages: " , package_dogs)

print ( " Total amount of bun packages: " , package_buns)

print ( " Leftover for hot dogs: ", leftover_dogs)

print ( " Leftover for buns", leftover_buns)








