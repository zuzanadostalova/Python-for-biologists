# # Reading text from a file
# open()

# my_file = open("dna.txt")
# # file on a hard drive

# read()

# my_file_name = "dna.txt"
# file_contents = open(my_file_name)
# my_file_contents = my_file.read()

# Exercises

# Splitting genomic DNA
my_DNA_file = open("GenomicDNA.txt") 
my_DNA = my_DNA_file.read()
exon_1 = my_DNA[0:63]
non_coding = my_DNA[63:90]
exon_2 = my_DNA[90: ]
# print(exon_1.upper() + non_coding.lower() + exon_2.upper())

exon = exon_1 + exon_2

# print(coding)
# print(non_coding.lower())

coding = open("Coding.txt", "w")
coding.write(exon)

noncoding = open("Non_coding.txt", "w")
noncoding.write(non_coding.lower())