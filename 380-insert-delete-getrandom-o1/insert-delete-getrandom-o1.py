class RandomizedSet:

    def __init__(self):
        self.obj = set()
        self.lists = []

    def insert(self, val: int) -> bool:
        if val in self.obj:
            return False
        self.obj.add(val)
        self.lists.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val in self.obj:
            self.obj.remove(val)
            idx = self.lists.index(val)
            temp = self.lists[-1]
            self.lists[-1] = self.lists[idx]
            self.lists[idx] = temp
            self.lists.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lists)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()