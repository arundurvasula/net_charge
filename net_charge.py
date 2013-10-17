#Run with: python net_charge.py <pH> <sequence>
# where pH is the pH the protein is at
from sys import argv

pH = float(argv[1])
seq = argv[2]

charge = 0

amino_acids = { "A":0,
                "R":12.48,
                "N":0,
                "D":3.65,
                "C":8.18,
                "E":4.25,
                "Q":0,
                "G":0,
                "H":6,
                "I":0,
                "L":0,
                "K":10.53,
                "M":0,
                "F":0,
                "P":0,
                "S":0,
                "T":0,
                "W":0,
                "Y":10.07,
                "V":0, 
                "+":7.4,
                "-":3.6 }
                
def HH(pKa):
    """returns fraction of base yet to be dissociated. Found using the
    Henderson-Hasselbalch equation:
    pH = pKa + log (base/acid)
    """
    b = 10**(pH-pKa)
    a = 1
    
    if (pKa < pH):
        ans = (a) / (b+a)
    elif (pKa > pH):
        ans = (-1*b) / (b+a)
    
    return ans      
                
if __name__ == "__main__":
    
    #add amino and carboxyl groups to seq
    seq = "+" + seq + "-"
    
    for i in seq:
        if ((abs(amino_acids[i] - pH)) <= 2):
            charge = charge + HH(amino_acids[i])

        elif (amino_acids[i] == 0):
            pass
                
        elif (amino_acids[i] > pH):
            charge = charge + 1
            
        elif (amino_acids[i] < pH):
            charge = charge - 1       
            
    print charge