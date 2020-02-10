# Conditional tests
# print(df["Drosophila melanogaster"][4]) Drosoph. ananassae
# print(df["Drosophila melanogaster"][4][1]) second letter "r" in Drosoph. ananassae

data = open("data.csv")
for line in data:
    column = line.rstrip("\n").split(",")
    species = column[0]
    sequence = column[1]
    gene = column[2]
    expression = column[3]
    # print(species)

# I. Several species
if species == "Drosophila melanogaster" or species == "Drosophila simulans":
    print(gene)

# Drosophila melanogaster
# kdy647
# Drosophila melanogaster
# jdg766
# Drosophila simulans
# kdy533
# Drosophila yakuba
# Drosophila ananassae
# Drosophila ananassae

# II. length range

    # Sol.I:
    length = len(sequence)
    if length in range(91,109):
        print(gene)
    
    # kdy647 - disappears when 109
    # kdy533 - has 90 b - it is better to set the range from 91 to 110
    # teg436 - 

    # Sol.II:
    if len(sequence) > 90 and len(sequence) < 110:
        print(gene)

    # kdy647 - disappears when 109
    # teg436 

# III. AT content

    a_count = sequence.count("a")
    t_count = sequence.count("t")
    at_count = (a_count+t_count)/length
    print(at_count)
    # 0.7247706422018348
    # 0.5641025641025641
    # 0.5333333333333333
    # 0.2857142857142857
    # 0.5299145299145299
    # 0.45918367346938777

    if ((a_count+t_count)/length) < 0.5 and int(expression) > 200:
        print(gene)
        # teg436

# IV. high low medium
    if at_count > 0.65:
        print(gene + " has high AT content")

    if at_count > 0.45 and at_count < 0.65:
        print(gene + " has medium AT content")

    if at_count < 0.45:
        print(gene + " has low AT content")

# V. complex condition
    first_letter = gene[0]
    print(first_letter)
    # k
    # j
    # k
    # h
    # h
    # t

    # Sol.I:

    # Wrong:
    if first_letter == "k" or "h":
        print(gene)
    # prints everything
    # kdy647
    # jdg766
    # kdy533
    # hdt739
    # hdu045
    # teg436

    if first_letter == "k" or first_letter == "h":
        print(gene)
    # kdy647
    # kdy533
    # hdt739
    # hdu045

    # works well but if "AND" condition with melanogaster would be added to the end
    # it would not be applied

    # Sol.II:
    if first_letter == "k":
        print(gene)
    # kdy647
    # kdy533

    # Except from Drosoph. melanogaster:
    if first_letter == "k" and species != "Drosophila melanogaster":
        print(gene)
    # kdy533

    if first_letter == "h":
        print(gene)
    # hdt739
    # hdu045 - do not use "OR", "OR" is True if at least one is True

    