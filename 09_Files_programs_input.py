# # I. File manipulations
# import os
# os.rename("old.txt", "new.txt") # if the file in the working directory

# # if elsewhere - provide complete path:
# os.rename("/home/martin/biology/old.txt","/home/martin/biology/new.txt")

# # if diff folder but same file name - the function moving file to another folder

# # or move AND rename in the same step

# # new folder created with os.mkdir()
# # if simultaneously more - os.mkdirs()

# # copy file/folder - shutil; shutil.copy() - single file, shutil.copytree()

# # os.path.exists() - boolean

# # II. Deleting
# # os.remove() - file, os.rmdir() - folder, shutil.rmtree() - file and folders

# # III. Listing contents
# # os.listdir()

# # External programs

# # Running a program
# # subprocess.call() - external

# import subprocess
# subprocess.call("/bin/date")

# # to supply cmd line to the external program
# subprocess.call("/bin/date +%B, shell=True")

# # Capturing output
# month = subprocess.check_output("/bin/date +%B, shell=True")

import os 
for file_name in os.listdir("."):
    if file_name.endswith("dna"):
        print("Reading sequences from " + file_name)
# Reading sequences from xag.dna
# Reading sequences from xaf.dna
# Reading sequences from xad.dna
# Reading sequences from xae.dna
# Reading sequences from xaa.dna
# Reading sequences from xab.dna
# Reading sequences from xac.dna
# Reading sequences from xah.dna
# Reading sequences from xai.dna
# Reading sequences from xaj.dna

for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("Reading sequences from " + file_name)
        dna_file = open(file_name)

        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            print("Found a dna sequence with length " + str(length))

for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("Reading sequences from " + file_name)

        dna_file = open(file_name)
        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            print("Sequence length is " + str(length))

            for bin_lower in range(100,1000,100):
                bin_upper = bin_lower + 99
                if length >= bin_lower and length <= bin_upper:
                    print("Bin is " + str(bin_lower) + " to " + str(bin_upper))

def process_sequence(line):
    dna = line.rstrip("\n")
    length = len(dna)
    print("Sequence length is " + str(length))
    for bin_lower in (100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
            print("Bin is " + str(bin_lower) + " to " + str(bin_upper))

for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("Reading sequences from " + file_name)
        dna_file = open(file_name)
        process_sequence(line)