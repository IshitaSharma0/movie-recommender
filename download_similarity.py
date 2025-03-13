import os
import gdown
import pickle

# Google Drive file ID (Extract from your Google Drive link)
file_id = "1MHyqeQBEuZ2p44FdIH1dRxCMOFTFa14r"
output_path = "similarity.pkl"

# Download the file if it doesn't exist
if not os.path.exists(output_path):
    print("Downloading similarity.pkl from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)

# Load the file
with open(output_path, "rb") as f:
    similarity = pickle.load(f)

print("File loaded successfully!")

