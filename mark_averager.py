#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a mark averager

import random


def calculate(lists):
    # this function calculates the average of percentages

    # process
    res = sum(lists) / len(lists)
    average_round = round(res, 1)

    return average_round


def main():
    # this function creates a list and lets the user enter their marks
    percentages = []
    percent = None

    # input & output
    percent = input("Enter Your Marks (%): ")

    try:

        percent_int = int(percent)
        percentages.append(percent_int)
        if percent_int < -1:
            print("\nInvalid Mark (To Low)")
        elif percent_int > 103:
            print("\nInvalid Mark (To high)")
        else:
            while True:
                if percent_int < -1:
                    print("\n Invalid Mark (To Low)")
                    break
                if percent_int > 103:
                    print("\n Invalid Mark (To high)")
                    break
                if percent_int == -1:
                    break

                percent = input("Mark (%): ")
                percent_int = int(percent)
                percentages.append(percent_int)

            percentages.pop()

            calculated_average = calculate(percentages)
            print(
                "\nYThe average of your percentages is {0}%".format(calculated_average)
            )

    except Exception:
        print("\nInvalid Input")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
