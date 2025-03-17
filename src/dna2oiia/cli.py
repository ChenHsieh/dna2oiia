import argparse
import os
from dna2oiia.converter import dna_to_oiia, process_fasta

def main():
    parser = argparse.ArgumentParser(description="Convert DNA sequences or FASTA files into Oiia sounds.")
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-s", "--string", type=str, help="DNA sequence to convert")
    input_group.add_argument("-f", "--file", type=str, help="Path to a FASTA file containing the DNA sequence")

    parser.add_argument("-o", "--output", type=str, default="output.wav", help="Output audio file name")

    args = parser.parse_args()

    # Handle DNA sequence directly
    if args.string:
        dna_sequence = args.string.upper()  # Ensure it's uppercase
        print(f"Processing DNA sequence: {dna_sequence}")


    # Handle FASTA file input
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"Error: File '{args.file}' not found!")
            exit(1)
        dna_sequence = process_fasta(args.file)
        print(f"Loaded sequence from {args.file}: {dna_sequence[:50]}...")  # Print first 50 bases

    # Convert to Oiia sound
    dna_to_oiia(dna_sequence, args.output)
    print(f"Generated sound file: {args.output}")

if __name__ == "__main__":
    main()