# Metacademy Fortune
Generate fortune file from metacademy.org content in order to print a concept and summary when a new shell is started.
```
sudo apt-get install fortune
git clone --recursive git@github.com:joetoth/metacademy-fortune.git
python generate.py
sudo cp metacademy-fortune metacademy-fortune.dat /usr/share/games/fortunes/
echo fortune >> .bashrc
```
