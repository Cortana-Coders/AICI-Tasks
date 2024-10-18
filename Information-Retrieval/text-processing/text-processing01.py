import string
import pandas as pd
import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


text = "Saya sangat suka menonton film action, apalagi jika film tersebut dibintangi oleh saya sendiri yang dapat dipastikan menjadi terlihat keren dan menampakkan keseruan."


stemmer = StemmerFactory().create_stemmer()
text_stemmed = stemmer.stem(text)


remover = StopWordRemoverFactory().create_stop_word_remover()
text_clean = remover.remove(text_stemmed)


tokens = text_clean.split(' ')


print(f"Sebelum tokenization: {text_clean}")
print(f"Setelah tokenization: {tokens}")