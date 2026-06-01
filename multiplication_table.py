class mTable:
    def __init__(self, n):
        self.n = n

    def show(self):
        for i in range(1, 11):
            result = self.n * i
            s = '{} x {} = {}'.format(self.n, i, result)
            print(s)
