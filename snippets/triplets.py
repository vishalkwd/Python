# Python program to find all triplets with zero sum using hashing
def findTriplets(arr):

    # Set to handle duplicates
    resSet = set()
    n = len(arr)
    mp = {}

    # Store sum of all the pairs with their indices
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s not in mp:
                mp[s] = []
            mp[s].append((i, j))

    for i in range(n):

        # Find remaining value to get zero sum
        rem = -arr[i]
        if rem in mp:
            for p in mp[rem]:
                
                # Ensure no two indices are the same in the triplet
                if p[0] != i and p[1] != i:
                    curr = sorted([i, p[0], p[1]])
                    resSet.add(tuple(curr))

    return [list(triplet) for triplet in resSet]

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    res = findTriplets(arr)
    for triplet in res:
        print(triplet[0], triplet[1], triplet[2])
