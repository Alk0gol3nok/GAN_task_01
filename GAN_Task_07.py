import random
x = [i for i in range(10)]
print(x)
random.shuffle(x)
print(x)
random.shuffle(x)
print(x)


def shuffle(self, x, random=None):
    if random is None:
        randbelow = self._randbelow
        for i in reversed(range(1, len(x))):
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]
    else:
        _int = int
        for i in reversed(range(1, len(x))):
            j = _int(random() * (i + 1))
            x[i], x[j] = x[j], x[i]
