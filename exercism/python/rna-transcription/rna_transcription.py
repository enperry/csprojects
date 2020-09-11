def to_rna(dna_strand):
    for char in dna_strand:
        if(char == "G"):
            char = "C"
        elif(char == "C"):
            char = "G"
        elif(char == "T"):
            char = "A"
        elif(char == "A"):
            char = "U"
        else:
            char = " "

    return dna_strand