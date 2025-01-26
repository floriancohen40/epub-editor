from gui.app import App

def main():
    """Point d'entrée de l'application."""
    try:
        # Démarre l'application CustomTkinter
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Une erreur critique est survenue : {e}")

if __name__ == "__main__":
    main()
