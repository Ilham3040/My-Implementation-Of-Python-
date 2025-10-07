def ends_with_ab_dfa(s: str) -> bool:
    # States: 0=start/other, 1=seen 'a', 2=seen 'ab' (accept)
    state = 0
    for ch in s:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            # Once we reach accept, a new 'a' might start a new 'ab'
            state = 1 if ch == 'a' else 0
    return state == 2

# Tests
tests = ["ab", "cab", "baba", "aabb", "abab", "bbb"]
for t in tests:
    print(f"{t!r:5} -> {ends_with_ab_dfa(t)}")
