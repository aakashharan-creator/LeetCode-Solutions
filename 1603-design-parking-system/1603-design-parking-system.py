class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.num_big = 0
        self.num_med = 0
        self.num_sm = 0
        
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.num_big < self.big:
                self.num_big += 1
                return True
        elif carType == 2: 
            if self.num_med < self.medium:
                self.num_med += 1
                return True
        else:
            if self.num_sm < self.small:
                self.num_sm += 1
                return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)