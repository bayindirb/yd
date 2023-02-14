from pytube import YouTube

while True:
    link = input("Enter the youtube video link: ")
    try:
        yt = YouTube(link)
        break
    except Exception as e:
        print(f"An error occurred while creating the YouTube object: {e}")
        print("Please enter a valid link.")

try:
    yd = yt.streams.get_highest_resolution()
    yd.download(r"\Users\Bekir\Desktop")
except Exception as e:
    print(f"An error occurred while downloading the video: {e}")
    exit()

print()
print("########### Download Completed ###########")

q_to_quit = True

while q_to_quit:
    q_to_quit = input("Q to quit: ").upper()

    if q_to_quit == "Q":
        t = False
        exit()
