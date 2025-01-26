import customtkinter as ctk, os
from gui import *
from logic import *

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Modifier EBOOK")
    self.iconbitmap(get_assets_file_path("assets/icons/book.ico"))
    self.xml_file_path = "OEBPS/root.opf"
    self.geometry("500x400")

    # Configuration globale du thème
    ctk.set_appearance_mode("dark")  # Modes : "System" (par défaut), "Light", "Dark"
    ctk.set_default_color_theme("green")  # Thèmes : "blue", "green", "dark-blue"

    # Initialisation des composants
    self.styles = self.load_app_styles()
    self.file_selector = FileSelector(self, styles=self.styles, width=400, height=100)
    self.status_bar = StatusBar(self, styles=self.styles)
    self.title_input = TitleInput(self, styles=self.styles, width=400, height=100)

    # Placement des widgets
    self.file_selector.pack(pady=(20, 10))
    self.status_bar.pack(side="bottom", fill="x")
    self.title_input.pack(pady=(10, 20))
    
    # Bouton pour lancer la modification
    self.modify_button = StyledButton(
        self,
        text="Modifier le EBOOK",
        command=self.modify_file,
        styles=self.styles
    )
    self.modify_button.pack(pady=10)
    
    # Events
    self.file_selector.event.on("file_selected", self.on_file_selected)

  def load_app_styles(self):
    """Charge les styles depuis le fichier JSON."""
    styles_path = "assets/styles.json"
    try:
      return load_styles(styles_path)
    except FileNotFoundError:
      print("Fichier styles.json introuvable. Les styles par défaut seront utilisés.")
      return {}
  
  def on_file_selected(self):
    zip_path = self.file_selector.get_selected_file()
    
    if(not os.path.isfile(zip_path)):
      self.status_bar.set_status("Fichier introuvable.", error=True)
      self.file_selector.reset()
      return
    
    try:
      self.extracted_file_path = extract_file_from_zip(zip_path, self.xml_file_path)
      epub_title = get_epub_title(self.extracted_file_path)
      
      if(epub_title):
        self.title_input.title.set(epub_title)
    except FileNotFoundError:
      self.status_bar.set_status("Vérifiez le format du fichier.", error=True)
      self.file_selector.reset()
    except:
      self.status_bar.set_status("Impossible de selectionner ce fichier.", error=True)
      self.file_selector.reset()
      return

  def modify_file(self):
    """Logique pour modifier le fichier XML dans le ZIP."""
    zip_path = self.file_selector.get_selected_file()
    title = self.title_input.get_title()
    
    if not zip_path:
      self.status_bar.set_status("Veuillez sélectionner un fichier EPUB.", error=True)
      return
    
    if not title or title == "":
      self.status_bar.set_status("Veuillez entrer un nouveau titre.", error=True)
      return
    
    try:
      # Simuler l"appel de la logique de modification
      # Vous pouvez remplacer cela par un appel à zip_handler et xml_modifier
      # Exemple : modifier_xml_dans_zip(zip_path, xml_filename, modifications)
      self.update_epub_title(zip_path, title)
    except Exception as e:
      self.status_bar.set_status(f"Erreur : {e}", error=True)
          
  def update_epub_title(self, zip_path, title):
    xml_file_path = "OEBPS/root.opf"
    
    if(not os.path.isfile(zip_path)):
      self.status_bar.set_status("Fichier introuvable.", error=True)
      return
    
    try:
      if(not self.extracted_file_path):
        self.extracted_file_path = extract_file_from_zip(zip_path, xml_file_path)
      updated_content = modify_epub_title(self.extracted_file_path, title)
      update_file_in_zip(zip_path, xml_file_path, updated_content)
    except FileNotFoundError:
      self.status_bar.set_status("Vérifiez le format du fichier.", error=True)
      return
    except ValueError:
      self.status_bar.set_status("Erreur lors de la mise à jour du titre.", error=True)
      return
    except:
      self.status_bar.set_status("Erreur lors de la réécriture dans le fichier EPUB.", error=True)
      return

    self.status_bar.set_status("Modification réussie !", error=False)
      


if __name__ == "__main__":
  app = App()
  app.mainloop()
