def getRna(dna):
    rna = ""
    for char in dna :
        if char == 'A':
            rna += 'U'
        elif char == 'C':
            rna += 'G'
        elif char == 'T':
            rna += 'A'
        elif char == 'G':
            rna += 'C'
        else :
            return 'Your string contains a non DNA character (only ACGT).'
    return rna

dna = "ACGT"
print(getRna(dna))