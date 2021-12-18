#!/usr/bin/env python3
# Created by: Ketia Gaelle Kaze
# Created on: Dec 13, 2021
# This program asks the user to enter two numbers
# It then compares the two numbers to show which number is larger or smaller
# than the other or if both numbers are equal

def main():
    # Get first_number_as_string from the user
    first_number_as_string = input("\033[1;36;38mEnter first number: ")
    # Cast first_number_as_string to an integer
    try:
        first_number_as_int = int(first_number_as_string)
        # Get second_number_as_string from the user
        second_number_as_string = input("\033[1;36;38mEnter second number: ")
        print("")
        # Cast second_number_as_string to an integer
        try:
            second_number_as_int = int(second_number_as_string)
            # compare the inputs
            if first_number_as_int < second_number_as_int:
                print(first_number_as_string + " is smaller than "
                      + second_number_as_string)
                print("")
                ask_again()
            elif first_number_as_int > second_number_as_int:
                print(first_number_as_string + " is larger than "
                      + second_number_as_string)
                print("")
                ask_again()
            else:
                print(first_number_as_string + " is equal to " +
                      second_number_as_string)
                print("")
                ask_again()
        except ValueError:
            print(second_number_as_string + " is not an integer")
            print("")
            ask_again()
    except ValueError:
        print(first_number_as_string + " is not an integer")
        print("")
        ask_again()


def ask_again():
    # Ask user if they want to play the game again
    ask_to_play = input("\033[1;33;38mwould you like to play"
                        "again :)?Please choose either y/n: ")
    if ask_to_play == "Y" or ask_to_play == "y":
        main()
    elif ask_to_play == "N" or ask_to_play == "n":
        print("")
        print("\033[1;34;38mThank you for playing.Hope you enjoyed the game!")
    else:
        print("\033[1;34;38mPlease enter either y/n")
        ask_again()


if __name__ == "__main__":
    main()
