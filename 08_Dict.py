# ---------------------------------------

# def translate_dna(dna):

#     last_codon_start = len(dna) - 2 # code works, but defined last codon is not used anywhere
#     sequence = ""
#     for start in range(0,len(dna),3):
#         codon = dna[start:start+3]
#         aa = gencode.get(codon)
#         sequence = sequence + aa
#     return sequence
# print(translate_dna("ATGTTCGGT"))

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