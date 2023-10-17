import os

def create_folders():
    parent_dir = './clients'
    folder_names = [
        'Abc',
        'Cba',
        'Bca']

    # Check if the parent directory exists, create it if not
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    # Create folders with the specified names inside the parent directory
    for folder in folder_names:
        folder_path = os.path.join(parent_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder {folder_path} already exists")

if __name__ == '__main__':
    create_folders()