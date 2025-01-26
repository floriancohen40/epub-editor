import customtkinter as ctk
from tkinter import filedialog
from .buttons import StyledButton
from ..event_emiter import EventEmiter

class FileSelector(ctk.CTkFrame):
    def __init__(self, parent, styles: dict = {}, **kwargs):
        super().__init__(parent, **kwargs)
        self.file_path = ctk.StringVar(self, "[Choisir un fichier]")
        self.styles = styles
        self.event = EventEmiter()
        
        self.pack_propagate(0)

        # Label
        self.frame_title = ctk.CTkLabel(self, text="Sélectionnez un fichier EPUB")
        self.frame_title.pack(pady=5)

        # Champ d'entrée
        self.label = ctk.CTkLabel(self, textvariable=self.file_path, width=250, text_color="white", font=ctk.CTkFont(slant="italic"), anchor="w")
        self.label.pack(side="right", padx=(15, 5), pady=(0, 15))

        # Bouton "Parcourir"
        self.browse_button = StyledButton(self, text="Parcourir", command=self.browse_file, styles=self.styles)
        self.browse_button.pack(side="left", padx=(15, 5), pady=(0, 15))

    def browse_file(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier EPUB."""
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers EPUB", "*.epub")])
        if file_path:
            self.file_path.set(file_path)
            self.label.configure(font=ctk.CTkFont(slant="roman"))
            self.event.trigger('file_selected')

    def get_selected_file(self):
        """Retourne le chemin du fichier sélectionné."""
        return self.file_path.get()
      
    def reset(self):
      self.file_path.set("")
