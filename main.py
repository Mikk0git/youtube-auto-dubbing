import re
import os
from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment


def main():
    print("Youtube Auto Dubbing")

    try:
        srtFileDir = input("Srt File Path: ")
        srtFile = open(srtFileDir, "r")
    except FileNotFoundError:
        print("File not found")
        return
    lang = input("Target Language: ")
    if not lang in ["", "en", "de", "fr", "es", "it", "pt", "nl", "pl", "ru", "tr", "ja", "ko", "zh"]:
        print("Language not supported")
        print("Supported languages: en, de, fr, es, it, pt, nl, pl, ru, tr, ja, ko, zh")
        return
    if lang == "":
        lang = "en"

    # Read srt file
    audioList = makeAudioList(srtFile)

    # Translate
    translateAudioList(audioList, lang)

    # Gtts
    generateAudio(audioList, lang)

    # Matching
    matchingAudioToTime(audioList)


def makeAudioList(srtFile):
    print("Reading srt file...")
    audioList = []
    # First item is left empty
    audioList.append("nothing")

    i = 1
    for line in srtFile:

        line = line.strip()

        if line == f"{i}":
            index = i
            audioList.append({})

            i += 1

        elif re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line):
            start = line[:12]
            end = line[17:]

            audioList[index]["start"] = start
            audioList[index]["end"] = end

        elif len(line) > 0:

            audioList[index]["text"] = line

    return audioList


def generateAudio(audioList, lang):
    print("Generating audio...")
    index = 1
    for audio in audioList:
        if audio != "nothing":

            tts = gTTS(audio["text"], lang=lang)
            tts.save(f"audio/{index}.mp3")
            mp3ToWav(f"audio/{index}.mp3")
            print(f"{index}/{len(audioList)-1}")
            index += 1
    return audioList


def translateAudioList(audioList, lang):
    print("Translating audio...")
    index = 1
    translator = Translator()
    for audio in audioList:
        if audio != "nothing":
            audio["text"] = translator.translate(audio["text"], dest=lang).text

            print(f"{index}/{len(audioList)-1}")
            index += 1
    return audioList


def matchingAudioToTime(audioList):
    print("Matching audio to time...")
    index = 1
    for audio in audioList:
        if audio != "nothing":
            print(audio)
            start = ((int(audio["start"][:2])*3600) +
                     (int(audio["start"][3:5]) * 60) +
                     int(audio["start"][6:8]) +
                     float("0." + audio["start"][9:12]))

            end = ((int(audio["end"][:2])*3600) +
                   (int(audio["end"][3:5]) * 60) +
                   int(audio["end"][6:8]) +
                   float("0." + audio["end"][9:12]))

            desiredDuration = end - start
            print(f"desiredDuration: {desiredDuration}")

            audioFile = AudioSegment.from_file(f"audio/{index}.wav")

            audioDuration = len(audioFile) / 1000.0
            print("audioDuration: ", audioDuration)
            ratio = desiredDuration/audioDuration
            print(f"Ratio: {ratio}")

            # This is not working
            # Another solution for changing speed needed
            audioFile = audioFile.speedup(playback_speed=ratio)
            audioFile.export(f"audio/{index}.wav", format="wav")

            print(f"{index}/{len(audioList)-1}")
            index += 1


def mp3ToWav(audioDIrMp3):
    audio = AudioSegment.from_mp3(audioDIrMp3)
    audioDIrWav = audioDIrMp3.replace(".mp3", ".wav")
    audio.export(audioDIrWav, format="wav")
    os.remove(audioDIrMp3)


main()
