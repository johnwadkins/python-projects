# my complement dna
# produces a complimentary strand of DNA
# given a DNA sequence

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

change_A = dna.replace("A", "t")
change_T = change_A.replace("T", "a")
change_C = change_T.replace("C", "g")
change_G = change_C.replace("G", "c")
print(dna),
print(change_C.upper())
