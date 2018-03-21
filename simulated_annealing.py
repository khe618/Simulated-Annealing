import math
import random
def weierstrass_function(x, a, b):
    n = 0
    partial_sum = 0
    old_value = -1
    while abs(partial_sum - old_value) > 0.0000001:
        old_value = partial_sum
        partial_sum += (a**n) * math.cos( (b**n) * math.pi * x)
        n += 1
    return partial_sum

def next_state(state, temperature, m, n):
    rand = random.gauss(state, (m - n) * temperature / 10 + 0.0001)
    i = 0
    while rand <= m or rand >= n:
        rand = random.gauss(state, (m - n) * temperature / 10 + 0.0001)
        i += 1
    return rand

def acceptance_prb(value, next_value, temperature, max_temp):
    if next_value > value:
        return 1
    return (1 / (5 ** (value - next_value) ) ) * (temperature / max_temp)

def simulated_annealing(temp):
    state = random.uniform(-1, 1)
    state_value = weierstrass_function(state, 0.5, 7)
    max_temp = temp
    while temp > 0:
        candidate_state = next_state(state, temp, -1, 1)
        candidate_value = weierstrass_function(candidate_state, 0.5, 7)
        prb = acceptance_prb(state_value, candidate_value, temp, max_temp)
        print([state, candidate_state, prb, temp])
        if prb > random.random():
            state = candidate_state
            state_value = candidate_value
        temp -= 0.1
    return (state, weierstrass_function(state, 0.5, 7) )
