# Time: O(n) - Single traversal of list
# Space: O(1) - Only simple values being tracked
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        tank = 0
        index = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Restart at next station
                tank = 0
                index = i + 1
        return index
# 1. If you start at gas[0] and fail at gas[i], you can conclude that any starting location between gas[0] and gas[i]
#    (inclusive) cannot be the answer. Therefore, restarting at the next station is the only option.
