# YouTube Bass Cover No-Bass Remover

## 📖 Project Description
This program removes the bass sound from YouTube bass cover videos, allowing you to play along while viewing the original tablature from the video. It's designed to help bass players practice by playing along with real music tracks, without the original bass interfering.

## 🛠 Features
- Download bass cover videos from YouTube.
- Extract the audio and remove only the bass track while keeping vocals, drums, and other instruments.
- Recombine the video with the modified audio, creating a no-bass practice track with the original video’s tablature.

## 🔧 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/jinnyday0719/yt_mp4-bass-remover
   ```

2. Install the necessary dependencies:
   ```bash
   pip install yt_dlp
   pip install spleeter
   ```

## 🚀 Usage
1. Run the program and input the YouTube URL for the bass cover video:
   ```bash
   python main.py
   ```

2. The program will process the video, remove the bass sound, and save the new video file.

## 📝 Notes
- Ensure you have `ffmpeg` installed on your system.
- This tool is intended for practice purposes only.

## 🤝 Contributions
Feel free to submit issues or contribute to the project by making a pull request!
