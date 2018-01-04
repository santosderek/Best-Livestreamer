# Best-Livestreamer

---

[FFMPEG]

To convert .ts to .mkv use ffmpeg:

ffmpeg -i LiveStream.ts -vcodec copy -qscale 0 -acodec copy -f matroska outputStream.mkv
