class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(3, 4)

# Use the + operator to add two points
p3 = p1 + p2

print(p3)  # Output: (5, 7)

# Here are some common operators that you can overload in Python:

# 1. **Arithmetic Operators**:
#    - `__add__(self, other)` for addition (`+`)
#    - `__sub__(self, other)` for subtraction (`-`)
#    - `__mul__(self, other)` for multiplication (`*`)
#    - `__truediv__(self, other)` for true division (`/`)
#    - `__floordiv__(self, other)` for floor division (`//`)
#    - `__mod__(self, other)` for modulus (`%`)
#    - `__pow__(self, other)` for exponentiation (`**`)

# 2. **Comparison Operators**:
#    - `__eq__(self, other)` for equality (`==`)
#    - `__ne__(self, other)` for inequality (`!=`)
#    - `__lt__(self, other)` for less than (`<`)
#    - `__le__(self, other)` for less than or equal to (`<=`)
#    - `__gt__(self, other)` for greater than (`>`)
#    - `__ge__(self, other)` for greater than or equal to (`>=`)

# 3. **Unary Operators**:
#    - `__neg__(self)` for negation (`-`)
#    - `__pos__(self)` for positive (`+`)
#    - `__abs__(self)` for absolute value (`abs()`)

# 4. **Bitwise Operators**:
#    - `__and__(self, other)` for bitwise AND (`&`)
#    - `__or__(self, other)` for bitwise OR (`|`)
#    - `__xor__(self, other)` for bitwise XOR (`^`)
#    - `__invert__(self)` for bitwise NOT (`~`)
#    - `__lshift__(self, other)` for left shift (`<<`)
#    - `__rshift__(self, other)` for right shift (`>>`)

# 5. **Assignment Operators**:
#    - `__iadd__(self, other)` for addition assignment (`+=`)
#    - `__isub__(self, other)` for subtraction assignment (`-=`)
#    - `__imul__(self, other)` for multiplication assignment (`*=`)
#    - `__itruediv__(self, other)` for true division assignment (`/=`)
#    - `__ifloordiv__(self, other)` for floor division assignment (`//=`)
#    - `__imod__(self, other)` for modulus assignment (`%=`)
#    - `__ipow__(self, other)` for exponentiation assignment (`**=`)

# 6. **Other Operators**:
#    - `__getitem__(self, key)` for indexing (`[]`)
#    - `__setitem__(self, key, value)` for setting indexed values (`[]`)
#    - `__delitem__(self, key)` for deleting indexed values (`del []`)
#    - `__call__(self, *args, **kwargs)` for function calls (`()`)
#    - `__len__(self)` for length (`len()`)
#    - `__repr__(self)` for the official string representation (`repr()`)

# These methods allow you to define custom behavior for these operators when used with instances of your classes. Happy coding!
