import argparse
import os
import io
from dna2oiia.converter import dna_to_oiia, process_fasta

def main():
    parser = argparse.ArgumentParser(description="Convert DNA sequences or FASTA files into Oiia sounds.")
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-s", "--string", type=str, help="DNA sequence to convert")
    input_group.add_argument("-f", "--file", type=str, help="Path to a FASTA file containing one or more DNA sequences")

    parser.add_argument("-o", "--output", type=str, default=None, help="Output audio file name (optional). If multiple sequences in FASTA, filenames will include headers as suffixes.")
    parser.add_argument("--format", type=str, choices=["wav", "mp3"], default="wav", help="Output audio format (wav or mp3)")
    parser.add_argument("--stream", action="store_true", help="Stream the audio output instead of saving to a file")

    args = parser.parse_args()

    if args.string:
        dna_sequences = {"sequence": args.string.upper()}  # Single sequence case
        output_name = args.output if args.output else "dna_oiia"
    
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"Error: File '{args.file}' not found!")
            exit(1)
        dna_sequences = process_fasta(args.file)
        output_name = args.output  # If None, handled inside dna_to_oiia
    
    if args.stream:
        output_buffer = io.BytesIO()
        dna_to_oiia(dna_sequences, output_prefix=None, output_buffer=output_buffer, output_format=args.format)
        print("Audio streamed successfully.")
    else:
        dna_to_oiia(dna_sequences, output_name, output_format=args.format)

if __name__ == "__main__":
    main()