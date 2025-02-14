class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # We have to merge the new intervel such that it eats up the coliding intervals considering start and end time

        res = []

        for i in range(len(intervals)):
            # First edge case or case where the new interval is les than the upcoming intervals
            # It simply adds the interval to the res and returns the further arrar and res array which has older intervals as well
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # 2nd case where the interval is bigger than the current interval to adding the current interval and thinking further for more intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case where we are making the new Interval Bigger by merging the current interval to the newInterval and then comparing to further
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        
        # Adding the new interval at the end considering case 2 and 3 where its not added yet
        res.append(newInterval)

        return res