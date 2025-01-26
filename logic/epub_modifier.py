import xml.etree.ElementTree as ET

namespaces = {
    "dc": "http://purl.org/dc/elements/1.1/",  # Namespace pour Dublin Core
    "opf": "http://www.idpf.org/2007/opf"
}
xpath = ".//opf:metadata/dc:title"

def get_epub_title(xml_path,):
  tree = ET.parse(xml_path)
  root = tree.getroot()
  element = root.find(xpath, namespaces)
  
  return element.text

def modify_epub_title(xml_path, title):
    """Modifie un fichier XML selon les instructions spécifiées.
    
    Args:
        xml_path (str): Chemin vers le fichier XML.
        modifications (dict): Dictionnaire des modifications à effectuer.
            Exemple : {"Tag/Element": "Nouvelle valeur"}
    
    Returns:
        bytes: Contenu XML modifié en format bytes.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    element = root.find(xpath, namespaces)
    if element is None:
        raise ValueError(f"L'élément '{xpath}' n'existe pas dans le fichier XML.")
    element.text = title

    # Convertir l'arbre XML modifié en bytes
    xml_bytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return xml_bytes
