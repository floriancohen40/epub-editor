import customtkinter as ctk
from .wrapping_label import WrappingLabel

class StatusBar(ctk.CTkFrame):
    def __init__(self, parent, styles: dict = {}):
        super().__init__(parent)
        self.styles: dict = styles.get("label", {})
        self.message = ctk.StringVar()
        self.configure(height=30)

        # Label pour afficher les messages
        self.label = WrappingLabel(self, textvariable=self.message, anchor="center")
        self.label.pack(fill="x", padx=10)

    def set_status(self, message, error=False):
        """Met à jour le message de statut.
        
        Args:
            message (str): Le message à afficher.
            error (bool): Si vrai, affiche le message en rouge.
        """
        self.message.set(message)
        color = self.styles.get("error", "red") if error else self.styles.get("success", "green")
        self.label.configure(text_color=color)
    
    def reset(self):
      self.message.set("")
