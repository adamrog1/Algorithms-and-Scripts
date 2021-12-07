class randomGenerator(object):

    def __init__(self, seed=3):
        self.seed = seed

    def random(self):
        self.seed = (1103515245 * self.seed + 12345) & 0x7fffffff
        return self.seed

generator = randomGenerator(3)

print(generator.random())