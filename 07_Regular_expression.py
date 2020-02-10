# # Accession names
# accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
# # print(accs[0][1])
# # "xkn59438", k


# # for name in accs:   
#     # n = accs[0:8]
#     # index = accs[0:][0:]
#     # print(index)

#     # I:
#     # Sol.I:
#     # if "5" in name:
#     #     print(name)
#     # xkn59438
#     # hedle3455
#     # xjhd53e
#     # 45da

#     # Sol.I:
# # import re
#     # for acc in accs:
#     #     if re.search(r"5", acc):
#     #         print(accs)

#     # II:
#     # Sol.I:
#     # if "d" in name or "e" in name:
#     #     print(name)
#     # yhdck2
#     # eihd39d9
#     # chdsye847
#     # hedle3455
#     # xjhd53e
#     # 45da
#     # de37dp

#     # # Sol.II:
#     # for acc in accs:
#     #     if re.search(r"(d|e)", acc):
#     #         print(acc)
#     # yhdck2
#     # eihd39d9
#     # chdsye847
#     # hedle3455
#     # xjhd53e
#     # 45da
#     # de37dp

# # # III:
# # for acc in accs:
# #     if re.search("d.*e", acc):
# #         print(acc)
# # chdsye847
# # hedle3455
# # xjhd53e
# # de37dp

# # IV:
# # for acc in accs:
# #     if re.search("d[l]e", acc):
# #         print(acc)
    

#     # V:
#     # if "d" and "e" in name:
#     #     print(name)

#     # VI:
#     # Sol.I:
#     # first_letter = name[0]
#     # # print(first_letter)
#     # if first_letter == "x" or first_letter ==  "y":
#     #     print(name)
#     # kn59438
#     # yhdck2
#     # xjhd53e
     
#     # Sol.II:
# # import re
# # for acc in accs:
# #     if re.search(r"^(x|y)", acc):
# #         print(acc)
# # xkn59438
# # yhdck2
# # xjhd53e

# import re
# # for acc in accs:
# #     if re.search(r"^(x|y).*e$", acc):
# #             print(acc)
# # xjhd53e

#     # VII.
# # Sol.I:
# # for acc in accs:
# #     if re.search(r"[123456789]{3,100}", acc):
# #         print(acc)
# # xkn59438
# # chdsye847
# # hedle3455

# # Sol.II:
# for acc in accs:
#     if re.search(r"\d{3,}", acc):
#         print(acc)
# # xkn59438
# # chdsye847
# # hedle3455

# # VIII.
# for acc in accs:
#     if re.search(r"d[arp]$", acc):
#         print(acc)
# # 45da
# # # de37dp

# dna = open("dna.txt").read().rstrip("\n")
import re
# print("AbcI cuts at:")
# for match in re.finditer(r"A[ATGC]TAAT", dna):
#     print(match.start())
# # AbcI cuts at:
# # 1140
# # 1625

# dna = open("dna.txt").read().rstrip("\n")
# import re
# print("AbcI cuts at:")
# for match in re.finditer(r"A[ATGC]TAAT", dna):
#     print(match.start() + 3)
# # the enzyme cuts 3 bases downstream of the start
# # AbcI cuts at:
# # 1143
# # 1628

# dna = open("dna.txt").read().rstrip("\n")
# all_cuts = [0]
# for match in re.finditer(r"A[ATGC]TAAT", dna):
#     all_cuts.append(match.start() + 3)
# all_cuts.append(len(dna))
# print(all_cuts)
# # [0, 1143, 1628, 2012]

# for i in range(1, len(all_cuts)):
#     this_cut_position = all_cuts[i]
#     previous_cut_position = all_cuts[i-1]
#     fragment_size = this_cut_position -previous_cut_position
#     print("one fragment size is " + str(fragment_size))
# # one fragment size is 1143
# # one fragment size is 485
# # one fragment size is 384

# dna = open("dna.txt").read().rstrip("\n")
# all_cuts = [0]

# for match in re.finditer(r"A[ATGC]TAAT", dna):
#     all_cuts.append(match.start() + 3)

# for match in re.finditer(r"GC[AG]TG", dna):
#     all_cuts.append(match.start() + 4)

# all_cuts.append(len(dna))
# print(all_cuts)
# # [0, 1143, 1628, 861, 1587, 1783, 2012]
# # incorrect - we need to use sort

dna = open("dna.txt").read().rstrip("\n")
all_cuts = [0]

for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)

for match in re.finditer(r"GC[AG]TG", dna):
    all_cuts.append(match.start() + 4)

all_cuts.append(len(dna))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)

for i in range(1, len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("One fragment size is " + str(fragment_size))

# [0, 861, 1143, 1587, 1628, 1783, 2012]
# one fragment size is 861
# one fragment size is 282
# one fragment size is 444
# one fragment size is 41
# one fragment size is 155
# one fragment size is 229