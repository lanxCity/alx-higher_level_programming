class Box:
    def __init__(self, data):
        self.data = data

b1 = Box(2)
b2 = Box(10)
b3 = Box(100)
b4 = Box(15)
b5 = Box(1)
b6 = Box(-10)

print(b2.data < b3.data)
print(b5.data < b3.data)
print(b4.data < b3.data)
print(type(b2.data))