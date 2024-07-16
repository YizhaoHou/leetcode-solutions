class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        if len(gas) == 1:
            return 0
        i = 0
        while i < len(gas):
            if gas[i] - cost[i] <= 0:
                i = i + 1
                continue
            myGas = gas[i] - cost[i]
            for j in range(len(gas) - 1):
                myGas = myGas + gas[(j + 1 + i) % len(gas)] - cost[(j + 1 + i) % len(gas)]
                if myGas < 0:
                    i = (j + 1 + i) % len(gas) + 1
                    break
                if j == len(gas) - 2:
                    return i
        return -1
        
