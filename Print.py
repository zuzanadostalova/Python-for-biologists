# Chapter 2 - Printing and manipulating text

# new GitHub repository -> username -> repositories -> new-name -> 
# create file on GitHub -> open upper terminal with cmd + shift + P, Git: clone -> 
# coppied URL from GitHub -> create through it file on the laptop

# do not omit quotes
# use comments
# error messages and debugging - common buggs (?): forgotten quotes, mis-spelling,
# statement splitted over two lines - EOL (end of the line) while scan. string literal =>
# printing special characters - \n - newline, \r - carriage  return, cursor back to the start of 
# the line without starting new - OVERWRITE, \t - tab, for codes with huge output

# variable names are arbitrary - we can use whatever name we want
# length = returns a value, not text like print(), and runs without output, if printed - number
# str(dna_length) - takes argument (number) returns a value (string) representing number
# int("4") - string turned into number

# to change the case - method .lower() - returns a copy in lowercase, method is not 
# bult in, belongs to a particular type, is writen behind argument - my_dna.lower()
# cannot be used to an integer - "int" object has no attribute "lower" -> method can
# be used only on the the type it belongs to

# Replacement - print(protein.replace("v","y")); exchange all v for y, even more characters

# Extracting part of a string - substring, print(protein[3:5])
# from 0, inclusive at the start, exlusive in the end

# Counting and finding substrings - count() - single argument type string, returns
# the number! of times that the argument is found

# where are the resiudes? find(); if the substring does not exist = -1

# disadvantage - with count() and find you can only search for an exact substring

# replace(), count(), and find()

# exercises:

# 1. caluculating AT content

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(dna)
a_count = dna.count("A")
t_count = dna.count("T")
AT_content = (a_count + t_count) / length
print("AT content is " + str(AT_content))

# 2. caluculating complementing DNA
# dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Replacement1 = dna.replace("A","T")
# print(Replacement1)
# Replacement2 = Replacement1.replace("T","A")
# print(Replacement2)
# Replacement3 = Replacement2.replace("C","G")
# print(Replacement3)
# Replacement4 = Replacement3.replace("G","C")
# print(Replacement4)

# 3. restriction fragment lengths
# EcoRI cuts at G*AATTC
# my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# frag1_length = my_dna.find("GAATTC") + 1
# frag2_length = len(my_dna) - frag1_length
# print("length of fragment one is " + str(frag1_length))
# print("length of fragment two is " + str(frag2_length))

# 4. splicing out introns, part one
# genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# # # print(genomic_dna)
# length_genom = len(genomic_dna)
# exon_1 = genomic_dna[0:64]
# length_exon_1 = len(exon_1)
# exon_2 = genomic_dna[91: ]
# length_exon_2 = len(exon_2)
# exon_percentage = (length_exon_1 + length_exon_2) / length_genom
# print("Exon percentage is " + str(exon_percentage))
# print(exon_1 + exon_2)
# print(length_exon_1, exon_1, length_exon_2, exon_2, genomic_dna.replace(exon_2, ""), sep="\n")

# # 5. part two
# genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# # # print(genomic_dna)
# length_genome = len(genomic_dna)
# exon_1 = genomic_dna[0:64]
# length_exon_1 = len(exon_1)
# exon_2 = genomic_dna[91: ]
# length_exon_2 = len(exon_2)
# exon_percentage = 100*((length_exon_1 + length_exon_2) / length_genome)
# print("Exon percentage is " + str(exon_percentage))
# non_coding = genomic_dna[64:91]
# print(non_coding)


# 6 part three
# genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# exon_1 = genomic_dna[0:64]
# non_coding = genomic_dna[64:91]
# exon_2 = genomic_dna[91: ]
# print(exon_1.upper() + non_coding.lower() + exon_2.upper())