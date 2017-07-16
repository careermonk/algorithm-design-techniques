class ClassTimings(object):
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return str((self.start, self.finish))

class ClassRoom(object):
    def __init__(self, roomNumber = 1, finish=0):
        self.roomNumber = roomNumber
        self.finish = finish

def schedule_classes(I):
    I.sort(lambda x, y: x.start - y.start) 
    classRooms = []
    classRooms.append(ClassRoom())
    finish = 0
    for i in I:
        scheduled = False
	roomNumber = 1
        for c in classRooms:
            if c.finish <= i.start:
                print "Scheduling (", i.start, i.finish, ") in classroom ", c.roomNumber
                c.finish = i.finish
                scheduled = True
                break
        if (scheduled == False):
            roomCount = len(classRooms) + 1
            finish = i.finish
            classRooms.append(ClassRoom(roomCount, finish))
            print "Adding new classroom", roomCount
            print "Scheduling (", i.start, i.finish, ") in classroom ", roomCount
    return roomCount

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
