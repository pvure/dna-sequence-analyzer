#calculating gc content
#important because gc content influences stability, gene expression, and more

def calculate_gc_content(sequence):
    if len(sequence) == 0:
        return 0
    
    gc_count = 0
    for nucleotide in sequence:
        if nucleotide in ['G','C']:
            gc_count += 1

    gc_content = (gc_count / len(sequence)) * 100
    return gc_content

def reverse_complement(sequence):
    ReverseComplement = ""
    mapping = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    if len(sequence) == 0:
        return ""
    for nucleotide in range (len(sequence), 0, -1):
        if sequence[nucleotide-1] not in mapping:
            raise ValueError(f"Invalid nucleotide '{sequence[nucleotide-1]}' at position {nucleotide-1}")
        ReverseComplement += mapping[sequence[nucleotide-1]]
    return ReverseComplement
    

def find_orfs(sequence, min_length=30):
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    i = 0
    while i <= len(sequence) - 3:
        if sequence[i:i+3] == start_codon:
            #look for stop
            j = i + 3
            while j <= len(sequence) - 3:
                if sequence[j:j+3] in stop_codons:
                    orf_length = j + 3 - i  
                    if orf_length >= max(6, min_length):
                        orfs.append((i, j+2, sequence[i:j+3])) 
                    i = j + 3
                    break  
                j += 3  
            else:
                i += 3 
        else:
            i += 3
    
    return orfs
