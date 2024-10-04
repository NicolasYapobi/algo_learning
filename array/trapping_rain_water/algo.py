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

def main():
    print(trap(array))


if __name__ == "__main__":
    main()