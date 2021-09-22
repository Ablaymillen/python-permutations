def permutation(list):
    # If only one element return it 
    # base case of our reccursion 
    if len(list) == 1:
        return [list]
    # List that will store our result
    res = []
    for i in range(len(list)):
        #Current item in the list
        curr = list[i]
        #All the other items except current
        not_curr = list[:i] + list[i+1:]
        # Generating all permutation with current item and remaining ones
        for j in permutation(not_curr):
            res.append([curr] + j)            
    return res

def permutate_list(list):
    for item in permutation(list):
        print(item)
