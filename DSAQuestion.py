def generate_permutation(num):
    num_str=str(num)
    perm=permutations(num_str)
    perm_list=[".join(p) for p in perm"]
    return perm_list
