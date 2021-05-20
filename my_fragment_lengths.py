#my_fragment_lengths
#calculates the lengths of the two fragments
#produced by a restriction enzyme

dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
recognition_site = "GAATTC"

fragment_1 = dna.find(recognition_site) +1
fragment_2 = len(dna) - fragment_1
print("Fragment 1 is " + str(fragment_1) + " nucleotides long.")
print("Fragment 2 is " + str(fragment_2) + " nucleotides long.")

