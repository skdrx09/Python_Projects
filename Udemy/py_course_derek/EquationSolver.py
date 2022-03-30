from re import X


def solve_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    x = int(num_2) - int(num_1)
    return x

equation = "x + 12 = 25"

print("The soluion is x =", solve_eq(equation))