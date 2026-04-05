class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in zip(position, speed)]
        cars = list(zip(position, speed, time))
        cars.sort(key=lambda x: x[0], reverse=True)
        
        print(cars)
        stack = []
        for car in cars:
            if not stack or stack[-1][2] < car[2]:
                stack.append(car)
            # else:
            #     while stack and stack[-1][2] >= car[2]:
            #         stack.pop()
            #         stack
        return len(stack)

