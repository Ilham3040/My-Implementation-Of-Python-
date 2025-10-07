def contains_substring(s: str, pattern: str) -> bool:
    m, n = len(pattern), len(s)
    if m == 0:  # empty pattern always matches
        return True
    if m > n:
        return False

    for i in range(n - m + 1):  # slide window of length m
        print(s[i:i+m])
    #     if s[i:i+m] == pattern:
    #         return True
    # return False

# Tests
tests = ["ab", "cab", "baba", "aabb", "abab", "bbb"]
for t in tests:
    print(f"{t!r:5} -> {contains_substring(t, 'ab')}")


"""

cab -> 3
ab -> 2

3-2+1 = 2

range return [0,1] because python range(2) will stop before since it start from 0

s[0:0+2]

ca

s[1:1+2]

ab


"""