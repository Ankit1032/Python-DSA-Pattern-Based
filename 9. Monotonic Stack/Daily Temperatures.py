class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #Temp can have duplicate numbers so we cannot use the hashmap technique

        warm_days = [0] * len(temperatures)
        stack = [] #will store indices

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_ele_index = stack.pop()
                days = i - prev_ele_index
                warm_days[prev_ele_index] = days
            stack.append(i)

        return warm_days
