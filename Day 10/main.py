# def format_name(f_name, l_name):
#     return f"{f_name.title()} { l_name.title()}"

# print(format_name("AngEla", "YU"))


# calculator
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    should_continue = True
    num1 = float(input("Enter first number: "))
    for operator in operations:
        print(operator)

    while should_continue:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("Enter second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continuee = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: "
        )
        if continuee.lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
