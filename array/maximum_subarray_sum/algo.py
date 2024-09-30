arr = {2, 3, -8, 7, -1, 2, 3}
arr2 = {-2, -4}
arr3 = {5, 4, 1, 7, 8}


def find_max(array):
    nb_max = list(array)[0]
    for nb in array:
        if nb_max < nb:
            nb_max = nb
    return nb_max
        


def main():
    print(find_max(arr))
    print(find_max(arr2))
    print(find_max(arr3))

if __name__ == "__main__":
    main()