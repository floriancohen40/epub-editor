import customtkinter as ctk, os
from gui import *
from logic import *

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Modifier EBOOK")
    self.iconbitmap(get_assets_file_path("assets/icons/book.ico"))
    self.xml_file_path = "META-INF/container.xml"
    self.geometry("500x400")
    self.minsize(300, 400)

    # Configuration globale du thème
    ctk.set_appearance_mode("dark")  # Modes : "System" (par défaut), "Light", "Dark"
    ctk.set_default_color_theme("green")  # Thèmes : "blue", "green", "dark-blue"

    # Initialisation des composants
    self.styles = self.load_app_styles()
    self.file_selector = FileSelector(self, styles=self.styles, width=400, height=100)
    self.status_bar = StatusBar(self, styles=self.styles)
    self.title_input = TitleInput(self, styles=self.styles, width=400, height=100)
    self.modify_button = StyledButton(
        self,
        text="Modifier le EBOOK",
        command=self.modify_file,
        styles=self.styles
    )

    # Placement des widgets
    self.file_selector.pack(pady=(20, 10), padx=35)
    self.title_input.pack(pady=(10, 20), padx=35)
    self.modify_button.pack(pady=10, padx=10)
    self.status_bar.pack(side="bottom", fill="x")
    
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
    epub_path = self.file_selector.get_selected_file()
    
    if(not os.path.isfile(epub_path)):
      self.status_bar.set_status("Fichier introuvable.", error=True)
      self.file_selector.reset()
      return
    
    try:
      self.epub_file = EPUBFile(epub_path)
      epub_title = self.epub_file.get_title()
      
      if(epub_title):
        self.title_input.title.set(epub_title)
        self.title_input.set_state("normal")
        self.modify_button.set_state("normal")
        self.status_bar.set_status('')
    except FileNotFoundError:
      self.status_bar.set_status("Vérifiez le format du fichier.", error=True)
      self.file_selector.reset()
    except:
      self.status_bar.set_status("Impossible de selectionner ce fichier.", error=True)
      self.file_selector.reset()
      return

  def modify_file(self):
    epub_path = self.file_selector.get_selected_file()
    title = self.title_input.get_title()
    
    if not epub_path:
      self.status_bar.set_status("Veuillez sélectionner un fichier EPUB.", error=True)
      return
    
    if not title or title == "":
      self.status_bar.set_status("Veuillez entrer un nouveau titre.", error=True)
      return
    
    try:
      self.update_epub_title(epub_path, title)
    except Exception as e:
      self.status_bar.set_status(f"Erreur : {e}", error=True)
          
  def update_epub_title(self, epub_path, title):
    if(not os.path.isfile(epub_path)):
      self.status_bar.set_status("Fichier introuvable.", error=True)
      return
    
    try:
      if(not self.epub_file):
        self.epub_file = EPUBFile(epub_path)
      self.epub_file.set_title(title)
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
