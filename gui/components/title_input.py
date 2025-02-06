import customtkinter as ctk
from .wrapping_label import WrappingLabel
from typing import Literal

class TitleInput(ctk.CTkFrame):
  def __init__(self, parent, styles: dict={}, state: Literal["normal", "disabled"] = "disabled", **kwargs):
    super().__init__(parent, **kwargs)
    self.title = ctk.StringVar()
    self.styles: dict = styles.get("entry")
    initial_style = self.styles.get("disabled", {}) if(state == "disabled") else self.styles.get("normal", {})
    
    self.pack_propagate(0)
    
    self.label = WrappingLabel(self, text="Saisissez le nouveau titre :")
    self.entry = ctk.CTkEntry(
      self, 
      textvariable=self.title, 
      state=state,
      width=250)
    self.entry.configure(**self.styles.get("common", {}))
    self.entry.configure(**initial_style)
    self.label.pack(pady=5, fill="x")
    self.entry.pack(pady=10, padx=10)
    
  def get_title(self):
    """Retourne le titre saisi."""
    return self.title.get()
  
  def set_state(self, state: Literal["normal", "disabled"]):
    style = self.styles.get("disabled", {}) if(state == "disabled") else self.styles.get("normal", {})
    self.entry.configure(state=state, **style)    
  
  def reset(self):
    self.title.set("")