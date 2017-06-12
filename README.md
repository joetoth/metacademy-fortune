# metacademy-fortune
Generate fortune file from metacademy.org content in order to print a concept and summary when a new terminal session is started.
```
git clone --recursive git@github.com:joetoth/metacademy-fortune.git
python generate.py
sudo cp metacademy-fortune metacademy-fortune.dat /usr/share/games/fortunes/
echo fortune >> .bashrc
```
