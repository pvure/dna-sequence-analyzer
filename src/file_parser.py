class FASTASequence:
    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence.upper()
        
    def __len__(self):
        return len(self.sequence) 
    
    def __str__(self):
        stringform = ">" + self.header + "\n" + self.sequence
        return stringform
    

class FASTAParser:
    """Parses FASTA files and stores sequences in dynamic arrays."""
    
    def __init__(self):
        self.sequences = []
    
    def parse_file(self, filename):

        current_header = None
        current_sequence_data = ""
        
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                
                if line.startswith(">"):
                    #save previous sequence if we have one
                    if current_header is not None:
                        self.sequences.append(FASTASequence(current_header,current_sequence_data))
                    
                    #start new sequence
                    current_header = line.replace(">", "")
                    current_sequence_data = ""

                else:
                    current_sequence_data += line
        
        #last sequence
        if current_header is not None:
            self.sequences.append(FASTASequence(current_header,current_sequence_data))
    
    def get_sequences(self):
        return self.sequences
    
    def get_sequence_count(self):
        return len(self.sequences)
