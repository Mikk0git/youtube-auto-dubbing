# Youtube Auto Dubbing
### WIP 👷‍♂️ 
##### Version: 1.1

### Simple tool for dubbing youtube videos with AI generatied voice


Project was inspired by ThioJoe's [Auto Synced & Translated Dubs](https://github.com/ThioJoe/Auto-Synced-Translated-Dubs) [🎥](https://youtu.be/uaHmtJrZRdM?si=bda32upN7QwT686V)
My version is more focused on simplicity and it doesn't require GCP or Azure API

## Usage

```
  -l <language>                    Target language (en, de, fr, es, it, pt, nl, pl, uk, ru, tr, ja, ko, zh)
  -s <subtitle directory>          Custom subtitles
  -a                               Audio only
```

## Setup

1. Clone repo

```bash
git clone git@github.com:Mikk0git/youtube-auto-dubbing.git
```

2. Download dependencies

```bash
pip install -r requirements.txt
```

3. Run

```python
python main.py <youtube link> -l <language>
```

## Requirements

- Python
  ```
  https://www.python.org/downloads/
  ```
- FFmpeg
  ```
  https://ffmpeg.org/download.html
  ```

## ToDO

- [ ] GUI
- [ ] 11Labs support
