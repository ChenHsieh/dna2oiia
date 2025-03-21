# DNA2oiia 🧬🎵🐱

**DNA2oiia** is a Python package that converts DNA sequences into sound using the "oiia" phonetics. It supports both command-line interface (CLI) and Python API usage, handling DNA input as either raw sequences or FASTA files with single or multiple sequences.

![DNA2Oiia Demo](demo.gif)

## 🚀 Getting started

### 📥 Installation
```bash
pip install git+https://github.com/ChenHsieh/DNA2oiia.git
# or
pipx install git+https://github.com/ChenHsieh/DNA2oiia.git
```

## 🛠️ CLI Usage

### Convert a DNA Sequence Directly

```bash
dna2oiia -s ATCGGATTA -o my_dna --format mp3
```

- Use `-s` or `--string` to pass a DNA sequence.
- The `-o` or `--output` flag specifies the output file name (default: `dna2oiia`).
- The `--format` flag specifies the output format (`wav` or `mp3`, default: `wav`).

### Convert a FASTA File

```bash
dna2oiia -f example.fasta -o fasta_output --format mp3
```

- Use `-f` or `--file` to provide a FASTA file.
- If the file contains **multiple sequences**, output files will be named:  
  - `fasta_output_sequence1.mp3`
  - `fasta_output_sequence2.mp3`
  - ...
- If `-o` is **not specified**, the default prefix is `dna2oiia`, so files will be named:
  - `dna_oiia_sequence1.mp3`
  - `dna_oiia_sequence2.mp3`

### 🔥 **Streaming Mode (No File Creation)**
You can stream the output audio directly instead of saving it to a file:

```bash
dna2oiia -s ATCGGATTA --stream --format wav
```

- The `--stream` flag outputs audio as an in-memory stream instead of writing to disk.
- Useful for real-time applications and integration with web services.

## 🧑‍💻 Python API Usage

You can also use `dna2oiia` as a Python library:

### Convert a Single Sequence
```python
from dna2oiia.converter import dna_to_oiia
dna_to_oiia({"example": "ATCGGATTA"}, "output")
```

### Convert a FASTA File with Multiple Sequences
```python
from dna2oiia.converter import dna_to_oiia, process_fasta

sequences = process_fasta("example.fasta")
dna_to_oiia(sequences, "output")  # Generates output_sequence1.wav, output_sequence2.wav...
```

### Stream Audio Directly (No File Creation)
```python
import io
from dna2oiia.converter import dna_to_oiia

output_buffer = io.BytesIO()
dna_to_oiia({"example": "ATCGGATTA"}, output_buffer)
output_buffer.seek(0)  # Ensure proper streaming

# Use output_buffer for real-time playback or streaming in web apps
```

## 🌐 Streamlit Web App

You can run a **Streamlit web app** to interactively input DNA sequences and generate audio.

### 🏗️ Install Streamlit
If you haven't installed Streamlit yet, add it to your environment:
```bash
pip install streamlit
```

### 🚀 Run the Web App
Navigate to the project directory and run:
```bash
streamlit run st_dna2oiia.py
```

This will open the web app in your default browser, where you can:
 - Enter a DNA sequence and generate sound.
 - Upload a FASTA file and process multiple sequences.
 - Stream and download the generated audio files.

## 🎉 Acknowledgments

This project was inspired by a conversation with my IOB friends Nathan and Ibukun during a hackathon trip. Their creative thinking sparked the idea of transforming DNA sequences into sound. Huge thanks for the inspiration!

## 🎶 Audio Source Attribution

The **"oiia"** sound used in this project was sourced from the following YouTube video:

[🔗 Original Video on YouTube](https://www.youtube.com/watch?v=1oKZFGLn02g)

The meme itself originates from viral internet content. This project does not claim ownership of the original meme audio but uses it under **fair use** for creative and educational purposes.
 
 ## TODO
 - 🌍 **Web Interface**: Refine the web app (Streamlit or Flet) user interface.
 - 📦 **PyPI Release**: Finalize documentation and publish to PyPI.

 ## 🤖 AI Assistance
  
 This project was developed with assistance from ChatGPT to improve code structure, refine documentation, and troubleshoot issues. ChatGPT was used as a tool to enhance productivity and streamline the development process.
 
 ## 📜 License
 This project is licensed under the MIT License.
 
 ## 🤝 Contributing
 Contributions are welcome! Feel free to open issues and pull requests.
