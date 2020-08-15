#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the output will be equal to the number of inputs


b)O(n^2) because the while loop is going to run for every input "i" in the for loop


c) O(n Log n) because the if statment is constant. It doens't matter what the input for bunnies is, the operation remains the same. Then recursion is Logatherimc operation.The function repeats itself and adds 2 to the operation each time. 

## Exercise II
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

