import argparse
import os
from dna2oiia.converter import dna_to_oiia, process_fasta

def main():
    parser = argparse.ArgumentParser(description="Convert DNA sequences or FASTA files into Oiia sounds.")
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-s", "--string", type=str, help="DNA sequence to convert")
    input_group.add_argument("-f", "--file", type=str, help="Path to a FASTA file containing the DNA sequence")

    parser.add_argument("-o", "--output", type=str, default="output.wav", help="Output audio file name or prefix for multiple sequences")

    args = parser.parse_args()

    # Handle DNA sequence directly
    if args.string:
        dna_sequences = {"single_sequence": args.string.upper()}  # Wrap string input in a dictionary
        print(f"Processing DNA sequence: {args.string.upper()}")

    # Handle FASTA file input
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"Error: File '{args.file}' not found!")
            exit(1)
        dna_sequences = process_fasta(args.file)
        print(f"Loaded {len(dna_sequences)} sequences from {args.file}")

    # Convert to Oiia sound
    for header, sequence in dna_sequences.items():
        output_file = f"{args.output}_{header}.wav" if len(dna_sequences) > 1 else args.output
        dna_to_oiia(sequence, output_file)
        print(f"Generated sound file: {output_file}")

if __name__ == "__main__":
    main()