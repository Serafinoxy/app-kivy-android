name: Compile Kivy Android

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del codice
        uses: actions/checkout@v4

      - name: Compilazione con Buildozer via Docker
        run: |
          docker run --rm \
            -v ${{ github.workspace }}:/home/user/hostcwd \
            kivy/buildozer:latest \
            android debug

      - name: Carica APK
        uses: actions/upload-artifact@v4
        with:
          name: kivy-apk
          path: bin/*.apk
