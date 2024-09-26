import Bio
from Bio.Blast import NCBIWWW, NCBIXML

def perform_blast(file_path, e_value_threshold=0.01):
    """
    Perform a BLAST search on a given FASTA sequence file.

    Parameters:
    - file_path (str): The path to the FASTA file containing the sequence(s).
    - e_value_threshold (float): The E-value threshold for reporting significant alignments (default is 0.01).
    """
    try:
        # Read the contents of the FASTA file into a string
        with open(file_path) as file:
            fasta_string = file.read()
        
        # Perform a BLAST search using the sequence read from the FASTA file
        result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
        
        # Parse the BLAST results from the result handle
        blast_record = NCBIXML.read(result_handle)

        count = 0  # Initialize a counter for significant alignments
        # Iterate through the alignments in the BLAST record
        for alignment in blast_record.alignments:
            # Iterate through the high-scoring pairs (HSPs) in each alignment
            for hsp in alignment.hsps:
                # Check if the E-value of the HSP is below the specified threshold
                if hsp.expect < e_value_threshold:
                    count += 1  # Increment the count of significant alignments
                    print("****Alignment****")
                    print("sequence:", alignment.title)  # Print the sequence title
                    print("length:", alignment.length)    # Print the length of the sequence
                    print("e value:", hsp.expect)         # Print the E-value of the HSP
                    print(hsp.query)                      # Print the query sequence
                    print(hsp.match)                      # Print the matching region
                    print(hsp.sbjct)                     # Print the subject sequence

        # Print the total number of significant alignments found
        print(f"Total alignments found with E-value < {e_value_threshold}: {count}")

    except FileNotFoundError:
        print("Error: FASTA file not found.")  # Handle the case where the file does not exist
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other exceptions

# Call the function with your FASTA file in the same directory
perform_blast("myseq.fa")  # This assumes myseq.fa is in the same directory as this script


