# NashVentures
Algorithm for Random number Generation which is 73% biased to higher number


Step 1- Take 2 inputs from user in which range you want a random no and store it in low and high variables

step 2 - take input from user ,n= no of times you want to execute this program

step 3- mid=(low+high)/2

step 4- make next() function which will generate a random no

step 5-in next() function put code of random no of Park & Miller paper
       ..get time from time module in python
        a = low
        m = high
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

step 6-in main function find out 73% of n and put this in variable
       i.e.  per=(73/100)*n;

step 7- use one for loop for range(1,per) in which call next function with range(low,mid)
      i.e.per = (73*100)/100
    
    for x in range(per):
        print("%d,  " %(random.Next()))
      
step-8-use 2nd for loop for range(per,n) in which call next function with range(mid+1,high)    
    for x in range(per):
        print("%d,  " %(random.Next()))
        
 step- 9 exit.
 
 
 
 
 
 concept-- 
 
 first we will take time seeds from time module in python so that we can use that time for generating random number with some calculations, then we will take a range from user in which he wants to get a random no then we will find mid of range.
 as the question says it should be 73% biased so we will ask user to input no of times he wants to execute this program and we will find out the 73% of that no.
  ex.- if user wants to execute it 1000 times then 73% of 1000 will be 730 so 730 times no would be higher then mid and 270 times no would be lower then mid.
  
   then we will use 2 for loops 
   1 for range(1,73% of n) and 2 loop for range(73% of n ,n)
    in 2nd loop we will call next function with  range(1,mid)
    in 1st loop we will call next function with range(mid+1,high)
    we will print both lists
 
 
 
 
 
 
 
 
 
 
 
 
 
 
