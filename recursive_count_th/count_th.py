'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # base case. When we are done checking all words
    if len(word) < 2:
        return 0
    else:
        # move towards base case
        # creat a sliding window by examining first two characters 
        if word[0:2] == "th":
            # recursive call
            # word = skip the first two characters
            return 1 + count_th(word[2:])
        else:
            # if the first 2 words is not "th", then
            # word = skip first character and check next 2 characters
            return count_th(word[1:])

# Everything below it testing what works. 

def count_th_pro(word):
    count = 0
    # new_count is same value as count above
    new_count = count
    phrase = 'th'

    if len(word) < len(phrase):
        return None
    else:
        start = 0
        #end = 

    if phrase in word:
        # new_count is same value as count above
        #new_count = count
        count = count + 1

        # split at the first occurance of the word
        remove = word.split(phrase, 1)

        # the new word to use for recursion
        new_word = remove[1]
        #new_word = word[word.find('th'):]
        #new_word = word.replace(phrase, "", 1)
        #new_word = word.remove('th')

        # use python word.count to keep track of things. 
        #if count < new_count:
        if count < word.count(phrase)  and len(new_word) >= 2:
            count_th(new_word)

    return count

def count_th_test(word):
    
    # TBC
    # 
    count = 0
    phrase = 'th'

    # with this approach, it will keep counting the same "th" repeately
    #if phrase in word:
    #    count += 1
    #    count_th(word)

    # need to count it, then drop it to avoid it from being counted again

    # this approach could work too. 
    #occur = []
    #if phrase in word:
    #    occur.append(phrase)

    if phrase in word:
        # increase the count
        count += 1
        # drop the phrase from the word to prevent it from being counted again
        word = word.replace(phrase, "")
               # if count increases, then recurse, if not, then terminate
        # keep track of the count. If new_count = count, then new_count did not increase. nothing more to count
        if new_count > count:
            count_th(word)
        
    else:
        return count

    # recursion. repeat the proces
    # need a base case so recursion doesn't run forever.
    #count_th(word)

    return count


# Another approach

def count_th_2(word):
    return word.count('th')