
import math, time

class MyRNG:
#  MyRNG class. This is the class declaration for the random number
#     generator. The constructor initializes data members "m_min" and
#     "m_max" which stores the minimum and maximum range of values in which
#     the random numbers will generate. There is another variable named "m_seed"
#     which is initialized using the method Seed(), and stores the value of the
#     current seed within the class. Using the obtained values from above, the
#     "Next()" method returns a random number to the caller using an algorithm
#     based on the Park & Miller paper.
    def __init__(self, low = 0, high = 0):
    #     The constructor initializes data members "m_min" and "m_max"
        if(low < 2):
            low = 2
        if(high < 2):
            high = 9223372036854775807
        self.m_min = low
        self.m_max = high
        self.m_seed = time.time()

    def Seed(self, seed):
    #  Seed the generator with 'seed'
        self.m_seed = seed

    def Next(self):
    #     Return the next random number using an algorithm based on the
    #        Park & Miller paper. 
        a = self.m_min
        m = self.m_max
        q = math.trunc(m / a)
        r = m % a

        hi = self.m_seed / q
        lo = self.m_seed % q
        x = (a * lo) - (r * hi)

        if(x < a):
           x += a

        self.m_seed = x
        self.m_seed %= m

        # ensure that the random number is not less
        # than the minimum number within the user specified range
        if(self.m_seed < a):
            self.m_seed += a

        return int(self.m_seed)

def test():
#  Simple test function to see if the functionality of my class
#     is there and works

    random = MyRNG(6, 10)
    random.Seed(806189064)
    per = (73*100)/100
    
    for x in range(per):
        print("%d,  " %(random.Next()))
    
    random = MyRNG(1, 5)   
    for x in range(per,100):
        print("%d,  " %(random.Next()))

if __name__ == '__main__':
    test()