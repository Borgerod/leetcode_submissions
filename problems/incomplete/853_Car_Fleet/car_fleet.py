class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        '''
        NOTE: km or miles are converted into cols: 
              5km/h -> 5cols/h 
              10km  -> 10cols
              likewise "h" is converted into iterations
              so all in all the speed will look like this: 
              5km/t -> 5cols/i
              which means every iteration, the carr will move 5 cols.

            position: list of positions (ALL POSITIONS ARE UNIQUE!)
                position[i]: position if i'th car 
            speed: list of speeds (km/h) (cols/h)
                speed[i]: speed if i'th car 
            n: length of position and speed (amount of cars)
            target: destination - how long the road is (km) (cols)
            
            rules: 
                - car can NOT pass another car ahead of it.
                - car can only catch up, then drive at the same speed as the car ahead of it. 
                    (catch up + drive together)

                - 'car-fleet': a position containing one or more cars (a set) ->  same position, same speed
                    - 'car-fleet': set of cars at the same position and same speed.
                    - single car is also considered a car-fleet
                - if a car catches up to a car-fleet the moment the car-fleet reaches the destination, that car is considered to be part of that car-fleet.
                - cars will allways merge into another car-fleet immediately when they catch up to each other.
                    - the car-fleet catching up, will allways merge into the car-fleet ahead.
                
            return:
                - num of 'different' car fleets that will arrive at the destination.

            Question: are we only working in whole numbers?
                if car_1 is 1 col away from target and speeds is 2;
                will it arrive in 0.5 or 1?
                I assume 1 since we cannot count half an iteration

            Example 1:

                Input: target = 10, position = [1,4], speed = [3,2]
                Output: 1
                Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination => 1 car-fleet arrives.
        '''

        '''
        Example 2:
            Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

            **  normally we would gave to adjust (-1) since were not counting 10th range(0,10)= 0 to 9 iterations.
                    so time-formula would look like this: target-position-1/speed
                but since both 0 and 10 is a position then the range needs to be range(0,11).
                    so time-formula should look like this: target-position/speed

            - to account for "0" as a position [0-10 to 0-11]) 'target' is NOT the length it is the final position.
            n = len(position) = 4
                                                                                            -> num of iterations to reach target 
            _____ destination _____ : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [target]                     target-position/speed **
            car_0:   position[car_0]: [_, _, _, _, x, _, _, _, _, _, 10] | speed[car_0]: 2 (col/h) -> 10-4/2 =  3.0 =  3
            car_1:   position[car_1]: [_, x, _, _, _, _, _, _, _, _, 10] | speed[car_1]: 2 (col/h) -> 10-1/2 =  4.5 =  5
            car_2:   position[car_2]: [x, _, _, _, _, _, _, _, _, _, 10] | speed[car_2]: 1 (col/h) -> 10-0/1 = 10.0 = 10
            car_3:   position[car_3]: [_, _, _, _, _, _, _, x, _, _, 10] | speed[car_3]: 1 (col/h) -> 10-7/1 =  3.0 =  3
            
            TIMELINE:
                                   i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [target] 
                               car_0: [_, _, _, _, x, _, 1, _, 2, _,  3], _] = i:3
                               car_1: [_, x, _, 1, _, 2, _, 3, _, 4,  _], 5] = i:5
                               car_2: [x, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], _] = i:10
                               car_3: [_, _, _, _, _, _, _, x, 1, 2,  3], _] = i:3

        answer:
            car_fleet_1: [car_0, car_3] - arrives at i:3
            car_fleet_2: [car_1] - arrives at i:5
            car_fleet_3: [car_2] - arrives at i:10
            ==> [[car_0, car_3] [car_1], [car_2]] = [fleet, fleet, fleet]
            ==> len([fleet, fleet, fleet])
            ==> 3
        '''


        # for i in range(len(position)):
        #     spd=speed[i]
        #     start=position[i]
        #     arrivesAt = int((target-position[i])//speed[i])  # '//' to make sure it is rounded up to nearest int
        #     car = {"speed":speed[i], "start":speed[i], "arrives": arrivesAt}
        #     print(f"car[{i}]:")
        #     print(f"    speed:{speed[i]}")
        #     print(f"    position:{position[i]}")
        #     print(f"    {target}-{position[i]}//{speed[i]}")
        #     print(f"    {target-position[i]}//{speed[i]}")
        #     print(f"    car[{i}] arrives at: {(target-position[i])//speed[i]}")
        #     print(f"    car[{i}] {car}")
        #     print()



        # n = len(speed) # using 'speed' because it has the smallest upper limit (less chars to deal with during huge datasets)
        # result = [0] * n #stores car-fleets 
        # stack = []  # stores arrivals
        # for i, spd in enumerate(speed):
        #     pos = position[i]
        #     print(f"i: {i} speed:{spd} position: {pos} arrives:{int((target-position[i])//speed[i])}")
        #     # while stack and speed[stack[-1]]<spd:
        #     while stack and position[stack[-1]]<pos:
        #         print(f"    pop  [{stack[-1]}] <- {stack} = {stack[:-1]}")
        #         # result[stack[-1]] = i - stack[-1]
        #         result[stack[-1]] = position[i-stack[-1]]
        #         stack.pop()

        #     print(f"    push [{i}] -> {stack} = {stack+[i]}")
        #     stack.append(i)

        # print()
        # print("speeds: ",speed)
        # print("positions: ",position)
        # print("stack: ",stack)
        # print("result: ",result)

        # Initialize an empty stack to maintain the decreasing order
        n = len(position) # using 'speed' because it has the smallest upper limit (less chars to deal with during huge datasets)
        result = [0] * n #stores car-fleets 
        result = [[]] * target #stores car-fleets 
        result = [[] for _ in range(target+1)]
        # result = [[] for _ in range(len(position))]
        stack = []  # stores arrivals

        # Iterate through each element in the input array
        # for pos in position:
        print(result)
        '''
        car[i]: pos     arrival
        car[0]: pos: 4, arrival: 3
        car[1]: pos: 1, arrival: 5
        car[2]: pos: 0, arrival: 10
        car[3]: pos: 7, arrival: 3
        '''
        for i, pos in enumerate(position):
            # While the stack is not empty and the top of the stack is less than the current element
            print("current: ", i)
            spd=speed[i]
            print(f"  target: {target}")
            print(f"  target-pos: {target-pos}")
            # print("  arrivals:")
            current_car_arrival = int(((target-pos)//spd))
            top_car_arrival = int((target-stack[-1])//spd) if stack else 0
            # if stack:
            #     print(f"    top-car: {int((target-stack[-1])//spd)}        (target-stack[-1])/spd")
            # else:
            #     print(f"    top-car: {0}       empty stack")

            print(f"  top-car (arrival): {current_car_arrival}        (target-stack[-1])/spd")
            print(f"  current-car (arrival): {top_car_arrival}     (target-pos)/spd")
            print()
            # print(f" : {}")
            print(f"  while ... (arrival) top < current:")
            print(f"            (arrival) {top_car_arrival} > {current_car_arrival}:")
            # while stack and top_car_arrival > current_car_arrival:
            while stack and stack[-1] < current_car_arrival:
            # while stack and pos < stack[-1]:
                # Pop the top element from the stack
                
                print(f"      stack[-1] -> ", stack[-1])
                # result[stack[-1]] = pos
                # result[stack[-1]] = [i]
                # result.insert(stack[-1], i)
                # result[stack[-1]].append(i)
                # result[current_car_arrival].append(i)
                result[stack[-1]] = current_car_arrival
                print(f"   inserting [num:{i}] in result at: [i:{current_car_arrival}] ==> {result}")
                # result[i] = stack[-1]

                print("       pop: ", stack)
                stack.pop()
                
                # print(f"    true")
                # print(f"    if (position) {pos} > {stack[-1]}:")
                # if pos > stack[-1]:
                #     print(f"      true")
                #     print(f"      stack[-1] -> ", stack[-1])
                #     # result[stack[-1]] = pos
                #     result[stack[-1]] = i
                #     print("       pop: ", stack)
                #     stack.pop()
                # else:
                #     print(f"      false")
                #     print(f"      CANNOT pass, MERGE")
                #     break
                #     # stack.append(pos)

            # Push the current element onto the stack
            print("     PUSH: ",pos, " -> ",stack)
            stack.append(current_car_arrival)
            print("  res: ", result)
            print()
        print("final res: ", result)
        print()


        # print(stack)

        '''
        if the car.position > top.position:
            allowed to arrive at intended destination.
        else:
            not attached to top-stack
            stack.insert(pos, -2) instead of putting it on top?
            

        '''



        return None

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # car = {"speed":speed[i], "pos":speed[i]}
        position, speed = zip(*sorted(zip(position, speed), key=lambda x: x[0], reverse=True))
        # position, speed = map(list, zip(*sorted(zip(position, speed), key=lambda x: x[0], reverse=True)))
        print(position, speed)
        result=[]
        result = [None] * len(position)
        stack=[]
        for i, pos in enumerate(position):
            current_car_arrival = int(((target-pos)//speed[i]))
            top_car_arrival = stack[-1] if stack else 0
            print(current_car_arrival)
            cnt=0
            while stack and top_car_arrival < current_car_arrival:
                print(True)
                cnt+=1

                print(f"cnt:{cnt}")
                result[i]=cnt
                stack.pop()
            stack.append(current_car_arrival)
        
        print(f"result: {result}")
        print(f"stack: {stack}")


    
        
        # length = len(result) - result.count(None)
        return len(result) - result.count(None)+len(stack)

if __name__ == '__main__':

    cases = [
        10,
        [1,4],
        [3,2],
        
        10,
        [4,1,0,7],
        [2,2,1,1],

        # 12,
		# [10,8,0,5,3],
		# [2,4,1,1,3],
		# 10,
		# [3],
		# [3],
		# 100,
		# [0,2,4],
		# [4,2,1]
    ] 

    #> OPTION 2 (for multiple inputs)
    s = Solution()
    for i in range(0, len(cases), 3):

        target = cases[i+0]
        position = cases[i+1]
        speed = cases[i+2]
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.carFleet(target, position, speed)}\n")











# # result=[]

# def monotonic_decreasing_stack(arr):
#     # Initialize an empty stack to maintain the decreasing order
#     stack = []
#     result = ['_'] * len(arr)
#     print("results before: ", result)

#     # Iterate through each element in the input array
#     # for num in arr:
#     for i, num in enumerate(arr):
#         # While the stack is not empty and the top of the stack is less than the current element
#         print(f"  i:{i} value: [{num}] stack: {stack}")
#         while stack and stack[-1] > num:
#             # Pop the top element from the stack
#             # result.append(num)
#             # result[stack[-1]] = i-stack[-1]
#             # result[stack[-1]] = num
#             result[i] = stack[-1]
#             print(f"   (stack-top) {stack[-1]} > {num} (num)")
#             print(f"   inserting [num:{num}] in result at: [i:{stack[-1]}] ==> {result}")
#             # print("     pop: ",stack[-1])
#             print(f"     pop: [{num}]")
#             stack.pop()
#         # Push the current element onto the stack
#         stack.append(num)
#         # stack.append(i)

#     # Return the stack, which now contains elements in monotonic decreasing order
#     return stack, result


# # Example usage

# arr = [2, 1, 2, 4, 3]
# print("arr:            ", arr)
# stack, result = monotonic_decreasing_stack(arr)
# print("stack:          ", stack)
# print("results before: ", result)
