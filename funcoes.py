# f(x) = y 
# f(x) = 2x
# f(2) = 4
# f(5) = 10

# def helloWorld():
#     print("Hello World")

# helloWorld()

# def helloPeople(name):
#     print(f'Olá, {name}!')

# helloPeople("Pedro")

# def double(n):
#     return n * 2

# print(double(5))    

# def multiTwoNumbers(a, b):
#     """ Multiplica dois números """
#     return a * b

# print(multiTwoNumbers(5, 7))

x = 5 # variável global
def soma():
    x = 10 # variável local
    print(x)
    return x + 1

soma()
print(x)    