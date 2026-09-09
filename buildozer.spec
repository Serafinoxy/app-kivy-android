[app]

title = App Di Prova
package.name = appdiprova
package.domain = org.esempio

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# API e architetture target: valori aggiornati e ragionevoli per il 2026.
# Se in futuro Google Play richiede una API piu' recente, aggiorna qui.
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1
