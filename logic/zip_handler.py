import zipfile
import os
import tempfile
import shutil

def extract_file_from_zip(zip_path, file_name):
    if not zipfile.is_zipfile(zip_path):
        raise ValueError("Le fichier spécifié n'est pas un fichier ZIP valide.")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        if file_name not in zip_ref.namelist():
            raise FileNotFoundError(f"{file_name} n'existe pas dans le ZIP.")
        
        temp_dir = tempfile.mkdtemp()
        zip_ref.extract(file_name, temp_dir)
        return os.path.join(temp_dir, file_name)

def update_file_in_zip(zip_path, file_name, new_content):
    temp_dir = tempfile.mkdtemp()
    temp_zip_path = os.path.join(temp_dir, "temp.zip")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with zipfile.ZipFile(temp_zip_path, 'w') as temp_zip:
            # Copier tous les fichiers sauf celui qu'on remplace
            for item in zip_ref.infolist():
                if item.filename != file_name:
                    temp_zip.writestr(item, zip_ref.read(item.filename))
            # Ajouter le fichier mis à jour
            temp_zip.writestr(file_name, new_content)

    shutil.move(temp_zip_path, zip_path)
    shutil.rmtree(temp_dir)
