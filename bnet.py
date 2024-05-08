#!/usr/bin/env python3
import sys

class BayesianNetwork:
    def __init__(self):
        # Base probabilities
        self.P_B = 0.001
        self.P_E = 0.002
        # Conditional probabilities
        self.P_A_given_BE = {(True, True): 0.95, (True, False): 0.94, (False, True): 0.29, (False, False): 0.001}
        self.P_J_given_A = {True: 0.9, False: 0.05}
        self.P_M_given_A = {True: 0.7, False: 0.01}

    def compute_probability(self, values, conditions=None):
        total_prob = 0
        # Generate all combinations of states for variables that might be None
        for b in [True, False] if values.get('B') is None else [values.get('B')]:
            for e in [True, False] if values.get('E') is None else [values.get('E')]:
                for a in [True, False] if values.get('A') is None else [values.get('A')]:
                    for j in [True, False] if values.get('J') is None else [values.get('J')]:
                        for m in [True, False] if values.get('M') is None else [values.get('M')]:
                            if conditions and not all(conditions.get(k, v) == v for k, v in zip('BEAJM', (b, e, a, j, m))):
                                continue  # skip configurations that don't match the condition
                            prob = (self.P_B if b else 1 - self.P_B) * \
                                   (self.P_E if e else 1 - self.P_E) * \
                                   (self.P_A_given_BE[(b, e)] if a else 1 - self.P_A_given_BE[(b, e)]) * \
                                   (self.P_J_given_A[a] if j else 1 - self.P_J_given_A[a]) * \
                                   (self.P_M_given_A[a] if m else 1 - self.P_M_given_A[a])
                            total_prob += prob
        return total_prob
    
    def parse_and_compute(self, args):
        query, given = {}, {}
        parsing_given = False
        for arg in args:
            if arg == 'given':
                parsing_given = True
                continue
            var, state = arg[0], arg[1] == 't'
            (given if parsing_given else query)[var] = state
    
        joint_prob = self.compute_probability(query, given if given else None)
        given_prob = self.compute_probability(given) if given else 1
        return joint_prob / given_prob if given_prob != 0 else 0

if __name__ == "__main__":
    network = BayesianNetwork()
    result = network.parse_and_compute(sys.argv[1:])
    print(f"Probability = {result:.10f}")
