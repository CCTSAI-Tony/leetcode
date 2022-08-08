'''
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. 
Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. 
These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. 
You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.
We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. 
The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, 
each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

Example 1:

Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
 

Constraints:

3 * n == water.length
1 <= n <= 20
water[i] is either 'H' or 'O'.
There will be exactly 2 * n 'H' in water.
There will be exactly n 'O' in water.
'''

# This solution uses Semaphore and Barrier. It is simple to understand, and performs well.

# Semantics
# a Semaphore -- trying to acquire it, is possible if there are tokens left. Otherwise the thread that tried is asked to wait until a different thread returns the tokens it was using.
# a Barrier -- if a thread reaches it, it can cross it, only if a predefined number of other threads have also arrived.
# Logic
# The solution creates 1 Semaphore for Hydrogen, and allows 2 threads to aquire it concurrently. Likewise, we create one for Oxygen, but this one only allows 1 thread.

# To ensure the molecule is generated at once, we use a barrier, which can only be crossed when 3 atoms have gathered.

# After each function completes, we release the token on the Semaphore.

# Tip
# As others have explained, we can use Python context managers, which makes the code easier to follow.

## WITH context (with)
sem = Semaphore(3)

with sem:
    # code...
is equivalent to

## WITHOUT context
sem = Semaphore(3)

sem.acquire()
try:
    # code...
finally:
    sem.release()

# 刷題用這個
# 思路: thread Semaphore() and Barrier()
# a Semaphore -- trying to acquire it, is possible if there are tokens left. Otherwise the thread that tried is asked to wait until a different thread returns the tokens it was using.
# a Barrier -- if a thread reaches it, it can cross it, only if a predefined number of other threads have also arrived.
from threading import Semaphore
from threading import Barrier
class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        with self.sem_h:
            self.bar_assembling.wait()

            releaseHydrogen()



    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        with self.sem_o:
            self.bar_assembling.wait()

            releaseOxygen()

