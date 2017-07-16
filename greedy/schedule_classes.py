class ClassTimings(object):
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return str((self.start, self.finish))

def schedule_classes(I):
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
    I.append(ClassTimings(1, 6))
    I.append(ClassTimings(1, 2))
    I.append(ClassTimings(3, 4))
    I.append(ClassTimings(5, 7))
    I.append(ClassTimings(5, 7))
    I.append(ClassTimings(8, 9))
    X = schedule_classes(I)
print "New room for classes",X, "and need total of ", len(X), "rooms"
