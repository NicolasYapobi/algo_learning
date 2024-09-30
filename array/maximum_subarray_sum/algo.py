arr = [2, 3, -8, 7, -1, 2, 3]
arr2 = [-2, -4]
arr3 = [5, 4, 1, 7, 8]


def find_max(array):
    nb_max = array[0]
    for nb in array:
        if nb_max < nb:
            nb_max = nb
    return nb_max
        
#Naive approach
def max_sum(array):
    start = array[0]

    #outerloop
    for i in range(len(array)):
        max_sum = 0
        #innerloop
        for j in range(i, len(array)):
            max_sum = max_sum + arr[j]
            start = max(start, max_sum)
        
    return start

#Faster
def kadane_algorithm(array):
    start = array[0]
    max_ending = start

    for i in range(1, len(array)):
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        max_ending = max(max_ending + array[i], array[i])

        start = max(max_ending, start)
    
    return start

def main():
    print(kadane_algorithm(arr))
    print(kadane_algorithm(arr2))
    print(kadane_algorithm(arr3))

if __name__ == "__main__":
    main()