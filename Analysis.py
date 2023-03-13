import sys
import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s" % sys.argv[0])
        print("    -N [N] for number in categorical distribution of dice")
        print
        sys.exit(1)
    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])
    else:
       #default number of sides
        N = 20
    #loading in files:
    data1 = np.loadtxt('alld6.txt')
    data2 = np.loadtxt('categorical.txt')
    
    #range of possible dice rolls for categorical file
    roll_bins1 = []
    for i in range(1,7):
        roll_bins1.append(i)
    roll_bins2 = []
    for x in range(1,N+1):
        roll_bins2.append(x)
    
    #histograms of the averages
    n, bins, patches = plt.hist(data1, bins=roll_bins1, alpha=0.7 ,rwidth=0.95, density = True, facecolor = "blue")
    plt.xlabel('Roll Average')
    plt.ylabel('Probability')
    plt.title(' all 6 sided die - ' + str(len(data1)) + ' trials')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('alld6.pdf')
    plt.clf()
    
    n, bins, patches = plt.hist(data2, bins=roll_bins2, alpha=0.7 ,rwidth=0.95, density = True, facecolor = "blue")
    plt.xlabel('Roll Average')
    plt.ylabel('Probability')
    plt.title(str(N) + ' sided distribution of die - ' + str(len(data1)) + ' trials')
    plt.grid(axis='y', alpha=0.75) 
    plt.savefig('categorical.pdf')
    
    #printing the probabilities of the 3 bins that correspond to the customer's results
    #function that finds probability of a bin
    def prob(low,high,data):
        count = 0
        for x in data:
            if x>=low and x<high:
                count += 1
        return(count/len(data))
    print('Simple Hypothesis probabilities:','3 to 4:',prob(3,4,data1),'4 to 5:',prob(4,5,data1),'5 to 6:',prob(5,6,data1))
    print('Complex Hypothesis probabilities:','3 to 4:',prob(3,4,data2),'4 to 5:',prob(4,5,data2),'5 to 6:',prob(5,6,data2))
    
              
