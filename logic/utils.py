import logging, json

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


def load_styles(file_path) -> dict:
    """Charge un fichier JSON contenant les styles."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        raise FileNotFoundError(f"Erreur lors du chargement du fichier de styles : {e}")
