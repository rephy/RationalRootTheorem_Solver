from math import pow, floor
from fractions import Fraction


def remove_duplicates(list):
    existing_values = []

    for n in range(len(list)):
        value = list[n]

        if value not in existing_values:
            existing_values.append(value)

    list = existing_values

    return list

class Polynomial:

    def __init__(self, degree):
        self.degree = int(degree)
        self.coefs = [0 for n in range(int(degree) + 1)]

        self.filled_coefs = 0

    def set(self, coef_num, coef):
        if coef_num == 0 and coef == 0:
            raise Exception("a must be a non-zero value!")
        self.coefs[coef_num] = coef
        self.filled_coefs += 1

    def reduce(self):
        reduce_amount = 0

        for n in range(self.degree, -1, -1):
            coef = self.coefs[n]

            if coef == 0:
                reduce_amount += 1
            else:
                if reduce_amount == 0:
                    return False
                else:
                    new_polynomial = Polynomial(self.degree - reduce_amount)

                    i = 0
                    for old_coef in self.coefs[0:self.degree - reduce_amount + 1]:
                        new_polynomial.set(i, old_coef)
                        i += 1

                    return new_polynomial

    def print(self):
        polynomial_str = "" # will hold the polynomial to be printed

        coef_num = 0 # for keeping track of the coefficient number

        for coef in self.coefs: # looping through the polynomial's coefficients
            power = self.degree - coef_num # the power of the current term
            
            if coef_num >= self.filled_coefs:
                if coef_num == 0:
                    polynomial_str += "ax^" + str(power) # the first term of the polynomial (blank)
                else:
                    polynomial_str += " + " + chr(97 + coef_num) # adding the next term (besides the actual variable and power)
                    if power == 1:
                        polynomial_str += "x" # adding the variable in the first-degree term
                    elif power != 0:
                        polynomial_str += "x^" + str(power) # adding the variable and power in a term (power not equal to 0 or 1)
            else:
                if coef_num == 0:
                    if coef == 1:
                        polynomial_str += "x^" + str(power) # first term (not blank) where a = 1
                    elif int(coef) == coef:
                        polynomial_str += str(int(self.coefs[coef_num])) + "x^" + str(power)  # first term where a is an integer
                    else:
                        polynomial_str += str(self.coefs[coef_num]) + "x^" + str(power) # first term, a is not an integer nor is a equal to 1
                else:
                    if power == 1:
                        if coef == 1:
                            polynomial_str += " + " + "x" # add first-degree term where coef = 1
                        elif coef == 0:
                            pass # don't add a first-degree term at all if coef = 0
                        elif int(coef) == coef:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(int(self.coefs[coef_num])) + "x" # add first-degree term where coef is a positive integer not equal to 0 or 1
                            else:
                                polynomial_str += " - " + str(-int(self.coefs[coef_num])) + "x" # add first-degree term where coef is a negative integer not equal to 0 or 1
                        else:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(self.coefs[coef_num]) + "x" # add first-degree term where coef is a positive non-integer value not equal to 0 or 1
                            else:
                                polynomial_str += " - " + str(-self.coefs[coef_num]) + "x" # add first-degree term where coef is a negative non-integer value not equal to 0 or 1
                    elif power == 0:
                        if coef == 0:
                            pass # don't add a constant at all if const = 0
                        elif int(coef) == coef:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(int(self.coefs[coef_num])) # add a positive integer constant not equal to 0
                            else:
                                polynomial_str += " - " + str(-int(self.coefs[coef_num])) # add a negative integer constant not equal to 0
                        else:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(self.coefs[coef_num]) # add a positive non-integer constant not equal to 0
                            else:
                                polynomial_str += " - " + str(-self.coefs[coef_num]) # add a negative non-integer constant not equal to 0
                    else:
                        if coef == 1:
                            polynomial_str += " + " + "x^" + str(power) # add a term (power not equal to 0 or 1 and this term isn't the first term) where a = 1
                        elif coef == 0:
                            pass
                        elif int(coef) == coef:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(int(self.coefs[coef_num])) + "x^" + str(power) # add a term (power not equal to 0 or 1 and this term isn't the first term) where a = 1
                                # coef is also a positive integer not equal to 0 or 1
                            else:
                                polynomial_str += " - " + str(-int(self.coefs[coef_num])) + "x^" + str(power) # add a term (power not equal to 0 or 1 and this term isn't the first term) where a = 1
                                # coef is also a negative integer not equal to 0 or 1
                        else:
                            if abs(coef) == coef:
                                polynomial_str += " + " + str(self.coefs[coef_num]) + "x^" + str(power) # add a term (power not equal to 0 or 1 and this term isn't the first term) where a = 1
                                # coef is also a positive non-integer value not equal to 0 or 1
                            else:
                                polynomial_str += " - " + str(-self.coefs[coef_num]) + "x^" + str(power) # add a term (power not equal to 0 or 1 and this term isn't the first term) where a = 1
                                # coef is also a negative non-integer value not equal to 0 or 1

            coef_num += 1 # indicates the next term in the polynomial

        print(polynomial_str) # print the polynomial

class Solver:

    def __init__(self, polynomial):
        self.polynomial = polynomial
        self.reduced = polynomial.reduce()

        lead_coef = polynomial.coefs[0]

        lead_coef_factors = []
        constant_factors = []
        self.possible_roots = []
        self.printable_roots = []

        if not self.reduced:
            constant = polynomial.coefs[polynomial.degree]
        else:
            self.possible_roots.append(0)
            self.printable_roots.append("0")
            constant = self.reduced.coefs[self.reduced.degree]

        for n in range(1, abs(int(lead_coef)) + 1):
            if lead_coef % n == 0:
                lead_coef_factors.append(n)

        for n in range(1, abs(int(constant)) + 1):
            if constant % n == 0:
                constant_factors.append(n)

        for f1 in lead_coef_factors:
            for f2 in constant_factors:
                root = f2/f1

                fraction = Fraction(f"{f2}/{f1}")

                printable_root = str(fraction.numerator) + ("/" + str(fraction.denominator) if abs(fraction.denominator) != 1 else "")

                self.possible_roots.append(root)
                self.possible_roots.append(-root)

                self.printable_roots.append("±" + printable_root)

        self.possible_roots = remove_duplicates(self.possible_roots)
        self.printable_roots = remove_duplicates(self.printable_roots)

    def evaluate(self, x):
        sum = 0

        for n in range(len(self.polynomial.coefs)):
            coef = self.polynomial.coefs[n]
            power = self.polynomial.degree - n

            term = coef * pow(x, power)

            sum += term

        return sum

    def print_roots(self, return_cond):
        if return_cond:
            return self.printable_roots

        print(self.printable_roots)

    def solve(self):
        rational_roots = []

        for n in range(len(self.possible_roots)):
            root = self.possible_roots[n]
            printable_root = self.printable_roots[floor(n/2) if 0 not in self.possible_roots else floor((n + 1)/2)]

            sign = "-" if abs(root) != root else ""

            if self.evaluate(root) == 0:
                rational_roots.append((root, sign + printable_root[(1 if root != 0 else 0):]))

        return rational_roots