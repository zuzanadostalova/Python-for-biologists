# 3. Chapter - Reading text from a file
open()

my_file = open("dna.txt")
# file on a hard drive

# read()

my_file_name = "dna.txt"
file_contents = open(my_file_name)
my_file_contents = my_file.read()

# Exercises

# 1. Splitting genomic DNA
my_DNA_file = open("GenomicDNA.txt") 
# .txt - just a plain text, no variables, just the DNA sequence
# always save also text files or you will not see the output
my_DNA = my_DNA_file.read()

exon_1 = my_DNA[0:63]
intron = my_DNA[63:90]
exon_2 = my_DNA[90: ]
# print(exon_1.upper() + non_coding.lower() + exon_2.upper())

exon = exon_1 + exon_2

# print(coding)
# print(non_coding.lower())

coding = open("Coding.txt", "w")
coding.write(exon)

noncoding = open("Non_coding.txt", "w")
noncoding.write(intron.lower())

# 2. FASTA file
# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# make a new file to hold the output
output = open("sequences.fasta", "w")

# write the header and sequence for seq1
output.write(">" + header_1 + "\n" + seq_1 + "\n")
# write the header and uppercase sequences for seq2
output.write(">" + header_2 + "\n" + seq_2.upper() + "\n")
# write the header and sequence for seq3 with hyphens removed
output.write(">" + header_3 + "\n" + seq_3.replace("-","") + "\n")

# Writing multiple fasta files
# three new files to hold the output using concatenation
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")

# one sequence to each output file
output_1.write(">" + header_1 + "\n" + seq_1 + "\n")
output_2.write(">" + header_2 + "\n" + seq_2.upper() + "\n")
output_3.write(">" + header_3 + "\n" + seq_3.replace("-", "") + "\n")