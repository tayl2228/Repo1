#Importing.
import time

#Defining local time.
right_now = time.localtime()

#Defining current date.
def currentDate():

    (print("The current date in Day - Month - Year format is:"), (print(right_now[1], right_now[2], right_now[0])), (print(" ")))

#Defining current time.
def currentTime():

    (print("The current time in your area is:"), print(right_now[3], ":", right_now[4]), (print(" ")))

#Defining Timer
def a_timer():

    seconds = int(input("How many seconds until timer goes off?"))

    D = False

    while not D:

        x = int(seconds)

        while x < seconds or x == seconds:

            x -= 1

            time.sleep(1)

            print(x)

            if x == 0:

                print("Time's up!")

                D = True

                break

        print(" ")

        input("Press enter to return to the main manu.")

        print(" ")
        

#Defining menu loop.
def mainLoop():

    program_exit = False

    while not program_exit:

        print("Main Menu:")

        print(" ")

        print("Enter 1 to view today's date.")

        print(" ")

        print("Enter 2 to view the current time.")

        print(" ")

        print("Enter 3 to view the current date and time.")

        print(" ")

        print("Enter 4 to set a timer.")

        print(" ")

        print("Enter 'e' to exit the program.")

        print(" ")

        menu_choice = input("Input your choice here: ")

        print(" ")

        if menu_choice == str(1):

            currentDate()

            input("Press enter to return to main menu.")

            print(" ")

        elif menu_choice == str(2):

            currentTime()

            input("Press enter to return to main menu.")

            print(" ")

        elif menu_choice == str(3):

            currentDate()

            currentTime()

            input("Press enter to return to main menu.")

        elif menu_choice == str(4):

            a_timer()

        elif menu_choice == 'e' or 'E':

            print("The program will exit.")

            time.sleep(5)
            
            program_exit = True

            exit()


        else:

            print("Unknown command, please try again")

            print(" ")

            mainLoop()



#calling menu loop            
mainLoop()

    

