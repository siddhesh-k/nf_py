import math
import cmath

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)

    print("The area of the circle is: {:.2f}".format(area))


def calculate_months_to_save():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion of salary to be saved (as a decimal): "))
    total_cost = float(input("Enter the cost of your dream home: "))

    portion_down_payment = 0.25  # 25% down payment
    current_savings = 0
    r = 0.04  # Annual return rate on investments
    monthly_salary = annual_salary / 12
    down_payment = portion_down_payment * total_cost
    months = 0

    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)  # Investment returns
        current_savings += portion_saved * monthly_salary
        months += 1


    print("Number of months:", months)


def calculate_months_to_save_with_raise():
    annual_salary = float(input("Enter your starting annual salary: "))
    portion_saved = float(input("Enter the portion of salary to be saved (as a decimal): "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter your semi-annual salary raise (as a decimal percentage): "))

    portion_down_payment = 0.25  # 25% down payment
    current_savings = 0
    r = 0.04  # Annual return rate on investments
    monthly_salary = annual_salary / 12
    down_payment = portion_down_payment * total_cost
    months = 0

    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)  # Investment returns
        current_savings += portion_saved * monthly_salary
        months += 1

        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    print("Number of months:", months)

def fibonacci():
    n = int(input("Enter the position in the Fibonacci sequence: "))

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        print(f"The Fibonacci number at position {n} is {fib[n]}.")

def sum_of_divisors(n):
    divisor_sum = 1  # Start with 1 as 1 is a divisor for all numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # If the divisor is not the square root of n, add its pair
                divisor_sum += n // i
    return divisor_sum

def find_perfect_numbers():
    limit = 10000
    perfect_numbers = find_perfect_numbers(limit)
    print("Perfect numbers less than 10000:")
    for num in perfect_numbers:
        print(num)
    perfect_numbers = []
    for num in range(2, limit):
        if sum_of_divisors(num) == num:
            perfect_numbers.append(num)
    return perfect_numbers


def type_casting():
    n = int(input("enter an integer: "))
    result = sum(int(str(n) * i) for i in range(1,5))
    print(result)

def taylor_series():
    x = 0.5
    n = 5
    approx_exp =sum(x**i / math.factorial(i) for i in range(n))
    approx_sin =sum((-1)**i * x**(2*i + 1) / math.factorial(2*i + 1) for i in range(n))
    real_exp = math.exp(x)
    real_sin = math.sin(x)
    print(f"Taylor Series approximation of e^{x} with n={n}: {approx_exp}")
    print(f"Real value of e^{x}: {real_exp}")
    print(f"Taylor Series approximation of sin({x}) with n={n}: {approx_sin}")
    print(f"Real value of sin({x}): {real_sin}")


def quadratic_equation():
    # print(dir(cmath))
    a=complex(input("Enter the coefficient a: "))
    b=complex(input("Enter the coefficient b: "))
    c=complex(input("Enter the coefficient c: "))
    if a == 0:
        if b == 0:
            if c == 0:
                return print("The equation has infinitely many solutions.")
            else:
                return print("The equation has no solution.")
        else:
            return print(f"The equation is linear. The solution is x = {-c / b}")
    else:
        discriminant = b ** 2 - 4 * a * c
        sqrt_discriminant = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

    print(f"The quadratic equation is: ({a})x^2 + ({b})x + ({c}) = 0")

    print(f"The roots of the equation are: {root1} and {root2}")
    print(f"Root 1: {root1.real:.2f} + {root1.imag:.2f}j")
    print(f"Root 2: {root2.real:.2f} + {root2.imag:.2f}j")



while True:
    user_input = input("Enter exercise number (1-8) or 'q' to exit: ")

    if user_input != "q":
        if user_input == "1":
            calculate_circle_area()
        if user_input == "2":
            calculate_months_to_save()
        if user_input =="3":
            calculate_months_to_save_with_raise()
        if user_input == "4":
            fibonacci()
        if user_input == "5":
            find_perfect_numbers()
        if user_input == "6":
            type_casting()
        if user_input == "7":
            taylor_series()
        if user_input == "8":
            quadratic_equation()


    elif user_input == "q":
        exit()
