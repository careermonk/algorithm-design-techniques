def set_cover(U, subsets):
    """Find a family of subsets that covers the universal set"""
    allElements = set(e for s in subsets for e in s)
    # Check the subsets cover the U
    if allElements != U:
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != allElements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
 
    return cover
 
def main():
    s1 = set([1, 2, 3, 4, 5, 6])
    s2 = set([5, 6, 8, 9])
    s3 = set([1, 4, 7, 10])
    s4 = set([2, 5, 7, 8, 11])
    s5 = set([3, 6, 9, 12])
    s6 = set([10, 11])
    U = set(range(1, 13))
    subsets = [s1, s2, s3, s4, s5, s6]
    cover = set_cover(U, subsets)
    print(cover)
 
if __name__ == '__main__':
    main()
