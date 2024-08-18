class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        cars = [a for a in zip(position,speed)]
        cars.sort()
        stack = []
        def time(pos,mph):
            return (target-pos)/mph
        for x in range(len(cars)-1,-1,-1):
            if x == len(cars)-1:
                stack.append(time(cars[x][0],cars[x][1]))
            elif stack[-1] < time(cars[x][0],cars[x][1]):
                stack.append(time(cars[x][0],cars[x][1]))
        return len(stack)



L = Solution()
print(L.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))