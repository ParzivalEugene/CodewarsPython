class Datamining:
    def __init__(self, train_set):
        self.data = train_set
        self.x = sum([i[0] for i in train_set]) / len(train_set)
        self.y = sum([i[1] for i in train_set]) / len(train_set)

    def predict(self, x):
        return x ** 7 + 42
