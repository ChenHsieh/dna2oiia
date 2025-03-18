import streamlit as st
import io
from pydub import AudioSegment
from dna2oiia.converter import dna_to_oiia

def is_valid_dna(sequence):
    return all(base in "ATCG" for base in sequence.upper())

def main():
    st.markdown(
    """
    <style>
        .stApp {
            background: url("https://raw.githubusercontent.com/ChenHsieh/dna2oiia/main/oiia.gif") no-repeat center center fixed;
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title("🧬🎵🐱 DNA2Oiia - Convert DNA Sequences to Sound")
    
    # Text input for DNA sequence
    dna_sequence = st.text_area("Enter a DNA sequence (only A, T, C, G allowed):", "ATTCGATGTCGCTCGCT")
    
    # Filter invalid characters in real-time
    filtered_sequence = "".join([base for base in dna_sequence.upper() if base in "ATCG"])
    
    if dna_sequence != filtered_sequence:
        st.warning("Only A, T, C, and G are allowed. Invalid characters were removed.")
    
    if st.button("Generate Sound"):
        if not filtered_sequence:
            st.error("Please enter a valid DNA sequence.")
            return
        # Display the filtered sequence
        st.write("Filtered DNA Sequence:")
        st.code(filtered_sequence)
        
        
        # Convert DNA sequence to audio stream
        output_audio = io.BytesIO()
        dna_to_oiia({"input_sequence": filtered_sequence}, output_buffer=output_audio)
        output_audio.seek(0)  # Ensure the buffer is at the beginning
        
        # Convert output_audio into a valid WAV format
        audio_segment = AudioSegment.from_file(output_audio, format="wav")
        output_wav = io.BytesIO()
        audio_segment.export(output_wav, format="wav")
        output_wav.seek(0)
        
        # Play and download audio
        st.audio(output_wav, format="audio/wav")
        st.download_button("Download Audio", output_wav, file_name="dna_oiia.wav", mime="audio/wav")

if __name__ == "__main__":
    main()
