print("Area of a rectangle")
print("="*40)

height = float(input("please enter the height:  "))
base = float(input("please enter the base:  "))

area = round(height * base,2)

print("="*40)
print(f"Area of rectangle is {area}, square units")


print("*" *30)
print('convert celsius to farenheit')

celsius = float(input("celsius:  "))
farenheit = (celsius*(9/5)) + 32

print("*"*10)
print(f"{celsius} celsius equals to  farenheit => {farenheit}")


def number_is_odd(number):
    """
    number : int
    check whether is odd number
    return True  or False
    """
    if number % 2 != 0:
        return True

check = number_is_odd(17)
print(check)