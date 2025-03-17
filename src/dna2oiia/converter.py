from pydub import AudioSegment
import importlib.resources

def process_fasta(fasta_file):
    """Reads a FASTA file and extracts multiple DNA sequences."""
    sequences = {}
    current_header = None
    current_sequence = []

    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_header:
                    sequences[current_header] = "".join(current_sequence)
                current_header = line[1:]  # Remove ">" from header
                current_sequence = []
            else:
                current_sequence.append(line)

        # Add the last sequence
        if current_header:
            sequences[current_header] = "".join(current_sequence)

    return sequences

# Load oiia.wav from the installed package
def get_oiia_audio():
    with importlib.resources.path("dna2oiia.data", "oiia.wav") as audio_path:
        return AudioSegment.from_wav(str(audio_path))

# Define slicing positions (manual or using silence detection)
DNA_TO_SOUND = {}

def dna_to_oiia(dna_sequences, output_prefix="dna_oiia"):
    """
    Convert DNA sequences to 'oiia' sound sequences.

    Parameters:
    dna_sequences (dict): A dictionary mapping sequence headers to DNA sequences.
    output_prefix (str): Prefix for the output WAV files.
    """
    # Lazy-load oiia_audio
    if not DNA_TO_SOUND:
        oiia_audio = get_oiia_audio()
        DNA_TO_SOUND.update({
            "A": oiia_audio[1600:1742],    # "o"
            "T": oiia_audio[1793:1895], # "ii"
            "C": oiia_audio[2003:2211], # "a"
            "G": oiia_audio[2220:2303]  # "e"
        })

    for header, dna_sequence in dna_sequences.items():
        tones = [DNA_TO_SOUND[base] for base in dna_sequence.upper() if base in DNA_TO_SOUND]

        if tones:
            output_sound = sum(tones)
            output_file = f"{output_prefix}_{header}.wav"
            output_sound.export(output_file, format="wav")
            print(f"Audio saved as {output_file}")
        else:
            print(f"No valid DNA sequence found for {header}!")

# Example usage
if __name__ == "__main__":
    test_fasta = "example.fasta"
    sequences = process_fasta(test_fasta)
    dna_to_oiia(sequences)