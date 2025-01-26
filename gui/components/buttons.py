import customtkinter as ctk

class StyledButton(ctk.CTkButton):
    def __init__(self, parent, text, command=None, styles: dict={}, **kwargs):
        super().__init__(parent, text=text, command=command, **kwargs)
        default_styles = { "corner_radius": 8, "text_color": "white", "fg_color": "#1D3557", "hover_color": "#457B9D" }
        self.styles = styles.get("button", default_styles)
        self.configure(**self.styles)