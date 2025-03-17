from dna2oiia.converter import dna_to_oiia
import os

def test_dna_to_oiia():
    test_file = "test_output.wav"
    dna_to_oiia("ATCG", output_file=test_file)
    
    assert os.path.exists(test_file), "Output file not generated!"
    
    # Verify the output file size is non-zero
    assert os.path.getsize(test_file) > 0, "Output file is empty!"
    
    # Cleanup
    os.remove(test_file)
def test_dna_to_oiia_empty_sequence():
    test_file = "test_empty.wav"
    dna_to_oiia("", output_file=test_file)

    # The function should either not generate a file or create an empty one
    assert not os.path.exists(test_file) or os.path.getsize(test_file) == 0, "Unexpected output for empty sequence"

    # Cleanup if necessary
    if os.path.exists(test_file):
        os.remove(test_file)