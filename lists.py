#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 2, 2021
# Rounds off decimal numbers


def round_off_decimal(user_decimals, number_var):
    final_digit = ((number_var[0] * (10 ** user_decimals)) + 0.5)
    return final_digit


def main():
    number_var = []
    user_input1 = (input("Enter your decimal number: "))

    try:
        user_number = float(user_input1)
        user_input2 = (input("Round how many decimals off: "))
        try:
            user_decimals = int(user_input2)
            number_var.append(user_number)
            round_off_decimal(user_decimals, number_var)
            final_number = int
            final_number = round_off_decimal(user_decimals, number_var)
            print(final_number)
        except Exception:
            print("{} is not a positive integer".format(user_input2))
    except Exception:
        print("{} is not a decimal number".format(user_input1))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
