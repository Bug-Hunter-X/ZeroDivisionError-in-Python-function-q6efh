def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

result = function(10, 0)
print(result)