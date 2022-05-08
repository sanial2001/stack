class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
                # print(stack)
        return stack
