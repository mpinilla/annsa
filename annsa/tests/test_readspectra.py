import os
from annsa.annsa import read_spectrum


def test_read_spectrum1():
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), './data_folder/rocky_flats_spectra.spe')
    _ = read_spectrum(TESTDATA_FILENAME)
    pass


def test_read_spectrum2():
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), './data_folder/gadras_template.spe')
    _ = read_spectrum(TESTDATA_FILENAME, float)
    pass
