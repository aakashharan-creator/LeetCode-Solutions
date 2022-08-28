import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[0])
        
        rooms = 1
        free_rooms = 0
        
        end_times = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start < end_times[0]:
                if free_rooms == 0:
                    rooms += 1
                else:
                    free_rooms -= 1
            else:
                while end_times and start >= end_times[0]:
                    heapq.heappop(end_times)                    
                    free_rooms += 1
                    
                free_rooms -= 1
                
            heapq.heappush(end_times, end)
        
        return rooms
                