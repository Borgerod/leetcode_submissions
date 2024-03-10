class Solution:

    def trap(self, height: list[int]) -> int:
        ''' THE PROPER SOLUTION'''
        trapped_water = 0 
        l , r = 0, len(height) - 1
        max_l, max_r = 0, 0 

        while (l < r):

            if height[l]<height[r]:
                if height[l]>max_l: 
                    max_l=height[l]
                else:
                    trapped_water += max_l - height[l]
                l+=1
            else:
                if height[r]>max_r:
                    max_r=height[r]
                else:
                    trapped_water += max_r - height[r]
                r-=1
        return trapped_water 


    def trap_experimental(self, height: list[int]) -> int:
        ''' Using a experimantal pixel-matrix formula i created '''
        '''#!ALMOST FINISHED
        DESCRIPTION OF THE IDEA
        the goal of this solution was to simplyfy the rather complicated task, due to two extra factors:
        and the solution basicly works just like how a human would read the graph with our eyes. 
            
            The challange:
                - The pols had a volume to them that you had to take account for. #? Meaning, the pols were closer to a coordinate (that you had to write a formula for) than a graphpoll  
                - Unlike "Container With Most Water" the water volume was not independant and you would have to take the pols within the volume into consideration. #? aka, you had to subtract the volums of the polls within the water volume, from the water volume.
            There two factors results in you having "alot of balls in the air". 
        
        So this solution solved this challange by simplyfying it, and which also was a low math solution. 
        It did this by doing two things:
            (1) disregard it as polls and volumes, and think of it as pixels (a 1x1 volume box) on a matrix (a stack of rows)
                    #* Description of what the keywords mean:
                    lvl: is the term used to describe 1 lvl of height.(the y-axis on the graph) and is the "row" for the matrix. e.g.: height[0]=2 => lvl 1 and 2 is filled. all the other lvls above lvl2 is filled with "void". 
                    pixel: since the graph has a 1:1 ration on the x:y -axis, then .e.g.: 
                            if height[0] = 1 then we know that xy[0,0]-xy[1,1] contained a pixel.
                            if height[0] > 0 then we also know that xy[0,0]-xy[1,1] contained a pixel (along with x-amount of other lvls above).
                            if height[0] = 0 then is is a void of wall-pixels at all levels. 
                    wall: this describes the pixels that contains container-material. these are occopied and cannot be replaced by a water-pixel.
                    void: is the vacuum or the absence of filled space (walls), and void-pixels are the only pixels that can be replaced by a water-pixel.
                    matrix: is a reimagination of the heights, where item in height-array is imagined as a stack of 1x1 boxes (pixels).
                            the height-array is split by the levels of the heights, the highest height decides how many stacks there are.
                            to visualize: 
                            height = [0,2,1,3]
                            would be a matrix that looked like this:

                            height_matrix = [
                                [0,0,0,1]
                                [0,1,0,1]
                                [0,1,1,1]
                            ]

                            NOTE; to be clear this is not how it actually works in the code. but is merly a representation to make the concept easier to understand.
            (2) The solutions uses a different approach than it normally would.
                it will iterate the list normally, by using only one pointer.
                    it would simply "symbolicly" iterate each stack and count how many voids there were. (ps, the void-counter is the counter for the whole height-array, so it is global for all lvls)
                    It would do this only after checking if the voids were legal; if a void had a wall-pixel on each side of it, or if not, then had a neighbour who had one.
                    sum(voids) that came before the first_wall_pixel in the stack, would be auto-excluded. (i did the opposite for the end of the stack). getting rid of all those trouble-makers early. 
                    if a void or a row of voids at the start or the end of the stack came before a wall pixel,   
                    after doing this for all the stacks, it would return the void-counter.

                    the loop would break whenever a stack only contained one wall-element. (the one poll that was taller than all the others)



        #* Critique:
            (1) The issue i had with it and the reason i didnt finished was; 
                I strugled with making reliable rules for when a void-pixel did not meet the wall-criteria but a neighour did.
                And it ended up not counting the middle pixels 
            (2) It's unknown wether this solution would've preformed better or worse than the pointer solution. Since it was never finished. 
            (3) The task was to make a pointer solution, so this solution is technically cheating.  
        '''
        len_lowest_points = height.count(0) #starting with zero

        print(f"bot:{min(height)} top: {max(height)}")        

        """ THIS WILL ITERATE THROUGH EACH FLOOR AND RUN THE void COUNTER (ALSO REMOVING ALL ILLEGAL voidS) """
        
        trapped_water = 0 #counts all legal void boxes (a legal void box can trap water) 
        lvl = 0


        while lvl < max(height)+1: #level as in floor / height level 
            print(f"lvl: {lvl}")
            
            """THE void COUNTER"""
            # these are all the voids found at that level    #?NOTE: all_voids is a INDEX list
            all_voids = list(i for i, x in enumerate(height) if x == lvl)
            
            # print("\n\n\n")
            print(f"lvl {lvl}")
            print(f"max(height) {max(height)}")
            print(f"all_voids {all_voids}")
            # print("\n\n\n")
            iterator=(i for i, x in enumerate(height) if x > lvl)
            # print("iterator: ", len(list(iterator)))
            print()
            iterator_copy = list(iterator).copy()
            if len(iterator_copy) <=0:
                print(len(iterator_copy))
                print("BROKEBROKEBROKE")
                break

            if height.count(lvl)<=1 and lvl==max(height):
                break
            i = 0

            first_void_index = height.index(0)
            last_void_index = height.index(0)
            while i < len_lowest_points: 
                if len(all_voids)<=1:
                    break

                #! if height[first_void_index]==0:
                #!     print(f"        void_index is ILLEGAL, popping {all_voids[i]} from all_voids ")
                if len(iterator_copy)==1:
                    first_wall_index = last_wall_index = iterator_copy[0]
                else:
                    first_wall_index, *_, last_wall_index = (i for i, x in enumerate(height) if x > lvl) #finds first and last wall
                void_index = height.index(0, i)
                print(f"    current left void, by index: {void_index}")
                print(f"    first wall, by index: {first_wall_index}")




                if void_index==0 or void_index < first_wall_index:
                    print(f"        void_index is ILLEGAL, popping {all_voids[i]} from all_voids ")
                    all_voids.pop(i)


                if void_index==len(height) or void_index > last_wall_index:
                    print(f"        void_index is ILLEGAL, popping {all_voids[i]} from all_voids ")
                    all_voids.pop(i)

                # if void_index < first_wall_index:
                #     # print(f"        {void_index} < {first_wall_index}")
                #     all_voids.pop(i)
                if void_index > last_wall_index:
                    print(f"        {void_index} < {last_wall_index}")

                print(f"    current left void, by index: {void_index}")
                print(f"    last wall, by index: {last_wall_index}")     





                i+=1
            trapped_water+=len(all_voids)
            print(f"amount of trapped water at lvl {lvl}: {len(all_voids)}, total: {trapped_water}")
            lvl += 1
        print("="*10)
        print(f"TOTAL trapped_water: {trapped_water}")
        return trapped_water
    def trap_explained(self, height: list[int]) -> int:
        ''' Using actual pointers as intended zzZ'''
        trapped_water = 0 #the total counter 
        ''' the solution will start of by working just like "Container With Most Water", 
            where it diregards the polls within it, 
            this water-volume will be reagrded as the maximum possible volume for that particular "valley"
            --> we make two max_height for each pointer: max_l,  max_r (these will cerate the max-volume)   
            '''

        l , r = 0, len(height) - 1
        max_l, max_r = 0, 0 

        #iterate the array, using the two-pointer while loops:
        while (l < r): #(left<right)
            # we store a new max-height if the height to the pointer is higher then current max.
            
            
            if height[l]<height[r]:
                if height[l]>max_l: # max height for left pointer
                    max_l=height[l]
                else:
                    #! trouble understanding why this works.
                    # explaination:
                    ''' max_l and max_r will never be reset and can only increase.
                        so any height[l] that is lower than max_l (the highest point at l) will
                        count the difference between height[l] and max_l as trapped_water. 

                        this would not work if it wasn't for the right pointer, since this will meet at the highest peak.
                        since the pointer with the lowest height moves, the one with the hightest height will stand still and not start moving again. 
                        because if it started to move, then is where all the wrongs numbers starts pouring in.  
                    '''

                    trapped_water += max_l - height[l]
                l+=1
            else:
                if height[r]>max_r: # max height for right pointer
                    max_r=height[r]
                else:
                    trapped_water += max_r - height[r]
                r-=1
        return trapped_water 
