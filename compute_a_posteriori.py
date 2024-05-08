#!/usr/bin/env python3

import os
import sys

def posterior_probability(sequence):
    hypothesis = [0.1, 0.2, 0.4, 0.2, 0.1]
    cherryQuantity = [1.00, 0.75, 0.50, 0.25, 0.00]
    limeQuantity = [0.00, 0.25, 0.50, 0.75, 1.00]

    # Precompute the upper case conversion to handle case insensitivity efficiently
    sequence = sequence.upper()

    for i, candy in enumerate(sequence):
        if candy == 'C':
            Q = cherryQuantity
        elif candy == 'L':
            Q = limeQuantity
        else:
            continue  # Skip invalid characters

        # Update hypotheses probabilities
        hypothesis = [Q[prob] * hypothesis[prob] for prob in range(len(hypothesis))]
        total_hypothesis = sum(hypothesis)

        # Normalize hypotheses probabilities
        dividedHypothesis = [h / total_hypothesis for h in hypothesis]

        print(f"After Observation {i+1} = {candy}:", end="\n\n")

        # Calculate probabilities for cherry and lime based on current hypotheses
        cherryProbability = sum(cherryQuantity[j] * dividedHypothesis[j] for j in range(len(dividedHypothesis)))
        limeProbability = sum(limeQuantity[j] * dividedHypothesis[j] for j in range(len(dividedHypothesis)))

        for prob, currentPosteriorProbability in enumerate(dividedHypothesis):
            print(f"P(h{prob+1} | Q) = {currentPosteriorProbability}")

        print(end="\n")
        print(f"Probability that the next candy we pick will be C, given Q: {cherryProbability}")
        print(f"Probability that the next candy we pick will be L, given Q: {limeProbability}", end="\n\n")

def main(sequence):
    
    seqLength =  len(sequence)
    for i in range(1,1000):
        fileName = f'result{i}.txt'
        fileNameRes = f'result.txt'

        if not os.path.exists(fileNameRes):
            with open(fileNameRes, 'w') as f:
                sys.stdout = f
                print("Observation sequence Q", sequence)
                print("Length of Q:", seqLength)
                print("\n")
                posterior_probability(sequence)
                sys.stdout

            f.close()
            break

        elif not os.path.exists(fileName):
            with open(fileName, 'w') as f:
                sys.stdout = f
                print("Observation sequence Q", sequence)
                print("Length of Q:", seqLength)
                print("\n")
                posterior_probability(sequence)
                sys.stdout

            f.close()
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide a sequence")
        sys.exit(1)

    sequence = sys.argv[1].upper()
    
    if set(sequence) <= {'C', 'L'}:
        main(sequence)
    else:
        print("Error: Please provide a sequence containing only letters C and L")
