Visit https://linuxjourney.com/the-shell. Read each of the 19 lessons carefully, answer the quizzes (lower right), and also do the exercises (upper right). Please document the questions and your answers, as well as the command line outputs of the exercises in a Markdown-formatted file linuxjourney.md and add it to this subfolder. Please remember that you can also document your command line outputs with verbatim code.

1)
Exercises:
$ date: Gibt das aktuelle Datum und die Uhrzeit aus, z. B.: Mon Oct 28 12:34:56 UTC 2024
$ whoami: Gibt den Namen des aktuellen Benutzers aus, z. B.: pete

Quiz:
Die Ausgabe wird Hello World sein.

2)
Quiz:
Der Befehl ist pwd.

3)
Exercises:
Der Befehl cd ohne jegliche Flags bringt dich in dein Home-Verzeichnis (z. B. /home/pete).

Quiz:
Der Befehl ist cd ..

4)
Exercises:
Der Befehl ls -R zeigt alle Dateien und Verzeichnisse rekursiv an, also inklusive der Inhalte von Unterverzeichnissen.
Der Befehl ls -r listet die Dateien und Verzeichnisse in umgekehrter Reihenfolge auf.
Der Befehl ls -t sortiert die Dateien und Verzeichnisse nach Änderungszeit und zeigt die neuesten zuerst an.

Quiz:
Das Flag ls -a zeigt alle Dateien, einschließlich der versteckten Dateien.

5)
Excercises:
$ touch mysuperduperfile
$ ls -l mysuperduperfile
$ touch mysuperduperfile
-rw-r--r-- 1 user group 0 Oct 28 12:50 mysuperduperfile

Quiz:
touch myfile

6)
Exercises:
$ file banana.jpg
banana.jpg: JPEG image data, JFIF standard 1.01

Quiz:
Der Befehl ist file

7)
Exercises:
$ cat dogfile
$ cat dogfile birdfile
This is a dog. This is a bird.

Quiz:
Der Befehl ist cat

8)
Exercises:
$ less /home/pete/Documents/text1
Tasten Page Up und Page Down, um durch die Datei zu navigieren.
Tasten ↑ und ↓
/Beispiel (specific Word)

Quiz:
Der Befehl ist q

9)
Ctrl + R
1  ls
2  cd /home/pete
3  cat file1
4  touch newfile
   
Quiz:
Der Befehl ist clear

10)
Exercises:
Quiz:
Der Befehl ist -r

11)
Exercises:
$ mv oldname.txt newname.txt
$ mv newname.txt /home/pete/Documents

Quiz:
Befehlt lautet mv cat dog

12)
Exercises:
$ mkdir music videos
$ mv song.mp3 music/
$ mv movie.mp4 videos/

Quiz:
Befehl lautet mkdir

13)
Exercises:
$ touch -- -file
$ rm -- -file

Quiz:
Befehl lautet rm myfile

14)
Exercises:
$ find / -name "*net*"

Quiz:
Befehl lautet -name

15)
Exercises:
$ help echo
$ help logout
$ help pwd

Quiz:
Befehl ist help 

16)
Exercises:
$ man ls

Quiz:
Befehl lauter man

17)
Exercises:
$ whatis less

Quiz:
Befehl lautet whatis

18)
Exercises:
$ alias ll='ls -l'
$ alias gs='git status'
$ unalias ll
$ unalias gs

Quiz:
Befehl ist alias

19)
Exercises:
Terminal-Sitzung wird beendet

Quiz:
Befehl lautet exit
