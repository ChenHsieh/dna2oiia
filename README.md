# 🎵 DNA2oiia 🎵
 
 **DNA2oiia** is a fun Python package that converts DNA sequences into sound, specifically using the "oiia" meme-inspired phonetics. It extracts phonetic sounds from an audio file (`oiia.wav`) and maps them to DNA bases (`A`, `T`, `C`, `G`), generating a unique auditory representation of genetic sequences.
 
## 🚀 Getting started

### 📥 Installation
 ```bash
 pip install git+https://github.com/ChenHsieh/DNA2oiia.git
 ```
 
## 🛠️ CLI Usage

```bash
# Convert a DNA Sequence Directly:
dna2oiia -s ATCGGATTA -o my_dna.wav
# Convert a FASTA File:
dna2oiia -f example.fasta -o fasta_output.wav

```
	•	Use -s or --string to pass a DNA sequence.
	•	Use -f or --file to provide a FASTA file path.
	•	The -o or --output flag specifies the output audio file (default: output.wav).

### python API

 ```python
 from dna2oiia.converter import dna_to_oiia
 
 # Convert a DNA sequence into sound
 dna_to_oiia("ATCGGATTA", output_file="output.wav")
 ```
 
 To process a FASTA file:
 ```python
 from dna2oiia.converter import process_fasta
 
 dna_seq = process_fasta("example.fasta")
 dna_to_oiia(dna_seq, output_file="output.wav")
 ```
 
## 🎶 Audio Source Attribution

The **"Oiia"** sound used in this project was sourced from the following YouTube video:

[🔗 Original Video on YouTube](https://www.youtube.com/watch?v=1oKZFGLn02g)

The meme itself originates from viral internet content. This project does not claim ownership of the original meme audio but uses it under **fair use** for creative and educational purposes.
 
 ## TODO
 - 🌍 **Web Interface**: Build a simple web app (Streamlit or Flet) allowing users to input DNA and hear their sequence.
 - 📦 **PyPI Release**: Finalize documentation and publish to PyPI.

 ## 🤖 AI Assistance
  
 This project was developed with assistance from ChatGPT to improve code structure, refine documentation, and troubleshoot issues. ChatGPT was used as a tool to enhance productivity and streamline the development process.
 
 ## 📜 License
 This project is licensed under the MIT License.
 
 ## 🤝 Contributing
 Contributions are welcome! Feel free to open issues and pull requests.
