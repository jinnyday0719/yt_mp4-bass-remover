import os
import subprocess
import sys
import tempfile
import logging
from yt_dlp import YoutubeDL
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logging.error(f"명령 실행 오류: {command}")
        logging.error(stderr.decode())
        sys.exit(1)
    return stdout.decode()

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': output_path,
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            ydl.download([url])
            return info
    except Exception as e:
        logging.error(f"영상 다운로드 오류: {str(e)}")
        sys.exit(1)

def sanitize_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = re.sub(r'\s+', "_", filename)
    filename = filename.encode('ascii', 'ignore').decode('ascii')
    return filename[:200]

def is_youtube_url(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
    )
    return re.match(youtube_regex, url) is not None

def process_video(youtube_url):
    ffmpeg = 'ffmpeg'

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_video = os.path.join(temp_dir, "temp_video.mp4")
        temp_audio = os.path.join(temp_dir, "temp_audio.wav")
        separated_dir = os.path.join(temp_dir, "separated")

        logging.info("유튜브 영상 다운로드 중...")
        video_info = download_youtube_video(youtube_url, temp_video)

        video_title = video_info.get('title', '제목 없음')
        safe_title = sanitize_filename(video_title)

        logging.info("오디오 추출 중...")
        run_command(f'{ffmpeg} -i "{temp_video}" -vn -acodec pcm_s16le -ar 44100 -ac 2 "{temp_audio}"')

        logging.info("오디오 트랙 분리 중...")
        run_command(f'spleeter separate -p spleeter:4stems -o "{separated_dir}" "{temp_audio}"')

        track_name = os.path.splitext(os.path.basename(temp_audio))[0]
        vocals = os.path.join(separated_dir, track_name, "vocals.wav")
        drums = os.path.join(separated_dir, track_name, "drums.wav")
        other = os.path.join(separated_dir, track_name, "other.wav")

        logging.info("베이스 필터링 중...")
        temp_audio_no_bass = os.path.join(temp_dir, "temp_audio_no_bass.wav")
        bass_removal_filter = (
            "highpass=f=80,lowshelf=f=100:g=-12,equalizer=f=125:width_type=o:width=1:g=-10,"
            "equalizer=f=250:width_type=o:width=1:g=-8,equalizer=f=500:width_type=o:width=1:g=-6,"
            "loudnorm=I=-14:TP=-1:LRA=11"
        )
        run_command(f'{ffmpeg} -i "{vocals}" -i "{drums}" -i "{other}" '
            f'-filter_complex "[0:a][1:a][2:a]amix=inputs=3:duration=longest,{bass_removal_filter}" '
            f'-ar 44100 -ac 2 "{temp_audio_no_bass}"')

        logging.info("파일 결합 중...")
        output_video = os.path.join(os.getcwd(), f"{safe_title}_no_bass.mp4")
        
        if os.path.exists(output_video):
            os.remove(output_video)
        
        run_command(f'{ffmpeg} -i "{temp_video}" -i "{temp_audio_no_bass}" '
                    f'-c:v copy -c:a aac -b:a 320k '
                    f'-map 0:v:0 -map 1:a:0 "{output_video}"')

    logging.info(f"처리 완료. 저장 위치: {output_video}")

def main():
    while True:
        youtube_url = input("유튜브 URL을 입력하세요 (종료하려면 엔터): ").strip()
        if youtube_url == "":
            print("프로그램을 종료합니다.")
            break
        if is_youtube_url(youtube_url):
            process_video(youtube_url)
        else:
            print("유효하지 않은 URL입니다.")

if __name__ == "__main__":
    main()
