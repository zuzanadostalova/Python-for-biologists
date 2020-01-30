# # Processing DNA in a file

# seq1 = "ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC"
# print(len(seq1))
# adapter = seq1[0:15]

# seq2 = "ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT"
# print(len(seq2))

# seq3 = "ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC"
# print(len(seq3))

# seq4 = "ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA"
# print(len(seq4))

# seq5 = "ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA"
# print(len(seq5))

# adapter = [0:15]
# print(line.replace()

# need to put the txt in the same file as Py for biologists
# file = open("input.txt")
# output = open("04_exercise_Trimmed.txt", "w") # output = open... has to be outside the for loop!

# for line in file:
#     # print("The length is " + str(len(line)))

# # Output:
# # The length is 57
# # The length is 52
# # The length is 63
# # The length is 48
# # The length is 62

# # different from manual typing
#     adapter = line[0:14] # 14 elements, counting from 0 - till number 13
#     trimmed = line.replace(adapter, "")
#     # output = open("04_exercise_Trimmed.txt", "w") - this would write only the last seq
#     output.write(trimmed)
#     print(trimmed)
#     print("The length is " + str(len(trimmed)))

# Multiple exons from gDNA
genomic_dna = open("genomic_dna.txt").read()
exon_locations = open("exons.txt")
coding_sequence = ""
for line in exon_locations:
    positions = line.split(",")
    start = positions[0]
    stop = positions[1]
    print("The start is " + start + ", the stop is " + stop)
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
    print("The coding sequence is : " + coding_sequence)