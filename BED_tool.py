# send commands to system (linux)
# download from URL with wget
! wget https://www.encodeproject.org/files/ENCFF861KMV/@@download/ENCFF861KMV.bed.gz
# gunzip to uncompress the archive
! gunzip ENCFF861KMV.bed.gz

# distribution plot, the hard way.
input_file = "ENCFF861KMV.bed"
dict_dist = {}

# dict_dist = {chrom_name[interval:count]}
# dict_dist[chrom_name]... when refering to the contents inside chrom_name list

with open(input_file, 'r') as text:
  for line in text.readlines():
    column = line.strip().split("\t")
    chrom_name = column[0]
    start = int(column[1])
    end = int(column[2])
    interval = end - start

    if chrom_name in dict_dist:
      dict_dist[chrom_name].append(interval)

    else:
      dict_dist[chrom_name] = [] # first the empty dictionary
      dict_dist[chrom_name].append(interval)

print(dict_dist) # to print out key value pairs of chromosomes with corrresponding intervals

for chrom_name in dict_dist: # iterating over the list in the dictionary
  # print(chrom_name) # to print out the individual chromosomes
  # print(dict_dist[chrom_name]) # to print out the list of intervals

# Experiments 

  # print([chrom_name]) prints out "['chr9']"
  # print(chrom_name) prints out "chr9"

  # print(chrom_name[0]) prints "c" because we are not entering the list inside "chrom_name" but the first character of the each key of chrom_name - "chr9", "chr3", "chr8"
  # print(chrom_name[3]) prints the fourth character of the each key of chrom_name - for "chr9" - 9, for "chr3" - 3, for "chr8" - 8
  # print([chrom_name[0]]) prints "c" because we are not entering the list inside "chrom_name" but the first character of the each key of chrom_name - "chr9", "chr3", "chr8"

# print(dict_dist[2]) # raises key error - key 2 does not exist
# print(dict_dist["chr3"]) prints the list with intervals from chromosome 3
# print(dict_dist[chrom_name][: :2]) # from beginning till the end, every second 

# check https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn/
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)

for index, chromosome in enumerate(dict_dist):
    # create data
    test=pd.Series(data=dict_dist[chromosome])
    if index == 0:
      sns.distplot( test , color="skyblue", ax=axes[0, 0])
    elif index == 1:
      sns.distplot( test , color="skyblue", ax=axes[1, 0])
    elif index == 2:
      sns.distplot( test , color="skyblue", ax=axes[0, 1])
    else:
      sns.distplot( test , color="skyblue", ax=axes[1, 1])

# load Bed file as pandas dataframe
input_file = "ENCFF861KMV.bed"
import pandas as pd
df = pd.DataFrame.from_dict(dict_dist, orient='index')

for chrom_name, group in df.groupby(by="chromosome"):
  # plot only chr9 distribution
  if chrom_name == 'chr9':
    group["interval"].hist(bins=20)