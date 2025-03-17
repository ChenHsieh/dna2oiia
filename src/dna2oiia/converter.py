from pydub import AudioSegment
import importlib.resources

def process_fasta(fasta_file):
    """Reads a FASTA file and extracts the DNA sequence."""
    with open(fasta_file, "r") as f:
        lines = f.readlines()
    dna_sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    return dna_sequence

# Load oiia.wav from the installed package
def get_oiia_audio():
    with importlib.resources.path("dna2oiia.data", "oiia.wav") as audio_path:
        return AudioSegment.from_wav(str(audio_path))

# Define slicing positions (manual or using silence detection)
DNA_TO_SOUND = {}

def dna_to_oiia(dna_sequence, output_file="dna_oiia.wav"):
    """
    Convert DNA sequence to an 'oiia' sound sequence.

    Parameters:
    dna_sequence (str): A string representing the DNA sequence (e.g., "AATTCCGG").
    output_file (str): The name of the output WAV file. Default is "dna_oiia.wav".
    """
    tones = []

    # Lazy-load oiia_audio
    if not DNA_TO_SOUND:
        oiia_audio = get_oiia_audio()
        DNA_TO_SOUND.update({
            "A": oiia_audio[1600:1742],    # "o"
            "T": oiia_audio[1793:1895], # "ii"
            "C": oiia_audio[2003:2211], # "a"
            "G": oiia_audio[2220:2303]  # "e"
        })


    for base in dna_sequence.upper():
        if base in DNA_TO_SOUND:
            tones.append(DNA_TO_SOUND[base])

    # Combine tones into a single audio file
    if tones:
        output_sound = sum(tones)
        output_sound.export(output_file, format="wav")
        print(f"Audio saved as {output_file}")
    else:
        print("No valid DNA sequence found!")

# Example usage
if __name__ == "__main__":
    test_dna = "aattccgg"
    dna_to_oiia(test_dna)