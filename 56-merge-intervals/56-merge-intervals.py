class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key = lambda x : x[0]))
        
        new_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            l_start, l_end = new_intervals[-1]
            r_start, r_end = intervals[i]
            
            if l_end < r_start:
                new_intervals.append([r_start, r_end])
            else:
                new_intervals[-1][1] = max(r_end, l_end)
                
        return new_intervals