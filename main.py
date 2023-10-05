import re
from gtts import gTTS
from googletrans import Translator


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
    print(audioList)
    return audioList


main()
