#  Chapter IV problem XIII nested loop one by Vincenzo Scotto Di Uccio



def main():

    a = 1

    for b in range(8, a, -1):
            for c in range(b - 1):
                    print("*", end=" ")

            print()
main()
