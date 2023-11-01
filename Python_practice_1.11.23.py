### Python Practice 31/10/23
## Content
# Class methods
#======================================================================#
class Stat_line:
    def __init__(self, pts, rbd, ast, stl, blk):
        self._pts = int(pts)
        self._rbd = int(rbd)
        self._ast = int(ast)
        self._stl = int(stl)
        self._blk = int(blk)        
    def trip_doub(self):
        if self._pts >= 10 and self._rbd >= 10 and self._ast >= 10:
            return "Triple double!"
        elif self.pts <10 and self._rbd >= 10 and self.ast >= 10:
            print("Not enough points")
        elif self.pts >= 10 and self._rbd < 10 and self.ast >= 10:
            print("Not enough rebounds!")
        elif self.pts >= 10 + self._rbd >= 10 + self.ast < 10:
            print("Not enough assists")
        else:
            print("Too bad")
    
    # Getter - pts
    @property
    def pts(self):
        return self.pts

    # Setter - pts
    @pts.setter
    def pts(self, pts):
        if isinstance(pts, str):
            raise ValueError("The points value you have added is an invalid data type") 
        self._pts = pts

def main():
    player = get_stats()
    print(player.trip_doub())



def get_stats():
    pts = input("How many pts did they score? ")
    rbd = input("How many rebounds did they get? ")
    ast = input("How many assists did they get? ")
    blk = input("How many blocks did they get? ")
    stl = input("How many steals did they get? ")
    return Stat_line(pts, rbd, ast, blk, stl)

if __name__ == "__main__":
    main()


