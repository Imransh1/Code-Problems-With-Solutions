This repo contains some basic python code problems and their solutions respectively
Note - All questions are taken from codechef.com

**Q1. Problem**
According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins. What is the total amount of money that Chef will have to pay?

**Input Format**

The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers X and Y, as described in the problem statement.

**Output Format**
For each test case, output on a new line the total amount of money that Chef will have to pay.

**Explanation:**

Test case 1: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes per week is 10 coins. Hence, Chef will have to pay 10 coins in total.
Test case 2: Chef will be required to attend the MasterChef's classes for 1 week and the cost of classes per week is 15 coins. Hence, Chef will have to pay 15 coins in total.
Test case 3: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes per week is 10 coins. Hence, Chef will have to pay 20 coins in total.
Test case 4: Chef will be required to attend the MasterChef's classes for 2 weeks and the cost of classes per week is 15 coins. Hence, Chef will have to pay 30 coins in total.

**Sample Input**
4
1 10
1 15
2 10
2 15

**Expected Output**
10
15
20
30

**Q2. Problem**

There are 10 problems in a contest. You know that the score of each problem is either 1 or 100 points.Chef came to know the total score of a participant and he is wondering how many problems were actually solved by that participant. Given the total score P of the participant, determine the number of problems solved by the participant. Print −1 in case the score is invalid.

**Input Format**
First line will contain T, number of test cases. Then the test cases follow. Each test case contains of a single line containing a single integer P - denoting the number of points scored by the participant.

**Output Format**
For each testcase, output the number of problems solved by the participant or −1 if the score is invalid. 

**Explanation:**

Test Case 1: The participant has solved 4 problems out of which 3 problems are worth 1 point each while 1 problem is worth 100 points.
Test Case 2: Since participant's score is 0, he solved 0 problems.
Test Case 3: The participant has solved 6 problems out of which all the problems are worth 1 point.
Test Case 4: It is not possible to get a score of 142.
Test Case 5: The participant solved all the 10 problems and score of all the problems is 1000.

**Sample Input**
5
103
0
6
142
1000

**Expected Output**

4
0
6
-1
10

**Q3. Problem**

Six friends go on a trip and are looking for accommodation. After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. X, while a triple room costs Rs. Y. The friends can either get three double rooms or get two triple rooms. Find the minimum amount they will have to pay to accommodate all six of them.

**Input Format**

The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers X and Y - the cost of a double room and the cost of a triple room.

**Output Format**
For each testcase, output the minimum amount required to accommodate all the six friends.

**Explanation:**

Test case 1: The friends can take three double rooms and thus pay a total of Rs. 30.
Test case 2: The friends can take two triple rooms and thus pay a total of Rs. 16.
Test case 3: The friends can take three double rooms and thus pay a total of Rs. 12.

**Sample Input**

3
10 15
6 8
4 8

**Expected Output**

30
16
12

**Q4. Problem**

In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
Top 10 participants receive rupees X each.
Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
Find the total prize money over all the contestants.

**Input Format**

First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.

**Output Format**
For each test case, output the total prize money over all the contestants.

**Sample Input**

4
1000 100
1000 1000
80 1
400 30

**Expected Output**

19000
100000
890
6700

**Q5. Problem**

Alice and Bob were having an argument about which of them is taller than the other. Charlie got irritated by the argument, and decided to settle the matter once and for all.Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X  centimeters and Bob's height is Y centimeters. Help Charlie decide who is taller. It is guaranteed that X!=Y.

**Input Format**

The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two integers X and Y, as described in the problem statement.

**Output Format**

For each test case, output on a new line A if Alice is taller than Bob, else output B. The output is case insensitive, i.e, both A and a will be accepted as correct answers when Alice is taller.

**Explanation:**

Test case 1: In this case, 150<160 so Bob is taller than Alice.
Test case 2: In this case, 160>150 so Alice is taller than Bob.

**Sample Input**
2
150 160
160 150

**Expected Output**
B
A

**Q6. Problem**

Chef appeared for a placement test. There is a problem worth XX points. Chef finds out that the problem has exactly 1010 test cases. It is known that each test case is worth the same number of points. Chef passes NN test cases among them. Determine the score Chef will get.

NOTE: See sample explanation for more clarity.

**Input Format**

First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers XX and NN, the total points for the problem and the number of test cases which pass for Chef's solution.

**Output Format**
For each test case, output the points scored by Chef.

**Explanation:**
Test Case 1: The problem is worth 10 points and since there are 10 test cases, each test case is worth 1 point. Since Chef passes 3 test cases, his score will be 1*3 = 3 points.
Test Case 2: The problem is worth 100 points and since there are 10 test cases, each test case is worth 10 points. Since Chef passes all the 10 test cases, his score will be 10*10 =100 points.
Test Case 3: The problem is worth 130 points and since there are 10 test cases, each test case is worth 13 points. Since Chef passes 4 test cases, his score will be 13*4=52 points.
Test Case 4: The problem is worth 70 points and since there are 10 test cases, each test case is worth 7 points. Since Chef passes 0 test cases, his score will be 7*0 =0 points.

**Sample Input**

4
10 3
100 10
130 4
70 0

**Expected Output**

3
100
52
0
