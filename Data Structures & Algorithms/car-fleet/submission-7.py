class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for pos, spd in zip(position, speed):
            pair.append([pos, spd])
        pair.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(pair) - 1, -1, -1):
            time = (target - pair[i][0]) / pair[i][1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        
        return len(stack)

        