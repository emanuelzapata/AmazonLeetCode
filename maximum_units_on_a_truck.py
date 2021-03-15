from typing import List

class MaximumUnitsOnATruck:
    def __init__(self, boxTypes: List[List[int]], truckSize: int):
        self.boxTypes = boxTypes
        self.truckSize = truckSize        
    def calculate_units(self)->int:
        temp_list = sorted(self.boxTypes, key=lambda x: x[1], reverse=True)
        sum = 0
        for box in temp_list:
            if(self.truckSize == 0):
                break
            if(box[0] > self.truckSize):
                sum = sum + (self.truckSize*box[1])
                break
            sum = sum + (box[0] * box[1])
            self.truckSize = self.truckSize - box[0]
        return sum