class Interval(object):
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return str((self.start, self.finish))

def schedule_intervals(I):
    I.sort(lambda x, y: x.finish - y.finish) 

    X = []
    finish = 0
    for i in I:
        if finish <= i.start:
            finish = i.finish
            X.append(i)

    return X

if __name__ == '__main__':
    I = []
    I.append(Interval(1, 6))
    I.append(Interval(1, 2))
    I.append(Interval(3, 4))
    I.append(Interval(5, 7))
    I.append(Interval(5, 7))
    I.append(Interval(8, 9))
    X = schedule_intervals(I)
print "Maximum subset",X, "and has", len(X), "intervals"
