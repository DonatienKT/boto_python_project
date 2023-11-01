def greet():
     print('\nHello Everybody')
greet()

def add_nu(a,b = 2):
    return a + b

# Define `divide()` with required arguments
def divide(a,b):
    return a / b

# Define 'add_num()' 
def add_num(*args):
    total = 0
    for i in args:
            total += i
    return total