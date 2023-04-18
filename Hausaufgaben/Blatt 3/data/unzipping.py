import zipfile
INPUT = 'train.zip'
OUTPUT = ''
with zipfile.ZipFile(INPUT, 'r') as zip_ref:
    zip_ref.extractall(OUTPUT)
print(f'Extracted Successfully: {INPUT}')