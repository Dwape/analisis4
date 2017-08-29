import math

def function_f(x):
    """Applies a function f(x) to a value x passed as parameter."""
    return math.sqrt(x**2+1)-1

def function_g(x):
    """Applies a function g(x) to a value x passed as parameter."""
    return x**2/(math.sqrt(x**2+1)+1)

def test_f(tries):
    for i in range (1, tries+1):
        print(str(function_f(8**(-i))))

def test_g(tries):
    for i in range (1, tries+1):
        print(str(function_g(8**(-i))))

def test_function(tries, function):
    for i in range (1, tries+1):
        print(str(function(8**(-i))))

print('Testing function f(x):')
test_f(10)
print()
print('Testing function g(x):')
test_g(10)
#test_function(10, function_f)
