from dice import Dice
from combinations import *

def main():
    d1 = Dice(6, "White")
    d2 = Dice(6, "White")
    d3 = Dice(6, "White")
    d4 = Dice(6, "White")
    d5 = Dice(6, "White")

    d1.roll()
    d2.roll()
    d3.roll()
    d4.roll()
    d5.roll()

    print(d1.get_face())
    print(d2.get_face())
    print(d3.get_face())
    print(d4.get_face())
    print(d5.get_face())
    print(Combinations.combo(d1,d2,d3,d4,d5))
 

    
    






if __name__ == '__main__':
    main()