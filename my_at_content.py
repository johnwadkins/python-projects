dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(dna)

a_count = dna.count('A')
t_count = dna.count('T')

at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))
