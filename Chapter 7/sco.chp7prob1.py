# Chapter VII problem I by Vincenzo Scotto Di Uccio

def main():
    total= 0

    x = 7

    sales = [0] * x

    a = 0

    day = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday", "Saturday", "Sunday"]

    for a in range(x):
        print(" Enter the amount of the sales for : ", day[a])
        sales[a] =float(input(" Enter the sales here : "))

        total += sales[a]

    print ("Total for the week is : ", total)

main()

