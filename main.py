
def main():
    print("Youtube Auto Dubbing")

    try:
        srtFileDir = input("Enter the path of the srt file: ")
        srtFile = open(srtFileDir, "r")
    except FileNotFoundError:
        print("File not found")
        return

    generateAudio(srtFile)


def generateAudio(srtFile):
    for line in srtFile:
        print(line)


main()
