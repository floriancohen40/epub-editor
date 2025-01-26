import customtkinter as ctk

class WrappingLabel(ctk.CTkLabel):
  def __init__(self, parent, debug = False, **kwargs):
    super().__init__(parent, **kwargs)
    self.debug = debug
    self.bind('<Configure>', self.update_wrap)
  
  def update_wrap(self, event):
    self.configure(wraplength=self.winfo_width())