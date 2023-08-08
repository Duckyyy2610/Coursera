import itertools

def generate_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]

while True:
    txt = input("Enter a string: ")
    if len(txt) < 1:
        break

    permutations = generate_permutations(txt)
    hash_values = {}

    for perm in permutations:
        hv = 0
        pos = 0
        for let in perm:
            pos = (pos % 3) + 1
            hv = (hv + (pos * ord(let))) % 1000000
            print(let, pos, ord(let), hv)
        
        if hv in hash_values:
            print(f"Found a pair with the same hv: {perm} and {hash_values[hv]}")
        else:
            hash_values[hv] = perm

    print("All permutations and their hash values:\n", hash_values)
