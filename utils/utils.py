import gdown
import zipfile
import os

def gdownload(output, url):
  gdown.download(url=url, output=output, fuzzy=True)

def load_test_images(dir='images', file='test_image.zip', 
                     gdive='https://drive.google.com/file/d/12CJkx7MeMXxYYV2RprTM-uMRBcNV2OqU/view?usp=sharing'):
    
    gdownload(file, gdive)
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(dir)
    
    os.remove(file)

def load_weights():
    gdownload(
        "best.pt",
        "https://drive.google.com/file/d/11qWfEky2ewFwO2NarjHSvA67zfV10PP1/view?usp=sharing"
    )