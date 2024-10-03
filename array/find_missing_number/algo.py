array = [1, 2, 4, 6, 3, 7, 8]
N = 8


def find_missing(array, n):
    hash = [0] * (n + 1)

    for num in array:
        hash[num] += 1
    for i in range(1, n):
        if hash[i] == 0:
            return i

def main():
    print(find_missing(array, N))

if __name__ == "__main__":
    main()