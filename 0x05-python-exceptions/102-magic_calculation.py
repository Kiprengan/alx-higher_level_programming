#!/usr/bin/python3
def magic_calculation(a, b):
    outcome = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            else:
                outcome += a ** b / m
        except Exception:
            outcome = b + a
            break
    return (outcome)
