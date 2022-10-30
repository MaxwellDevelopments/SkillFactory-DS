# Project 0. Guess the number

## Contents
* [1. Abstract](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Abstract) 

* [2. Our case](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Our-case)

* [3. Work stages](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Work-stages)

* [4. Result](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Result)

* [5. Summary](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Summary) 

### Abstract   
Guess the randomly generated number with minimal iteration steps.

:arrow_up: [to contents](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Contents)  


### Our case
We need to write a program that guesses the number in the minimum number of attempts.

**Competition conditions:**
- The computer "spit" randomly generated integer number in a range from 1 to 100, and we need to guess that number. By "guess" I mean "write a program that guesses a number".
- The algorithm uses information about whether the random number is greater or less than what we need.

**Quality metric**     
The results rate by the value of average number of attempts at 1000 repetitions

**What I practice**     
* Learning to write good code on python
* Learning to work with IDE.
* Learning to work with GitHub.

### Work stages 
* Development the algorithm
* Writing function in module game.py
* Writing python notebook game.ipynb for results presentation

:arrow_up: [to contents](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Contents) 


### Result:  
Function predict_number in game.py that solving problem of finding number

:arrow_up: [to contents](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Contents) 


### Summary: 
I used algorithm of halving the search area on each iteration based on information about relation beetwen numbers
So, the algorithm has complexity: O(log(n, 2))
This means that when n = end_value - start_value = 100, we have log(100) with base 2 which is 6.643856189774725.
So, in the worst case, we have 7 steps of the algorithm, which solves the problem of finding a number in a range from 1 to 100 in less than 20 steps

        
:arrow_up: [to contents](https://github.com/MaxwellDevelopments/SkillFactory-DS/tree/main/project_0/README.md#Contents) 


If you found information in this project somehow useful or interesting, than It would be very appreciated if you mark this repository and my github account with the ⭐️⭐️⭐️'s
