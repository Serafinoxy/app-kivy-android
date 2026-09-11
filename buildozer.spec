[app]

# Titolo dell'applicazione
title = [app]

title = HelloKivy
package.name = hellokivy
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Livello 2: Aggiungiamo Kivy al motore Python
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Nome del pacchetto
package.name = hellokivy

# Dominio del pacchetto
package.domain = org.example

# Cartella di origine del codice sorgente
source.dir = .

# Estensioni dei file da includere nel pacchetto
source.include_exts = py,png,jpg,kv,atlas

# Versione dell'applicazione
version = 0.1

# Requisiti ridotti al solo Python per il test incrementale
requirements = python3

# Orientamento dello schermo
orientation = portrait

# Modalità schermo intero (0 = disattivato, 1 = attivato)
fullscreen = 0

# Configurazione specifica per Android
android.api = 33
android.minapi = 21

# Versione NDK stabile e compatibile
android.ndk = 25b

# Accettazione automatica delle licenze SDK di Google
android.accept_sdk_license = True
