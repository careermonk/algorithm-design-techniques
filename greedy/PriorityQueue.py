class PriorityQueue(list):
    """Priority queue clas."""
    
    def __init__(self):
        """Create an empty priority queue."""
        self.__entries = []
        
    def add(self, key, value):
        """Add new entry with specified key and value to this priority queue."""
        new_entry = (key, value)
        self.__entries.append(new_entry)
        self.__entries.sort(key = lambda x: x[0])
        
    def get_min_key(self):
        """Return a minimum key value in this priority queue."""
        return self.__entries[0][0]
    
    def get_min_value(self):
        """Return a value associates with the min. value key in this queue."""
        return self.__entries[0][1]
    
    def extract_min(self):
        """Remove and return an entry with min. key."""
        min_entry =  self.__entries[0]
        self.__entries.pop(0)
        return min_entry
        
    def show(self):
        for (k, v) in self.__entries:
            print("(%s, %s)" % (str(k), str(v)))
    
    def empty(self):
        return len(self.__entries) == 0
