 # 🎵 DNA2oiia 🎵
 
 **DNA2oiia** is a fun and creative Python package that converts DNA sequences into sound, specifically using the "oiia" meme-inspired phonetics. It extracts phonetic sounds from an audio file (`oiia.wav`) and maps them to DNA bases (`A`, `T`, `C`, `G`), generating a unique auditory representation of genetic sequences.
 
 ## 🚀 Features
 - 🎼 Converts DNA sequences (`ATCG`) into audio using predefined phonetic sounds.
 - 📂 Supports input as strings or FASTA files.
 - 🔊 Uses real audio clips instead of synthetic sine waves.
 - 🛠️ Built with `pydub` and `ffmpeg` for audio processing.
 
 ## 📥 Installation
 First, install the package using `poetry`:
 
 ```bash
 poetry add dna2oiia
 ```
 
 Or install directly from GitHub (if not yet published on PyPI):
 
 ```bash
 git clone https://github.com/yourusername/DNA2oiia.git
 cd DNA2oiia
 poetry install
 ```
 
## 🛠️ Usage

### Convert a DNA Sequence Directly:

```bash
dna2oiia -s ATCGGATTA -o my_dna.wav
```

### Convert a FASTA File:

```bash
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
 
 ## 🧪 Running Tests
 Run unit tests using `pytest`:
 
 ```bash
 pytest tests/
 ```
 
 ## 🏗️ Next Steps
 - 🎤 **Tune Audio Processing**: Improve phoneme slicing to make the generated audio more natural.
 - 🌍 **Web Interface**: Build a simple web app (Streamlit) allowing users to input DNA and hear their sequence.
 - 📦 **PyPI Release**: Finalize documentation and publish to PyPI.
 - 🏆 **Community Engagement**: Create social media content and challenges for users to submit their DNA sounds.
 
 ## 🤖 AI Assistance
  
 This project was developed with assistance from ChatGPT to brainstorm ideas, improve code structure, refine documentation, and troubleshoot issues. ChatGPT was used as a tool to enhance productivity and streamline the development process.
 
 ## 📜 License
 This project is licensed under the MIT License.
 
 ## 🤝 Contributing
 Contributions are welcome! Feel free to open issues and pull requests.
