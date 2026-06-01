class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.memory = []

    def sum(self):
        result = self.num1 + self.num2
        self.memory.append(result)
        print(result)

    def multiplication(self):
        result = self.num1 * self.num2
        self.memory.append(result)
        print(result)

    def change(self, a, b):
        self.num1 = a
        self.num2 = b
