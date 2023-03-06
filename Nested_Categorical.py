import sys
import numpy as np

sys.path.append(".")
from Random import Random
random = Random()

# main function
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-Nsides number] [-Ndice number] [-Ntrials number]" % sys.argv[0])
        print ("Outputs file to 'output.txt' ")
        sys.exit(1)
    # default seed
    seed = 5555
    
    #standard 6-sided dice for simple hypothesis
    n_sides = 6
    #default categorical distribution of dice
    n_categorical = 20
    #default number of dice rolled
    n_dice = 10
    #default number of trials to create the distribution
    n_trials = 1000
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    #read the other parameters (if there)
    if '-Nsides' in sys.argv:
        p = sys.argv.index('-Nsides')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            n_sides = Ns            
    if '-Ndice' in sys.argv:
        p = sys.argv.index('-Ndice')
        Nd = int(sys.argv[p+1])
        if Nd > 0:
            n_dice = Nd
    if '-Ntrials' in sys.argv:
        p = sys.argv.index('-Ntrials')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            n_trials = Nt
   
    #loop that writes results to output file
    output1 = open('alld6.txt','w')
    output2 = open('categorical.txt','w')
    for x in range(n_trials):
        #empty arrays to roll outcomes
        rolls1 = []
        rolls2 = []
        #random dice
        n = random.categorical(n_categorical)
        for i in range(n_dice):
            rolls1.append(random.categorical(n_sides))
            rolls2.append(random.categorical(n))
        avg1 = np.mean(np.asarray(rolls1))
        avg2 = np.mean(np.asarray(rolls2))
        output1.write(str(avg1)+" \n")
        output2.write(str(avg2)+" \n")