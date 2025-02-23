import os

link = input("Enter the video link: ")
command = f"yt-dlp -f best {link}"

confirm = input(f"Run this command? (y/n): ").strip().lower()

if confirm == "y":
    try:
        os.system(command)
    except KeyboardInterrupt:
        print("\nDownload stopped.")
else:
    print("Download canceled.")