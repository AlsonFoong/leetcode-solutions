# Time - O(1): Use of list and dictionary structures to minimize time complexity
# Space - O(n): Up to n elements stored in both structures
import random
class RandomizedSet:
    def __init__(self):
        self.data_list = []
        self.pos_map = {}
    def insert(self, val: int) -> bool:
        if val in self.pos_map:
            return False
        # Map the value to its index in the list
        self.pos_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.pos_map:
            return False
        # 1. Find the index of the element to remove and the last element
        idx_to_remove = self.pos_map[val]
        last_element = self.data_list[-1]
        # 2. Move the last element to the spot of the element we're removing
        self.data_list[idx_to_remove] = last_element
        self.pos_map[last_element] = idx_to_remove
        # 3. Remove the last element from both structures
        self.data_list.pop()
        del self.pos_map[val]
        return True
    def getRandom(self) -> int:
        # random.choice on a list is O(1)
        return random.choice(self.data_list)
# 1. remove uses a "swap and pop" technique to turn an O(n) removal operation into an O(1) operation.
# 2. Using a set with .pop() does not work because it isn't truly random.
