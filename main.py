import re
from gtts import gTTS


def main():
    print("Youtube Auto Dubbing")

    try:
        srtFileDir = input("Enter the path of the srt file: ")
        # srtFileDir = 'C:\Users\Milan\Documents\projects\youtube-auto-dubbing\srt\[English] I Created Another App To REVOLUTIONIZE YouTube [DownSub.com].srt'
        srtFile = open(srtFileDir, "r")
    except FileNotFoundError:
        print("File not found")
        return

    audioList = makeAudioList(srtFile)
    # print(audioList)

    # Gtts
    generateAudio(audioList, "en")


def makeAudioList(srtFile):
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

            tts = gTTS(audio["text"])
            tts.save(f"audio/{index}.mp3")
            print(f"{index}/{len(audioList)-1}")
            index += 1
    return audioList


main()
