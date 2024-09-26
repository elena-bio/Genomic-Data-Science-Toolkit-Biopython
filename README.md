## Project Overview

This repository contains a Biopython-based script that accompanies the project **"Identify the Species of an Unknown DNA Sequence Using BLAST"**. The script allows users to input a FASTA file with DNA sequences and uses the NCBI BLAST (Basic Local Alignment Search Tool) service to identify the species from which the DNA sequence likely originated.

## Requirements

To run this script, you need the following:

- **Python 3.x**: Make sure Python 3.x is installed. You can check your Python version by running:
  
    ```bash
    python --version
    ```

- **Biopython library**: The script depends on the Biopython library for BLAST functionalities. To install it, use the following pip command:

    ```bash
    pip install biopython
    ```

- **Internet connection**: Since the script performs BLAST searches via NCBI, an active internet connection is required to fetch the BLAST results.

## How to Run the Script

Follow the steps below to execute the script:

1. **Clone the repository**: First, clone the repository from GitHub to your local machine.

    ```bash
    git clone https://github.com/YOUR_USERNAME/Genomic-Data-Science-Toolkit-Biopython.git
    ```

2. **Navigate to the project directory**: Change into the directory where the repository was cloned.

    ```bash
    cd Genomic-Data-Science-Toolkit-Biopython
    ```

3. **Run the Python script**: Make sure that the `myseq.fa` file (your input FASTA sequence) is in the same directory as the Python script. Then, run the script by executing:

    ```bash
    python Bio-python.py
    ```

## Example Usage

For instance, if you have a FASTA file `myseq.fa` in the same directory, simply run:

```bash
python Bio-python.py
```

## Script Explanation

The script includes:

- **Input**: A DNA sequence stored in a FASTA file (`myseq.fa`).
- **Output**: A list of significant alignments from the BLAST search, including the aligned sequences, E-values, and additional information.
- **Customization**: Users can adjust the E-value threshold for more or fewer significant matches.

## Code

Here’s the full code for the project:

```python
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
                    print(hsp.sbjct)                      # Print the subject sequence

        # Print the total number of significant alignments found
        print(f"Total alignments found with E-value < {e_value_threshold}: {count}")

    except FileNotFoundError:
        print("Error: FASTA file not found.")  # Handle the case where the file does not exist
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other exceptions

# Call the function with your FASTA file in the same directory
perform_blast("myseq.fa")
```

- **Internet connection**: The script sends BLAST requests to NCBI servers, so an active internet connection is required for the script to function.

## How to Run the Script

Follow the steps below to run the script:

1. **Clone the repository**: Download the project files from GitHub by cloning the repository.

    ```bash
    git clone https://github.com/YOUR_USERNAME/Genomic-Data-Science-Toolkit-Biopython.git
    ```

2. **Navigate to the project directory**: Change into the project directory after cloning.

    ```bash
    cd Genomic-Data-Science-Toolkit-Biopython
    ```

3. **Run the Python script**: Execute the `Bio-python.py` script in your terminal. Ensure that the `myseq.fa` file is in the same directory, or update the file path accordingly.

    ```bash
    python Bio-python.py
    ```

### Example of running the script:
Make sure the `myseq.fa` file is in the project directory, then run the script as shown:

```bash
python Bio-python.py




# Genomic-Data-Science-Toolkit-Python
