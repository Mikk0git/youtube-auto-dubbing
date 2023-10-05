
def main():
    print("Youtube Auto Dubbing")

    try:
        srtFileDir = input("Enter the path of the srt file: ")
        srtFile = open(srtFileDir, "r")
    except FileNotFoundError:
        print("File not found")
        return

    generateAudio("C:\Users\Milan\Documents\projects\youtube-auto-dubbing\srt\[English] I Created Another App To REVOLUTIONIZE YouTube [DownSub.com].srt")


def generateAudio(srtFile):
    for line in srtFile:
        print(line)


main()
