# Yatzy (Python refactoring)
Refactoring excercise based on [Emily Banche](https://github.com/emilybache)'s [*Yatzy Refactoring Kata*](https://github.com/emilybache/Yatzy-Refactoring-Kata/tree/main/python) \
&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; <sub>(Python's version)</sub> 

> " Ward Cunningham explained it like this:  
> &emsp; Whenever you have to figure out what code is doing, **you are building some understanding in your head**. Once you've built it, **you should move that understanding into the code so nobody has to build it from scratch** in their head again."  &emsp;&emsp;&emsp;&emsp;<sub>*Martin Fowler*, in [*Workflows of Refactoring*](https://martinfowler.com/articles/workflowsOfRefactoring/)</sub>

> "Don't refactor unless you think you will recoup your investment later by quicker work"
> \
> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<sub>*Jonathan Rasmusson*, in [*The Agile Samurai: How Agile Masters Deliver Great Software*](https://www.amazon.com/Agile-Samurai-Software-Pragmatic-Programmers/dp/1934356581)</sub>



## Refactoring commits logbook
Cronological order of refactoring commits: 

- Commit [*befe38a*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/befe38a43f2a4f625bf8e1dd86005c81fb401e40):
    - Moved `class Yatzy` `def __init__` to the top of the class. 

- Commit [*7b37cab*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/7b37cabfb088fd5e3f3d26d91537f8928025cad8):
    - Changed how `self.dice` is defined, from a list in which the arguments given to the `__init__` function are inserted into a positional index, to a list that it's created from the value of arguments itself; yatzy always expects 5 values that range from 1 to 6, which allows this level of simplicity.

- Commit [*f27e12f*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/f27e12f7f294cc1481cbaf3c850b51b5bbc1991c)
    - Morphed `Yatzy.chance` into a class instance dependant method that takes the `self.dice` argument to operate.
    - Modified the operations from a iterative sum of each given argument into a total variable to a sum of all objects stored inside `self.dice`, which is directly returned.

- Commit [*05bbd99*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/05bbd992f99c04f79440f5658842c87b2fcd906b)
    - Changed the test linked to `Yatzy.chance`: it now requires the arguments for the test to be given to the class instead of to the function itself. 

- Commit [*30aecd7*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/30aecd766a6ec8e3bde1eb1ad97b6ef762a5148c)
    - Each and every *count occurances of x number* funcion has been changed following the spirit of `Yatzy.chance`: it now returns the sum of a list comprehension that it's based on looping through `self.dice` appending only the desired value (which is held by the constant `FILTER`) to the list to be summed. This all is directly returned.
    - Some of the functions remained static: now they're also class instance dependant, as they all reference `self.dice` in their execution.

- Commit [*18b0c01*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/18b0c01f51def9b7c3307ea9ff56ca7137396e78):
    - Accomodated the tests pertaining to the now changed static functions: their arguments are now given directly to `class Yatzy` instead of directly to the function.

- Commit [*3fff994*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/3fff994d67ad1887ff6c1d4c67226e525278d98e):
    - Given that the function `Yatzy.yatzy` only checks if all dice have the same number, it could be simplified into an if/else statement that checks the length of the set of `self.dice`: if the set length is 1, it means all the die's values are the same. If not, more than one value is present, therefore the maximum score of 50 is not given.
    - Again, the function used to be a static method. Now it's not.

- Commit [*dc667c5*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/dc667c50014ce9c1a51538d7288103fcc318e468)
    - Another test change to a function that is now class instance based, this time to the maximum score test.

- Commit [*69e17a4*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/69e17a4435ce0d8558d6c4e0e27b45d7084ca4fa):
    - The commit changes all `x_of_a_kind` functions. They recieved the self argument (despite being static funtions) and each dice separatedly: now they only recieve self and are tied to the instance of a class. Additionaly, their functionalities have been simplified and standarized to the sum of a list comprehension (which is sliced after the first object inside of it) that takes an inversely ordered set with the values inside of `self.dice` and checks how many dice have given that value in the current roll. If the die are equal or more to the `X_OF_A_KIND` constant value, they're considered for the sum.

- Commit [*6b569e5*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/6b569e575574232649adfe2a75e1394894e2961b):
    - Given that now every `x_of_a_kind` function recieves their arguments through `class Yatzy`, the tests needed updating.

- Commit [*325d13c*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/325d13c02cc940c1a112d15424efef5b5bb71b96):
    - Now `two_pair` takes only self argument. It creates a list variable that holds the same list comprehension than `one_pair`, but it slices it at [:2] instead of [:1]. Then, the `return` statement checks the length of the list: if it's 2, it'll return the sum of the list; if it's 1 or 0 (meaning that `self.dice` only held 1 pair or 0), it'll return 0.  

- Commit [*0a1de2c*](https://github.com/MMSS99/Yatzy-Refactor-py/commit/0a1de2cff26df794e36997dd53a4f55d05b7f927): 
    - Again, now `two_pair` is instance dependant so the arguments given by the test are now being sent to the class.




