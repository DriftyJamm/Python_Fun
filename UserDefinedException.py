class MyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def CheckValue(value):
    if value < 0:
        raise MyException("Value cannot be negetive")
    print("Value is invalid")

try:
    num = int(input("Enter a number"))
    CheckValue(num)
except MyException as e:
    print(F"Error : {e}")
except ValueError:
    print("Invalid input")
