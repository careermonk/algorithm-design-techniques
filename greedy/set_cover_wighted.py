import itertools
from heapq import *

class PriorityQueue:
    def __init__(self):
        self._pq = []
        self._entry_map = {}
        self._counter = itertools.count()

    def add(self, element, priority = 0):
        '''Add a new element or update the priority of an existing element'''
        if element in self._entry_map:
            entry = self._entry_map.pop(element)
            entry[-1] = 'removed'
        count = next(self._counter)
        entry = [priority, count, element]
        self._entry_map[element] = entry
        heappush(self._pq, entry)

    def extract_min(self):
        '''Remove and return the lowest priority element.'''
        while self._pq:
            priority, count, element = heappop(self._pq)
            if element is not 'removed':
                del self._entry_map[element]
                return element

    def __len__(self):
        return len(self._entry_map)

infinity = float("infinity")

def set_cover(F, w):
    udict = {}
    C = list()
    s = [] # During the process, F will be modified. Make a copy for F.
    for index, item in enumerate(F):
        s.append(set(item))
        for j in item:
            if j not in udict:
                udict[j] = set()
            udict[j].add(index)

    pq = PriorityQueue()
    cost = 0
    coveredElements = 0
    for index, item in enumerate(s): # add all sets to the priorityqueue
        if len(item) == 0:
            pq.add(index, infinity)
        else:
            pq.add(index, float(w[index]) / len(item))

    while coveredElements < len(udict):
        a = pq.extract_min() # get the most cost-effective set
        C.append(a) # a: set id
        cost += w[a]
        coveredElements += len(s[a])
        # Update the sets that contains the new covered elements
        for m in s[a]: # m: element
            for n in udict[m]:  # n: set id
                if n != a:
                    s[n].discard(m)
                    if len(s[n]) == 0:
                        pq.add(n, infinity)
                    else:
                        pq.add(n, float(w[n]) / len(s[n]))
        s[a].clear()
        pq.add(a, infinity)
                        
    return C, cost

if __name__ == "__main__":
    F = [[1, 2, 3, 4, 5, 6], [5, 6, 8, 9], [1, 4, 7, 10], [2, 5, 7, 8, 11], [3, 6, 9, 12], [10, 11]]
    w = [1, 2, 3, 4, 5, 6]
    C, cost = set_cover(F, w)
    print F
    print w
    print "Selected subsets:", C
    print "cost:", cost
