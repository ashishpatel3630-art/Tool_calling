def calculator(
    a: float,
    b: float,
    operation: str
) -> float:
    """
    ======== WELCOME TO CALCULATOR =======
    Perform a mathematical calculation.

    operation can be:
    add
    subtract
    multiply
    divide
    """

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return f"Unknown operation: {operation}"