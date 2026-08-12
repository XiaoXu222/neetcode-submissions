class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
        
        
        
        
        
        # stack = []
        # pairs = [(p, s) for p, s in zip(position, speed)]
        # pairs.sort()

        # for pair in pairs:
        #     time = (target - pair[0]) / pair[1]
        #     while stack and time >= stack[-1]:
        #         stack.pop()
        #     stack.append(time)
        
        # return len(stack)
        