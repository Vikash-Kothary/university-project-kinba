DIRECTORY="myrobotlab"
FILENAME="myrobotlab.jar"
java -jar "$DIRECTORY/$FILENAME" -service gui GUIService webgui WebGui python Python -invoke python execFile ../main/main.py
