from ps import Polynomial, Solver

from os import system

degree = float(input("What is the degree of your polynomial? (Must be a positive integer less than or equal to 10) "))
if (round(degree) != degree):
    raise Exception("Degree must be an integer")
elif (degree < 1):
    raise Exception("Degree must be greater than or equal to 1")
elif (degree > 10):
    raise Exception("Degree muse be less than or equal to 10!")

polynomial = Polynomial(degree)

for coef_num in range(polynomial.degree + 1):
    system("clear")
    print("What is the value of " + chr(97 + coef_num) + " in the polynomial below:")

    polynomial.print()

    coef = float(input())
    if (coef_num == 0 or coef_num == polynomial.degree) and (round(coef) != coef):
        raise Exception("The leading coefficient and constant must be integers")
    polynomial.set(coef_num, coef)

system("clear")
polynomial.print()

solver = Solver(polynomial)
roots_str = "The possible rational roots of the polynomial are:"

for n in range(len(solver.print_roots(True))):
    root = solver.print_roots(True)[n]

    if n == len(solver.print_roots(True)) - 1:
        if len(solver.print_roots(True)) > 1:
            roots_str += " and " + root + "."
        else:
            roots_str += " " + root + "."
    else:
        roots_str += " " + root + ","

print(roots_str + "\n")

print("Choose an option for solving the polynomial:")
print("Type yes to find all the actual rational roots")
print("Type anything else to quit\n")

option = input("Option: ").strip().lower()

if option == "yes":
    roots = solver.solve()

    if len(roots) > 1:
        real_roots_str = "The actual rational roots of the polynomial are:"
    elif len(roots) == 1:
        real_roots_str = "The only rational root of the polynomial is:"
    else:
        real_roots_str = "There are no rational roots."

    for n in range(len(roots)):
        root = solver.solve()[n][1]

        if n == len(roots) - 1:
            if len(roots) > 1:
                real_roots_str += " and " + root + "."
            elif len(roots) == 1:
                real_roots_str += " " + root + "."
        else:
            real_roots_str += " " + root + ","

    print(real_roots_str)
    print("Reminder: these are the rational roots of the polynomial; the polynomial may have irrational or complex roots that aren't listed.")

else:
    quit()