# DNA2oiia 🧬🎵🐱
 
**DNA2oiia** is a Python package that converts DNA sequences into sound using the "oiia" phonetics. It supports both command-line interface (CLI) and Python API usage, handling DNA input as either raw sequences or FASTA files with single or multiple sequences.

## 🚀 Getting started

### 📥 Installation
 ```bash
 pip install git+https://github.com/ChenHsieh/DNA2oiia.git
 ```
## 🛠️ CLI Usage

### Convert a DNA Sequence Directly

```bash
dna2oiia -s ATCGGATTA -o my_dna
```

- Use `-s` or `--string` to pass a DNA sequence.
- The `-o` or `--output` flag specifies the output file name (default: `dna_oiia.wav`).

### Convert a FASTA File

```bash
dna2oiia -f example.fasta -o fasta_output
```

- Use `-f` or `--file` to provide a FASTA file.
- If the file contains **multiple sequences**, output files will be named:  
  - `fasta_output_sequence1.wav`
  - `fasta_output_sequence2.wav`
  - ...
- If `-o` is **not specified**, the default prefix is `dna_oiia`, so files will be named:
  - `dna_oiia_sequence1.wav`
  - `dna_oiia_sequence2.wav`

## 🧑‍💻 Python API Usage

You can also use `dna2oiia` as a Python library:

### Convert a Single Sequence
```python
from dna2oiia.converter import dna_to_oiia
dna_to_oiia({"example": "ATCGGATTA"}, "output.wav")
```

### Convert a FASTA File with Multiple Sequences
```python
from dna2oiia.converter import dna_to_oiia, process_fasta
sequences = process_fasta("example.fasta")
dna_to_oiia(sequences, "output")  # Generates output_sequence1.wav, output_sequence2.wav...
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
