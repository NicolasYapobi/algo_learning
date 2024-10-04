array = [3, 0, 1, 0, 4, 0, 2]


def trap(array):
    max_nb = max(array)
    first_boundaries = array[0]
    water = 0

    for i in range(0, len(array)):
        if array[i] == 0:
            water += array[i - 1]
            print(array[i - 1])
    return water

# brute force

def trap_water(array):
    res = 0

    for i in range(1, len(array) - 1): #[0, 1, 0, 4, 0, 2]
        print("loop: ", i)
        for j in range(i): # i = 1 j = 0
            left = max(left, array[j]) # array[j] = 3
        
        right = array[i] # array[i] = 0
        for j in range(i + 1, len(array)): #[1, 0, 4, 0, 2]
            right = max(right, array[j])
        
        res += (min(left, right) - array[i])

    return res

def main():
    print(trap_water(array))


if __name__ == "__main__":
    main()