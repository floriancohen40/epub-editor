import customtkinter as ctk
from .wrapping_label import WrappingLabel

class TitleInput(ctk.CTkFrame):
  def __init__(self, parent, styles: dict={}, **kwargs):
    super().__init__(parent, **kwargs)
    self.title = ctk.StringVar()
    self.styles: dict = styles.get("entry")
    
    self.pack_propagate(0)
    
    self.label = WrappingLabel(self, text="Saisissez le nouveau titre :")
    self.entry = ctk.CTkEntry(
      self, 
      textvariable=self.title, 
      width=250,
      **self.styles)
    
    self.label.pack(pady=5, fill="x")
    self.entry.pack(pady=10, padx=10)
    
  def get_title(self):
    """Retourne le titre saisi."""
    return self.title.get()
  
  def reset(self):
    self.title.set("")