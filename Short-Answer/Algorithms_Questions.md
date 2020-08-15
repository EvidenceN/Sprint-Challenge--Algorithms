# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 # O(1)
    while (a < n * n * n): # O(n)
      a = a + n * n # O(n)
```
O(n) because the output will be equal to the number of inputs

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n^2) because the while loop is going to run for every input "i" in the for loop
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

O(n Log n) because the if statment is constant. It doens't matter what the input for bunnies is, the operation remains the same. Then recursion is Logatherimc operation.The function repeats itself and adds 2 to the operation each time. 
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# number of buildings = n
# eggs = e
# if eggs fall of floor f = broken
# if floor >= f = broken else not_broken
# number of eggs + broken eggs = minimized

# if egg is broken: print what floor that egg fell down from. 
# Then, throw egg from floor below floor f and see if it breaks. If it breaks, then repeat the process. If it doesn't break, THAT is the minimum floor to minimize broken eggs

# def egg(floor number=7):
#    # if f == 7  and egg_broken ==True:
#    # f -= 1
#    # return egg(f)
#      else:
#          #print(f) print the floor where the egg doesn't break