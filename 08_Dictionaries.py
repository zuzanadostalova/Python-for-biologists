# 8. chapter - Dictionaries
# DNA translation
# I. split DNA seq into codons
# II. look up AA residue for each codon
# III. join all AA to give a protein

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


# def translate_dna(dna):
#     last_codon_start = len(dna) - 2
#     protein = ""
#     for start in range(0, last_codon_start, 3)
#     codon = dna[start:start+3]

# I. 
# spliting into codons manually
dna = "ATGTTCGGT" # create a substring
codon1 = dna[0:3]
codon2 = dna[3:6]
codon3 = dna[6:9]
print(codon1, codon2, codon3)
# Output: ATG TTC GGT

# range automatically into codons
# start at 0 at steps of 3, finishes at 7
dna = "ATGTTCGGT" 
for start in range(0,7,3): # defining start
    codon = dna[start:start+3] # to find the stop position
    print("One codon is " + codon)

# II. translating
# look up the AA for the given codon
    print("The amino acid is " + gencode[codon])





# for (k,v) in gencode.items():
#     codons = k
#     print(codons)
#     print(k,v)
#     residue = v
#     print(v)

# print(gencode['TGC'])

# print(dict.values(gencode))
	
# # Create a new list from the view object returned by values() 
# dictValues = list(gencode.values())
# print(dictValues)

# Output: ['I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 
# 'R', 'R', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 
# 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 
# 'G', 'G', 'S', 'S', 'S', 'S', 'F', 'F', 'L', 'L', 'Y', 'Y', '_', '_', 'C', 'C', '_', 'W']


# for line in gencode:
#     print(line)
#     name = line.strip().split("\t")
#     print(name)
# print(gencode['TGG'])

# input_file = "genetic_code.txt"
# with open(input_file, 'r') as text:
#   for line in text.readlines():
#       column = line.strip().split(",")
#       print(column)

 

# for row in gencode:
#     print(row)
    # column = line.strip().split("\t")
    # codon = column[0]
    # print(codon)

# input_file = "genetic_code.txt"
# with open(input_file, 'r') as text:
#     for key, value in gencode.items():
#         prot = [key, value]
#         for line in text.readlines():
#             prot = line.strip().split(",") # ['ATA']
#             print(prot)
