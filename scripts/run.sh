DIRECTORY="myrobotlab"
FILENAME="myrobotlab.jar"
java -jar "$DIRECTORY/$FILENAME" -service gui GUIService python Python -invoke python execFile ../main/speech.py
