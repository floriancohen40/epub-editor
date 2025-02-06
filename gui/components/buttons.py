import customtkinter as ctk
from typing import Literal

class StyledButton(ctk.CTkButton):
  def __init__(self, parent, text, command=None, styles: dict={}, state: Literal["normal", "disabled"]="disabled", **kwargs):
    super().__init__(parent, text=text, command=command, state=state, **kwargs)
    self.styles: dict = styles.get("button", {})
    initial_style = self.styles.get("disabled", {}) if(state == "disabled") else self.styles.get("normal", {})
    self.configure(**self.styles.get("common", {}))
    self.configure(**initial_style)
        
  def set_state(self, state: Literal["normal", "disabled"]):
    style = self.styles.get("disabled", {}) if(state == "disabled") else self.styles.get("normal", {})
    self.configure(state=state, **style)