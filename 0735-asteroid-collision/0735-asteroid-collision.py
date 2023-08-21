class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        
        # there is no probelem if the incoming asteriod is going right we just add it to stack
        # if the incoming is a negative one, we can continue until the top of the stack is positive and current has not reached 0
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                current = asteroids[i]
                while stack and stack[-1] > 0:
                    top = stack.pop()
                    if abs(top) > abs(current):
                        # left goint asteroid will explode
                        stack.append(top)
                        current = 0
                        break
                    elif abs(top) < abs(current):
                        # right going asteroid will explode
                        continue
                    else:
                        # both will explode
                        current = 0
                        break
                # At the end if there is current, we add it to stack
                if current:
                    stack.append(current)
        return stack
            # print(stack)
        return stack
                