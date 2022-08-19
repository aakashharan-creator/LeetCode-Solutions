class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_by_value = list(reversed(sorted(boxTypes, key = lambda x : x[1])))

        curr_boxes = 0
        curr_units = 0
        
        for units, value in box_by_value:
            remaining_space = truckSize - curr_boxes
            
            if remaining_space == 0:
                break
            
            boxes_to_add = min(units, remaining_space)
            curr_boxes += boxes_to_add
            
            curr_units += value * boxes_to_add
            
        return curr_units