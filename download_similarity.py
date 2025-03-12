import gdown
import os

def download_similarity_file():
    # Google Drive File ID
    file_id = "1MHyqeQBEuZ2p44FdIH1dRxCMOFTFa14r"
    output_file = "similarity.pkl"

    # Check if file exists, if not, download it
    if not os.path.exists(output_file):
        print("Downloading similarity.pkl from Google Drive...")
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)
        print("Download complete!")
    else:
        print("Model file already exists!")

if __name__ == "__main__":
    download_similarity_file()
