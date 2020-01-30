# # 8. chapter - Dictionaries
# # DNA translation
# # I. split DNA seq into codons
# # II. look up AA residue for each codon
# # III. join all AA to give a protein

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


# # def translate_dna(dna):
# #     last_codon_start = len(dna) - 2
# #     protein = ""
# #     for start in range(0, last_codon_start, 3)
# #     codon = dna[start:start+3]

# # I. 
# # spliting into codons manually
# dna = "ATGTTCGGT" # create a substring
# codon1 = dna[0:3]
# codon2 = dna[3:6]
# codon3 = dna[6:9]
# print(codon1, codon2, codon3)
# # Output: ATG TTC GGT

# # range automatically into codons
# # start at 0 at steps of 3, finishes at 7
# dna = "ATGTTCGGT" 
# for start in range(0,7,3): # defining start
#     codon = dna[start:start+3] # to find the stop position
#     print("One codon is " + codon)

# # II. translating
# # look up the AA for the given codon
#     print("The amino acid is " + gencode[codon])

# III. add new AA to the end of a protein
# sequence = ""
# dna = "ATGTTCGGT" 
# for start in range(0,len(dna),3):
#     codon = dna[start:start+3]
#     aa = gencode.get(codon)
#     sequence = sequence + aa
# print(sequence)

# # to turn the code into function
# def translate_dna(dna):

#     sequence = ""
#     for start in range(0,len(dna),3):
#         codon = dna[start:start+3]
#         aa = gencode.get(codon)
#         sequence = sequence + aa
#     return sequence

# print(translate_dna("ATGTTCGGT"))
# print(translate_dna("ATGTTCGGTA")) # TypeError: can only concatenate str (not "NoneType") to str

# Error handling
# Therefore we need to assure translation of sequence of any length

# If there is an incomplete codon and the seq is not an exact multiple of three
# we need to set the start position of the final codon to equal to the length
# of the DNA sequence minus 2 - there will be always two more characters following
# the position of the final codon start

# def translate_dna(dna):

#     last_codon_start = len(dna) - 2 # to translate any length
#     sequence = ""
#     for start in range(0,last_codon_start,3):
#         codon = dna[start:start+3]
#         aa = gencode.get(codon)
#         sequence = sequence + aa
#     return sequence
# print(translate_dna("ATGTTCGGTA")) # output: MFG, ignores the single base
# print(translate_dna("ATGTTCGGTAGCGC")) # Output: MFGS, no problem, ignores the dinucleo

# If writing undetermined base
def translate_dna(dna):
    last_codon_start = len(dna) - 2 # to translate any length
    sequence = ""
    for start in range(0,last_codon_start,3):
        codon = dna[start:start+3]
        aa = gencode.get(codon, "X") # error without this line, with it: MXG
        sequence = sequence + aa
    return sequence

# print(translate_dna("ATGTNCGGTA")) # TypeError: can only concatenate str (not "NoneType") to str
# print(translate_dna("ATGTTCGGTA"))

assert(translate_dna("ATGTTCGGT"))  == "MFG"
assert(translate_dna("ATCGATCGAT")) == "IDR"
assert(translate_dna("ACGANCGAT"))  == "TXD" 
