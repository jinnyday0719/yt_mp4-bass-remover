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

2. The program will process the video, remove the bass sound, and save the new video file with the original tablature visible.

## 📝 Notes
- Ensure you have `ffmpeg` installed on your system.
- This tool is intended for practice purposes only.

## 🤝 Contributions
Feel free to submit issues or contribute to the project by making a pull request!


# YouTube 베이스 커버 영상 베이스 제거 프로그램

## 📖 프로젝트 설명
이 프로그램은 유튜브에 있는 베이스 커버 영상에서 베이스 소리를 제거하여, 원래 영상에 있는 타브 악보를 보며 연주할 수 있게 만들어졌습니다. 이를 통해 베이스 연습 시 원곡의 다른 파트는 유지하면서 베이스만 제거된 상태에서 연습할 수 있습니다.

## 🛠 주요 기능
- 유튜브 베이스 커버 영상을 다운로드합니다.
- 오디오를 추출한 후 베이스 트랙만 제거하고, 보컬, 드럼, 기타 악기는 그대로 유지합니다.
- 수정된 오디오와 비디오를 다시 결합하여 타브 악보가 있는 연습용 영상을 생성합니다.

## 🔧 설치 방법
1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/jinnyday0719/yt_mp4-bass-remover
   ```

2. 필요한 의존성 패키지를 설치합니다:
   ```bash
   pip install yt_dlp
   pip install spleeter
   ```

## 🚀 사용 방법
1. 프로그램을 실행하고 베이스 커버 영상의 유튜브 URL을 입력합니다:
   ```bash
   python main.py
   ```

2. 프로그램은 영상을 처리하여 베이스 소리가 제거된 새 비디오 파일을 원래 타브 악보와 함께 저장합니다.

## 📝 참고 사항
- `ffmpeg`가 시스템에 설치되어 있어야 합니다.

## 🤝 기여
이슈를 제출하거나 풀 리퀘스트를 통해 프로젝트에 기여해 주시면 감사하겠습니다!
