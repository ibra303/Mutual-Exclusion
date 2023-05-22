# Mutual Exclusion - Dijkstra's first self-stabilizing algorithm for the mutual Exclusion problem in a circular network.

Introduction:
                mutual exclusion is a property of concurrency control, which is instituted for the purpose of preventing race conditions. 
                It is the requirement that one thread of execution never enters a critical section while a concurrent thread of execution is already accessing said critical                   section, which refers to an interval of time during which a thread of execution accesses a shared resource or shared memory.

        ->      The shared resource is a data object, which two or more concurrent threads are trying to modify (where two concurrent read operations are permitted but, 
                no two concurrent write operations or one read and one write are permitted, since it leads to data inconsistency).
                Mutual exclusion algorithms ensure that if a process is already performing write operation on a data object [critical section] no other process/thread is                       allowed to access/modify the same object until the first process has finished writing upon the data object [critical section] and released the object for                       other processes to read and write upon.

        ->      The requirement of mutual exclusion was first identified and solved by Edsger W. Dijkstra in his seminal 1965 paper "Solution of a problem in concurrent                       programming control", which is credited as the first topic in the study of concurrent algorithms!
              
Motivation:              
              The code refers to Dijkstra's first self-stabilizing algorithm for the mutual exclusion problem in a circular network.
              In a circuit N processors, N >= 3, and the possible states for each processor are [0, 1, ..., k-1] (k>=2).
              processor d is said to have a token if it can perform a step of his algorithm, and the goal of the algorithm is to bring about that from any
              starting state we will reach the point where there will be a single token in the system, which will continue and pass between all the processors.
              
              ![Mutual_exclusion_example_with_linked_list](https://github.com/ibra303/MutualExclusion/assets/94124916/eb38365b-9985-4016-811b-54a807cb29ec)
