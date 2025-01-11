from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)

# Accessing enum values
print(Color.RED.value)
print(Color.GREEN.value)
print(Color.BLUE.value)

# Iterating over enum members
for col in Color:
    print(col)
