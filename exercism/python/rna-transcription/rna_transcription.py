def to_rna(dna_strand):
    transcriptionDict = {'G':'c', 'C':'g', 'T':'a', 'A':'u'}
    for nucleotide in transcriptionDict:
        dna_strand = dna_strand.replace(nucleotide, transcriptionDict[nucleotide])
    return dna_strand.upper()