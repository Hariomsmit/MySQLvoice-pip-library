import speech_recognition as SR
import MySQLvoice
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="Hariomsmit",
    database="mysqlvoice")
mycursor = mydb.cursor()
tablename = "empl"

rec = SR.Recognizer()
with SR.Microphone() as source:
    rec.adjust_for_ambient_noise(source)
    print("Please Speak what do you want from your Database:")
    audi = rec.listen(source)
    voicenote = rec.recognize_google(audi)
print("YOU SPOKE:\n", voicenote)
print(MySQLvoice.query(voicenote))
