
def first_print():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                Warning                                *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*   1. You must need dump file.                                         *")
    print("*   2. You can't recover all files if dump data is damaged.             *")
    print("*   3. The recovered file may not have normal information.              *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")


def isContinue():
    print()
    print()
    ans = input("Do you want to continue?  (y/n) ")
  
    if ans == "N" or ans == "n":
        print("No") # change this part after merging
    elif ans == "Y" or ans =="y":
        print("Yes")   # change this part after merging
    else:
        print("Wrong command")

   
   


first_print()
isContinue()
