from tkinter import *
from random import *
man = Tk()


def roller():
    dice = ["\u2680","\u2681", "\u2682","\u2683","\u2684","\u2685"]
    lab.config(text=f"{choice(dice)}",font=("times",200))
    lab.pack()


man.geometry("500x500")
man.title("DICE")
B = Button(man,text="Click to Roll...",font=("Ariel",20),width=20,command=roller)
B.pack(padx=10,pady=10)
lab = Label(man,text="")

if __name__ == '__main__':
    man.mainloop()
def prime(n):
    if type(n) == str:
        print("invalid input -_-")
        n = int(input("Enter a number >> "))
        prime(n)
    else:
        # this checker function check the given number and call result function
        def checker(n):
            counter = 0
            if n < 0:
                s = -1 * n
                if all(s % j for j in range(2, s)):
                    counter += 1
            else:
                if all(n % j for j in range(2, n)):
                    counter += 1
            result(counter, n)

        # this result function print that the given number is a prime or not and
        #  if the number is negative it call negative function
        def result(count, n):
            if count == 0:
                print(n, "is not a prime")
            else:
                print(n, "is a prime")
            n += 1
            if n < 0:
                negative(n)
            else:
                if all(str(n)[0] == j for j in str(n)) and len(str(n)) >= 2:
                    final_one(n)
                else:
                    prime(n)

        # negative numbers was handled by this negative function
        def negative(neg_num):
            s = -1 * neg_num
            if all(str(s)[0] == j for j in str(s)) and len(str(s)) >= 2:
                final_one(neg_num)
            else:
                prime(neg_num)

        # this final_one function is for the last number that is the number that contain same numbers
        def final_one(num):
            count = 0
            if num < 0:
                s = -1 * num
                if all(s % j for j in range(2, s)):
                    count += 1
            else:
                if all(num % j for j in range(2, num)):
                    count += 1
            final_result(count, num)

        # this final result is going to check the final number result and print its a prime/not
        # and stop the recursion
        def final_result(count, n):
            if count == 0:
                print(n, "is not a prime")
                return
            else:
                print(n, "is a prime")
                return

        # calling the checker function to start the program
        checker(n)


if __name__ == "__main__":
    prime("a")
