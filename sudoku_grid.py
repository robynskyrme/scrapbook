

class Grid:

    cells = [0]

    def __init__(self,size):
        self.size = size
        for c in range (size ** 2):
            self.cells.append(c + 1)

    def lookup(self,cell,direction):
        if direction == "N":
            ans = cell - self.size
        if direction == "S":
            ans = cell + self.size
        if direction == "W":
            ans = cell - 1
        if direction == "E":
            ans = cell + 1
        ans == ans % self.size ** 2
        return ans

if __name__ == "__main__":
    g = Grid(9)

    print(g.lookup(10,"W"))