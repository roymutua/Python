def cs50():
    print("Hello, there")
    print("Lock in!")
cs50()

name = input("What is your name? ")

#Remove whitespace from str and capitalizing the first letter
name = name.strip().title()

print(f"Hello, {name},':)'")


#calculation
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round((x + y))
c = round(x / y, 2) #rounded to 2 decimal places

print(f"{z:,}") #used to input (,) after 3 digit (eg. 1,000)
print(f"{c:.2f}") #F string approach to specify how many decimal places

def main ():
    names = input("What is your name? ")
    hello(names)

def hello(to='world'):
        print(f"Hello, {to}!")

main()

def main ():
    k = float(input("What is k? "))
    print("x squared is", square(k))

def square(n):
    return n ** n

main()