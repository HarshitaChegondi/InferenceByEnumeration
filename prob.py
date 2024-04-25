import sys
import os
def posterior_probability(sequence):

    hypothesis = [0.1, 0.2, 0.4, 0.2, 0.1]

    cherryQuantity = [1.00, 0.75, 0.50, 0.25, 0.00]
    limeQuantity = [0.00, 0.25, 0.50, 0.75, 1.00]

    for i, candy in enumerate(sequence):
        if candy == 'C' or candy == 'c':
           Q = cherryQuantity
        elif candy == 'L' or candy == 'l':
           Q = limeQuantity

        for prob in range(len(hypothesis)):
            hypothesis[prob]=Q[prob]*hypothesis[prob]


        sumofHypothesis = 0
        for prob in range(len(hypothesis)):
            sumofHypothesis += hypothesis[prob]

        dividedHypothesis = []
        for prob in range(len(hypothesis)):
            dividedHypothesis.append(hypothesis[prob]/sumofHypothesis)



        print(f"After Observation {i+1} = {candy}:")
        cherryProbability = 0
        limeProbability = 0

        for prob in range(len(dividedHypothesis)):
            cherryProbability += cherryQuantity[prob] * dividedHypothesis[prob]
            limeProbability += limeQuantity[prob] * dividedHypothesis[prob]

        for prob, currentPosteriorProbability in enumerate(dividedHypothesis):
            print(f"P(h{prob+1} | Q)= {currentPosteriorProbability:}")
        print(f"Probability that the next candy we pick will be C, given Q:{cherryProbability:}")
        print(f"Probability that the next candy we pick will be L, given Q:{limeProbability:}")
        print("\n")

    

def main(sequence):
    
    seqLength =  len(sequence)
    for i in range(1,1000):
        fileName = f'result{i}'
        if not os.path.exists(fileName):
            with open(fileName, 'w') as f:
                sys.stdout = f
                print("Given observation:", sequence)
                print("Length of Sequence:", seqLength)
                print("observation sequence: ", seqLength)
                posterior_probability(sequence)
            sys.stdout

            f.close()
            break
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please give a sequence")
        sys.exit(1)

    sequence = sys.argv[1]
    
    if 'C' in sequence or 'L' in sequence:
        main(sequence)
    elif 'c' in sequence and 'l' in sequence:
        main(sequence)
    else:
        print("Error: give only letters C nad L")
