def nfa_ends_with_ab(s: str) -> bool:
    # NFA states: each is (pos_in_input, stage)
    # stage 0=any char, stage1=seen 'a', stage2=accept
    states = {(0,0)}
    for i,ch in enumerate(s,1):
        next_states = set()
        for _,stage in states:
            if stage == 0:
                # Always stay in stage0
                next_states.add((i,0))
                if ch == 'a':
                    next_states.add((i,1))
            elif stage == 1:
                if ch == 'b':
                    next_states.add((i,2))
                elif ch == 'a':
                    next_states.add((i,1))
        states = next_states
    return any(stage == 2 for _,stage in states)
