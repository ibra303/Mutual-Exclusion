"""
       @Author: Habib Ibrahim
       @Date: 25/05/2023
       @issue: Mutual Exclusion  - Distributed systems
       @Version: "0.1"
       @Status: Code Optimization

Introduction:
    The code refers to Dijkstra's first self-stabilizing algorithm for the mutual exclusion problem in a circular network.
    In a circuit N processors, N >= 3, and the possible states for each processor are [0, 1, ..., k-1] (k>=2).

Motivation:
    processor d is said to have a token if it can perform a step of his algorithm, and the goal of the algorithm is to bring about that from any
    starting state we will reach the point where there will be a single token in the system, which will continue and pass between all the processors.

I/O:
    input: Number of processors(N), Number of states(K), Processors values [p(0),p(1),.....,p(n-1)]
    output: Processors values after stabilizing [p(0),p(1),.....,p(n-1)], Processor index who has the only token , Number of iterations needed to achieve self-stabilizing

Notes:
    Processors are format as an array, where index 0 is Processor number 1, index 1 is Processor number 2 ..

Example:
    input: N = 8, k = 3, [0, 1, 0, 0, 0, 0, 0, 0]
    output: [2, 2, 1, 1, 1, 1, 1, 1], 'Processor in index 1 is the only one who has a token ..', 'Problem solved, 8 iterations needed to solve the problem!'

"""


# input: ()
# output: Number of processors(N), Number of states(K), Processors values [p(0),p(1),.....,p(n-1)]
def ME_inputs():
    processorsNumber = 0
    statesNumber = 0
    while processorsNumber < 3:
        processorsNumber = int(input("Enter number of processors: "))
    processorsValues = [0] * processorsNumber
    while statesNumber < 2:
        statesNumber = int(input("Enter number of states: "))
    for i in range(processorsNumber):
        processorsValues[i] = int(input("Enter value of processor number " + str(i) + ": "))
        while processorsValues[i] >= statesNumber or processorsValues[i] < 0:
            processorsValues[i] = int(input("Wrong value! processors values can be 0 - " + str(statesNumber - 1) +
                                            " \n Enter new value of processor number" + str(i) + ": "))
    return processorsNumber, statesNumber, processorsValues


# input: (Number of processors(N), Processors values [p(0),p(1),.....,p(n-1)])
# output: which processors has a token, total tokens (in current state)
def calculate_tokens(processorsNumber, processorsValues):
    tokensNum = 0
    haveToken = [0] * processorsNumber
    for i in range(processorsNumber):
        if i == 0 and processorsValues[i] == processorsValues[processorsNumber - 1]:
            haveToken[i] = 1
            tokensNum += 1
        elif i != 0 and processorsValues[i] != processorsValues[i - 1]:
            haveToken[i] = 1
            tokensNum += 1
    return haveToken, tokensNum


# input: (Number of processors(N), Processors values [p(0),p(1),.....,p(n-1)], which processors has a token, total tokens, Number of states)
# output: Processors values after each one used his token [p(0),p(1),.....,p(n-1)]
def make_stable(processorsNum, processorsValues, haveToken, tokensNum, statesNum):
    for i in range(processorsNum - 1, -1, -1):
        if i == 0 and haveToken[i] == 1:
            processorsValues[i] = (processorsValues[i] + 1) % statesNum
        elif i != 0 and haveToken[i] == 1:
            processorsValues[i] = processorsValues[i - 1]
        # Update tokensNum if a token is consumed
        if haveToken[i] == 1:
            tokensNum -= 1
    return processorsValues


# input: (Number of processors(N), Processors values [p(0),p(1),.....,p(n-1)])
# output: print algorithm outputs
def print_result(processorsNum, processorsValues):
    print("\nprocessors values = " + str(processorsValues))
    for i in range(processorsNum):
        if have_token[i]:
            print("Processor in index " + str(i) + " is the only one who has a token ..")
    print("Problem solved, " + str(number_of_iterations) + " iterations needed to solve the problem!\n")


# Dijkstra's first self-stabilizing Algorithm
if __name__ == '__main__':
    number_of_iterations = 0
    k = 0
    processors_num, states_num, processors_values = ME_inputs()
    have_token, tokens = calculate_tokens(processors_num, processors_values)
    while tokens != 1:
        number_of_iterations += 1
        processors_values = make_stable(processors_num, processors_values, have_token, tokens, states_num)
        have_token, tokens = calculate_tokens(processors_num, processors_values)
        if number_of_iterations > 10000:
            print("Cant solve this state!")
            exit()
    print_result(processors_num, processors_values)
