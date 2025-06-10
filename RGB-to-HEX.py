"""
Written in April 2025 by Noga Levy.

This program converts a user-inputted RGB value into a hexadecimal one via two functions, and a for loop to gather the
appropriate information.
"""


def num_to_letter(n, m):
    # Initializes a list of hex letters
    letters = ["a", "b", "c", "d", "e", "f"]

    # We start off by checking one of two edge-cases: n is less than 0 (and thus, so is the r, g, or b value)
    if n < 0:
        # If the r, b, or g value is this edge case, then we can just return the hex of 00
        return "00"

    # Next, we check the second edge-case: n is more than 15 (and thus, the r, g, or b has to be bigger than 255)
    if n > 15:
        # If the r, b, or g value is this edge case, then we can just return the hex of FF
        return "ff"

    # Now that all the edge-cases have been eliminated as a possibility, we can check the normal cases

    # Loop to replace n values bigger than 9 with their corresponding letter, written in the list "letters"
    if n > 9:
        for i in range(10, 16):
            if n == i:
                n = letters[i - 10]

    # Loop to replace m values bigger than 9 with their corresponding letter, written in the list "letters"
    if m > 9:
        for j in range(10, 16):
            if m == j:
                m = letters[j - 10]

    # Returns the final result of the n and m
    return str(n) + str(m)


def rgb(r, g, b):
    # Using the previously defined function, num_to_letter, we find the hex for the r, g, and b values.

    r_value = num_to_letter(r // 16, (r % 16))
    g_value = num_to_letter(g // 16, (g % 16))
    b_value = num_to_letter(b // 16, (b % 16))

    # Now, we combine hexes from r, g, and b to form the final hexadecimal
    hexadecimal = r_value + g_value + b_value

    return hexadecimal


print("Hello! To convert from RGB to hexadecimal, please enter the following:")

RGB_list = ["red", "green", "blue"]
for color in range(3):
    RGB_list[color] = input(f"The {RGB_list[color]} RGB value: ")
    while not RGB_list[color].isdigit():
        RGB_list[color] = input("The value has been registered as a non-integer value. Please try again: ")

    while int(RGB_list[color]) > 255:
        RGB_list[color] = input("The value is too high--RGB numbers can only go up to 255. Please try again: ")
        while not RGB_list[color].isdigit():
            RGB_list[color] = input("The value has been registered as a non-digit value. Please try again: ")

print(f"The following is the equivalent hexadecimal: {rgb(int(RGB_list[0]), int(RGB_list[1]), int(RGB_list[2]))}")
