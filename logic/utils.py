import logging, json, sys, os

def log_error(message):
    """Enregistre un message d'erreur dans le log.
    
    Args:
        message (str): Message à enregistrer.
    """
    logging.basicConfig(
        filename="app.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.error(message)

def get_assets_file_path(file_path):
  if getattr(sys, 'frozen', False):  # Si l'application est en mode exécutable
    base_path = sys._MEIPASS  # Dossier temporaire où PyInstaller extrait les ressources
  else:
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
      
  return os.path.join(base_path, file_path)

def load_styles(file_path) -> dict:
    path = get_assets_file_path(file_path)
    
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        raise FileNotFoundError(f"Erreur lors du chargement du fichier de styles : {e}")
