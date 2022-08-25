class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = list(sorted(intervals, key = lambda x : x[0]))
        
        for i in range(len(intervals) - 1):
            l_start, l_end = intervals[i]
            r_start, r_end = intervals[i + 1]
            
            
            if l_end > r_start:
                return False
        return True