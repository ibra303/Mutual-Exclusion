# Mutual Exclusion 

       @Author: Habib Ibrahim
       @Date: 25/05/2023
       @issue: Mutual Exclusion  - Distributed systems
       @Version: "0.1" , "python 3.9"
       @Status: Code Optimization
       
Code can be executed at: https://colab.research.google.com/drive/1CCuv1OqWT0z2A2O-iefwLp2x0Zr2ygtb?usp=sharing

Introduction:

    The code refers to Dijkstra's first self-stabilizing algorithm for the mutual exclusion problem in a circular network.
    In a circuit N processors, N >= 3, and the possible states for each processor are [0, 1, ..., k-1] (k>=2).

Motivation:

    processor d is said to have a token if it can perform a step of his algorithm, and the goal of the algorithm is to bring
    about that from any starting state we will reach the point where there will be a single token in the system, which will
    continue and pass between all the processors.

I/O:

    input: Number of processors(N), Number of states(K), Processors values [p(0),p(1),.....,p(n-1)]
    output: Processors values after stabilizing [p(0),p(1),.....,p(n-1)], Processor index who has the only token , 
    Number of iterations needed to achieve self-stabilizing.

Notes:

    Processors are format as an array, where index 0 is Processor number 1, index 1 is Processor number 2 ..

Example:

    input: N = 8, k = 3, [0, 1, 0, 0, 0, 0, 0, 0]
    output: [2, 2, 1, 1, 1, 1, 1, 1], 'Processor in index 1 is the only one who has a token ..', 'Problem solved,
      8 iterations needed to solve the problem!'

              
       
   ![Mutual_exclusion_example_with_linked_list](https://github.com/ibra303/MutualExclusion/assets/94124916/eb38365b-9985-4016-811b-54a807cb29ec)
