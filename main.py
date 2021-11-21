import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def texttospeech(text,filename):
    alreadytext=str(text)
    language="hi"
    speech=gTTS(text=alreadytext,lang=language,slow=False)
    speech.save(filename)

def mergeaudio(audios):
    all=AudioSegment.empty()
    for i in audios:
        all+=AudioSegment.from_mp3(i)
    return all

def brakingAudioFile():
    audio=AudioSegment.from_mp3("railway.mp3")

    # 1st typical announcement
    start=88000
    finish=90200
    audiopro=audio[start:finish]
    audiopro.export("1.mp3",format="mp3")

    # 2 city name

    # 3 se chal kar
    start=91000
    finish=92200
    audiopro=audio[start:finish]
    audiopro.export("3.mp3",format="mp3")

    # 4 via city name

    # 5 ke raste 
    start=94000
    finish=95000
    audiopro=audio[start:finish]
    audiopro.export("5.mp3",format="mp3")

    # 6 to city

    # 7  ko jane vali gadi sankhya

    start=9000
    finish=98900
    audiopro=audio[start:finish]
    audiopro.export("7.mp3",format="mp3")

    # 8 train no. and name

    # 9 kuch hi samay me platform no.

    start=105500
    finish=108200
    audiopro=audio[start:finish]
    audiopro.export("9.mp3",format="mp3")

    # 10  platform no

    # 11 aa rahi he
    start=109000
    finish=112250
    audiopro=audio[start:finish]
    audiopro.export("11.mp3",format="mp3")


def announcement(filename):
    ann =pd.read_excel(filename)
    for index,item in ann.iterrows():
        texttospeech(item["from"], "2.mp3")
        texttospeech(item["via"], "4.mp3")
        texttospeech(item["to"], "6.mp3")
        texttospeech(item["train_no"]+""+item["train_name"], "8.mp3")
        texttospeech(item["platform"], "10.mp3")
        audios=[f"{i}.mp3" for i in range(1,12)]
        announce=mergeaudio(audios)
        announce.export(f"announce_{index+1}.mp3",format="mp3")
        
    

if __name__=="__main__":
    print("Collection Data .... ")
    brakingAudioFile()
    print("Making Announcement File ....")
    announcement("announce_hindi.xlsx")
    print("The New Announcement File has been created !!! ")