class Submarine:
    aim = 0
    horizontal = 0
    depth = 0

    def moveForward(self, units):
        self.horizontal += units
    
    def moveDown(self, units):
        self.depth += units
    
    def moveUp(self, units):
        self.depth -= units
    
    def increaseAim(self, units):
        self.aim += units

    def decreaseAim(self, units):
        self.aim -= units
        

def parse_move(s):
    split = s.split()
    return (split[0], int(split[1]))
