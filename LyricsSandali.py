import time
import sys

lyrics = [
    ("Kahit pa ang mundo ay gumuho", 0.60, 0.08),
    ("At ang kalangitan ay mahulog", 0.80, 0.08),
    ("'Di man alam ang gagawin", 1.0, 0.08),
    ("Sa 'yo pa rin, sa 'yo pa rin", 1.5, 0.08),
    ("Kahit araw at buwan ay magtalo", 0.50, 0.08),
    ("'Di magbabago aking pagsamo", 0.80, 0.08),
    ("Tanging hiling, tanging hiling", 0.80, 0.08),
    ("Ikaw ang aking huling sandali", 0.50, 0.08),
]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, post_line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(post_line_delay)

if __name__ == "__main__":
    print("Now playing: Sandali by Cup Of Joe\n")
    play_lyrics(lyrics)
