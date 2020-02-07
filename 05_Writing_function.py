# Writing own functions I
# Assignment:
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
# assert my_function("msrslllrfllfllllpplp", "L") == 50
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

# Sol.I:
# For a particular AA
# def count_percentage(l1, aa):
#     length = len(l1)
#     aa_count = l1.count("M")
#     aa_content = (aa_count/length)*100
#     print(aa_content)
#     return aa_content # I am interested in aa_content

# # print(l1.count("M"))

# print(count_percentage("MSRSLLLRFLLFLLLLPPLP", "M"))

# # Sol.II:
# # For all:
# # no need to provide arguments for the function apriori
# # provide arguments after defining it when you are calling it within print
# def count_percentage(p, aa):
#     length = len(p)
#     aa_count = p.lower().count(aa.lower())
#     aa_content = (aa_count/length)*100
#     return aa_content # I am interested in aa_content, returning to save it

# # # printing the function
# # print(count_percentage("MSRSLLLRFLLFLLLLPPLP", "M"))
# # print(count_percentage("MSRSLLLRFLLFLLLLPPLP", "r"))
# # print(count_percentage("msrslllrfllfllllpplp", "L"))
# # print(count_percentage("MSRSLLLRFLLFLLLLPPLP", "Y"))
# # # 5.0
# # # 10.0
# # # 50.0
# # # 0.0

# # or positive control
# assert count_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
# assert count_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
# assert count_percentage("msrslllrfllfllllpplp", "L") == 50
# assert count_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0 
# # if matched with the experimental data it does not raise error

# assert count_percentage("MSRSLLLRFLLFLLLLPPLP", "L") == 0 
# # assert count_percentage("MSRSLLLRFLLFLLLLPPLP", "L") == 0, AssertionError

# Writing own functions II
# def count_percentage(p, df_aa=None):
#     df_aa = ["A","I","L","M","F","W","Y","V"]
#     aa, df_aa = count_percentage(p)
#     for x in p:
#         if x == aa:
#             length = len(p)
#             aa_count = p.upper().count(aa)
#             aa_content = (aa_count/length)*100
#         else:
#             x == df_aa
#             length = len(p)
#             dfaa_count = p.upper().count(df_aa)
#             dfaa_content = (dfaa_count/length)*100
#     return aa_content, dfaa_content

protein = "MSRSLLLRFLLFLLLLPPLP"
aa_list = ["A","I","L","M","F","W","Y","V"]

# ?
def get_aa_percentage(protein, aa_list = ["A","I","L","M","F","W","Y","V"]):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count # total of matching aa
    percentage = total * 100 / protein_length
    return percentage

    # def count_percentage(p, aa):
#     length = len(p)
#     aa_count = p.lower().count(aa.lower())
#     aa_content = (aa_count/length)*100
#     return aa_content

print(get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']))
print(get_aa_percentage("MSRSLLLRFLLFLLLLPPLP"))
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65