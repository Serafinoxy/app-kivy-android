name: Compile Kivy Android Native

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del codice
        uses: actions/checkout@v4

      - name: Configurazione Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Installazione dipendenze di sistema
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip openjdk-17-jdk python3-pip \
            autoconf libtool pkg-config zlib1g-dev \
            libncurses5-dev libncursesw5-dev \
            libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

      - name: Installazione Buildozer e Cython
        run: |
          pip install --upgrade pip
          pip install --user cython==0.29.33 buildozer

      - name: Compilazione APK con Buildozer
        run: |
          export PATH=$PATH:~/.local/bin
          buildozer -v android debug

      - name: Carica APK
        uses: actions/upload-artifact@v4
        with:
          name: kivy-apk
          path: bin/*.apk
