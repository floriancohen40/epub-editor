import customtkinter as ctk
from tkinter import filedialog
from .buttons import StyledButton
from .wrapping_label import WrappingLabel
from ..event_emiter import EventEmiter

class FileSelector(ctk.CTkFrame):
    def __init__(self, parent, styles: dict = {}, **kwargs):
        super().__init__(parent, **kwargs)
        self.file_path = ctk.StringVar(self, "[Choisir un fichier]")
        self.styles = styles
        self.event = EventEmiter()
        
        self.pack_propagate(0)

        self.frame_title = WrappingLabel(self, text="Sélectionnez un fichier EPUB")
        self.browse_button = StyledButton(self, text="Parcourir", command=self.browse_file, styles=self.styles, state="normal")
        self.label = WrappingLabel(self, textvariable=self.file_path, width=250, text_color="white", font=ctk.CTkFont(slant="italic"), anchor="w")

        self.frame_title.pack(pady=5, fill="x")
        self.browse_button.pack(side="left", padx=(10, 10), pady=(0, 15))
        self.label.pack(side="right", padx=(10, 10), pady=(0, 15))

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
