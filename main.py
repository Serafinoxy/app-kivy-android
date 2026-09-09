"""
main.py

App Kivy minima di esempio. Sostituisci questo contenuto con il tuo
progetto reale: questo file serve solo a verificare che l'intera
catena (Windows -> GitHub -> compilazione -> APK) funzioni prima di
aggiungere la logica vera dell'app.
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class AppDiProva(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Ciao! L'app compilata funziona."))
        layout.add_widget(Button(text="Premi qui"))
        return layout


if __name__ == "__main__":
    AppDiProva().run()
