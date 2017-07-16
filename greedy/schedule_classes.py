class ClassTimings(object):
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return str((self.start, self.finish))

def schedule_classes(I):
    I.sort(lambda x, y: x.start - y.start) 
    count = 1
    finish = 0
    for i in I:
        if finish <= i.start:
            print "Scheduling (", i.start, i.finish, ") in classroom ", count
            finish = i.finish
        else:
            count = count + 1
            print "Adding new classroom", count
            print "Scheduling (", i.start, i.finish, ") in classroom ", count
            finish = i.finish
    return count

if __name__ == '__main__':
    I = []
    I.append(ClassTimings(1, 6))
    I.append(ClassTimings(5, 8))
    I.append(ClassTimings(6, 8))
    I.append(ClassTimings(1, 2))
    I.append(ClassTimings(3, 4))
    I.append(ClassTimings(5, 7))
    I.append(ClassTimings(8, 9))
schedule_classes(I)
