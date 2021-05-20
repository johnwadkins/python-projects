# my_intron_splicing_1
# removes the intron from a sequence
# and splices the two exons back together

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = genomic_dna[0:63]
exon_2 = genomic_dna[91:]

intron_1 = genomic_dna[64:90]
intron_lower = intron_1.lower()
print(exon_1 + exon_2)
print(exon_1 + intron_lower + exon_2)
print(genomic_dna)

exon_total = len(exon_1) + len(exon_2)

print(exon_total / len(genomic_dna))