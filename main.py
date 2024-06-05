from tiktok_uploader.upload import upload_video
import time
import os
from datetime import datetime


def upload():
    output_file = create_output_file()
    cookie_files = os.listdir("cookies")
    video_files = [file for file in os.listdir("videos") if not file.startswith(".")]
    index = 0

    for cookie_file in cookie_files:
        video_file = video_files[index % len(video_files)]
        if cookie_file.endswith(".txt"):
            print("Uploading video for account", cookie_file)
            upload_video(
                f"videos/{video_file}",
                description="Euro 2024 is coming!",
                song_keywords="BAND4BAND Central Cee & Lil Baby",
                sound_title="BAND4BAND",
                artist_name="Central Cee & Lil Baby",
                cookies=f"cookies/{cookie_file}",
                browser="chrome",
                headless=False,
            )
            append_tiktok_profile_to_output_file(output_file, cookie_file)
            index += 1


def create_output_file():
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{date_time}_upload_log.txt"
    with open(filename, "w") as f:
        pass
    return filename


def append_tiktok_profile_to_output_file(filename, cookie_file):
    with open(filename, "a") as f:
        filename = os.path.splitext(cookie_file)[0]
        tiktok_profile = f"https://www.tiktok.com/@{filename}"
        f.write(f"{tiktok_profile}\n")


if __name__ == "__main__":
    start_time = time.time()

    upload()

    execution_time = time.time() - start_time
    print(f"The execution time is {execution_time} seconds.")
