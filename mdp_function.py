import numpy as np

reward_matrix = np.array([[-5, -5, -5], [3, 5, 0], [5, 3, 0], [1, 2, 20], [2, 1, 20]])

transition_matrix = np.array([[[1, 0, 0, 0, 0], [0.17, 0.36, 0.31, 0.13, 0.03], [0, 0.17, 0.36, 0.31, 0.16],
                              [0, 0, 0.17, 0.36, 0.47], [0, 0, 0, 0.17, 0.83]],
                              [[1, 0, 0, 0, 0], [0.06, 0.2, 0.3, 0.255, 0.185], [0, 0.06, 0.2, 0.3, 0.44],
                               [0, 0, 0.06, 0.2, 0.74], [0, 0, 0, 0.06, 0.94]],
                              [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0],
                               [0, 0.962, 0.038, 0, 0], [0, 0, 0.962, 0.038, 0]]])

N_ACTIONS = 3
N_STATES = 5
HORIZON = 6
DISCRDING_FACTOR = 0.8


def evaluate_policy(s, action, tM, rM, k):
    if k == HORIZON:
        return 0
    total = 0
    beta = DISCRDING_FACTOR

    def big_sum(a):
        result = 0
        for s_prime in range(0, N_STATES):
            result += tM[a, s, s_prime] * evaluate_policy(s_prime, a, tM, rM, k+1)
        return result

    total += rM[s, action] + beta * big_sum(action)
    return total


def find_best_action(s, tM, rM):
    evaluation_array = []
    for a in range(0, N_ACTIONS):
        evaluation_array.append(evaluate_policy(s, a, tM, rM, 0))
    return evaluation_array.index(max(evaluation_array)) + 1


def compute_policies():
    policy_array = np.zeros(N_STATES)
    for state in range(0, N_STATES):
        policy_array[state] = find_best_action(state, transition_matrix, reward_matrix)
    return policy_array

