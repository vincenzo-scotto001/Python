#Chapter IV problem II calories burned by Vincenzo Scotto Di Uccio


def main():

    cal = 4.2

    total = 0

    print("If you burn 4.2 calories per minute: ")

    for minutes in range(10,35,5):
        total += minutes + cal
        print("For", minutes, "minutes you burn" , total, "calories!")        
main()
