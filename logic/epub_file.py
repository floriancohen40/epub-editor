import xml.etree.ElementTree as ET, os
from .zip_handler import extract_file_from_zip, update_file_in_zip

class EPUBFile:
  def __init__(self, path):
    self.__namespaces = {
      "dc": "http://purl.org/dc/elements/1.1/",  # Namespace pour Dublin Core
      "opf": "http://www.idpf.org/2007/opf",
      "container": "urn:oasis:names:tc:opendocument:xmlns:container"
    }
    self.__title_xpath = ".//opf:metadata/dc:title"
    self.__rootfile_xpath = ".//container:rootfile"
    self.__internal_container_path = "META-INF/container.xml"
    self.path = path
    self.__open()
    
  def __open(self):
    self.__extracted_container_path = extract_file_from_zip(self.path, self.__internal_container_path)
    self.__internal_opf_path = self.__find_node(self.__extracted_container_path, self.__rootfile_xpath).attrib['full-path']
    self.__extracted_opf_path = extract_file_from_zip(self.path, self.__internal_opf_path)
  
  def __find_node(self, xml_path, xpath):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    element = root.find(xpath, self.__namespaces)
  
    return element
  
  def __is_readonly(self):
    return not os.access(self.path, os.W_OK)
  
  def __get_permissions(self):
    return oct(os.stat(self.path).st_mode)[-3:]

  def __set_permissions(self, permissions):
    os.chmod(self.path, int(permissions, 8))
  
  def __unlock_file(self):
     self.__set_permissions("777")

  def get_title(self):
    return self.__find_node(self.__extracted_opf_path, self.__title_xpath).text

  def set_title(self, title):
      tree = ET.parse(self.__extracted_opf_path)
      root = tree.getroot()
      element = root.find(self.__title_xpath, self.__namespaces)
      if element is None:
          raise ValueError(f"L'élément '{self.__title_xpath}' n'existe pas dans le fichier XML.")
      element.text = title

      # Convertir l'arbre XML modifié en bytes
      xml_bytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)
      readonly = self.__is_readonly()
      if readonly:
          permissions = self.__get_permissions()
          self.__unlock_file()
      update_file_in_zip(self.path, self.__internal_opf_path, xml_bytes)
      if readonly:
          self.__set_permissions(permissions)
