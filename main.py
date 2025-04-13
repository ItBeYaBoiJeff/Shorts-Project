##IMPORT EVERYTHING
import random
from moviepy import *
from PIL import Image
import cv2
import os
from glob import glob
from gtts import gTTS


##VARIABLES
repeat = 1
inputBlank = 0


##DELETE OLD FILES4
if os.path.exists("./output/frames/output.mp4"):
    os.remove("./output/frames/output.mp4")
if os.path.exists("./output/frames/output1.png"):
    os.remove("./output/frames/output1.png")
if os.path.exists("./output/frames/output2.png"):
    os.remove("./output/frames/output2.png")
if os.path.exists("./output/frames/output3.png"):
    os.remove("./output/frames/output3.png")
if os.path.exists("./assets/audio/voices/wyr1tts.mp3"):
    os.remove("./assets/audio/voices/wyr1tts.mp3")
if os.path.exists("./assets/audio/voices/wyr2tts.mp3"):
    os.remove("./assets/audio/voices/wyr2tts.mp3")
if os.path.exists("./assets/audio/voices/wyr3tts.mp3"):
    os.remove("./assets/audio/voices/wyr3tts.mp3")


##FRAME 1
direct = "./assets/image bank/frame 1/"
wyr_red = Image.open("./assets/image bank/nuhuh.jpg")
wyr_blue = Image.open(f"./assets/image bank/nuhuh.jpg")
image_1 = random.randint(0,9)
image_2 = random.randint(0,9)
if image_1 == image_2:
    image_2 = abs(image_2 - 1)
wyr1_list = [f"{direct}caseoh.jpg", f"{direct}dafuqboom.jpg", f"{direct}dharman.jpg", f"{direct}lankybox.jpg", f"{direct}mrbeast.jpg", f"{direct}nickheh30.jpg", f"{direct}ninja.jpg", f"{direct}rainbolt.jpg", f"{direct}sypherPK.jpg", f"{direct}xQc.jpg"]
wyr_red = Image.open(f"{wyr1_list[image_1]}")
wyr_blue = Image.open(f"{wyr1_list[image_2]}")
background = Image.open(f"./assets/image bank/BG.jpg")
background.paste(wyr_red, (10,12))
background.paste(wyr_blue, (10,866))
background.save(format="PNG", fp = "./output/frames/output1.png")
aiClip = wyr1_list[image_1].split("/")
aiClip = aiClip[4].split(".")
aiClip1 = aiClip[0]
aiClip = wyr1_list[image_2].split("/")
aiClip = aiClip[4].split(".")
aiClip2 = aiClip[0]


##FRAME 2
direct = "./assets/image bank/frame 2/"
wyr_red = Image.open(f"./assets/image bank/nuhuh.jpg")
wyr_blue = Image.open(f"./assets/image bank/nuhuh.jpg")
image_1 = random.randint(0,6)
image_2 = random.randint(0,6)
if image_1 == image_2:
    image_2 = abs(image_2 - 1)
wyr1_list = [f"{direct}bigmac.jpg", f"{direct}chickennugget.jpg", f"{direct}cocacola.jpg", f"{direct}drpepper.jpg", f"{direct}mountaindew.jpg", f"{direct}pizza.jpg", f"{direct}whopper.jpg"]
wyr_red = Image.open(f"{wyr1_list[image_1]}")
wyr_blue = Image.open(f"{wyr1_list[image_2]}")
background = Image.open(f"./assets/image bank/BG.jpg")
background.paste(wyr_red, (10,12))
background.paste(wyr_blue, (10,866))
background.save(format="PNG", fp = "./output/frames/output2.png")
aiClip = wyr1_list[image_1].split("/")
aiClip = aiClip[4].split(".")
aiClip3 = aiClip[0]
aiClip = wyr1_list[image_2].split("/")
aiClip = aiClip[4].split(".")
aiClip4 = aiClip[0]


##FRAME 3
direct = "./assets/image bank/frame 3/"
wyr_red = Image.open("./assets/image bank/nuhuh.jpg")
wyr_blue = Image.open(f"./assets/image bank/nuhuh.jpg")
image_1 = random.randint(0,8)
image_2 = random.randint(0,8)
if image_1 == image_2:
    image_2 = abs(image_2 - 1)
wyr1_list = [f"{direct}baconhair.jpg", f"{direct}cameraman.jpg", f"{direct}caseoh2.jpg", f"{direct}goku.jpg", f"{direct}jackblack.jpg", f"{direct}ninja.jpg", f"{direct}omniman.jpg", f"{direct}peely.jpg", f"{direct}skibiditoilet.jpg"]
wyr_red = Image.open(f"{wyr1_list[image_1]}")
wyr_blue = Image.open(f"{wyr1_list[image_2]}")
background = Image.open(f"./assets/image bank/BG.jpg")
background.paste(wyr_red, (10,12))
background.paste(wyr_blue, (10,866))
background.save(format="PNG", fp = "./output/frames/output3.png")
aiClip = wyr1_list[image_1].split("/")
aiClip = aiClip[4].split(".")
aiClip5 = aiClip[0]
aiClip = wyr1_list[image_2].split("/")
aiClip = aiClip[4].split(".")
aiClip6 = aiClip[0]


##FRAMES TO NO AUDIO MP4
fps = 1
image_folder = "./output/frames"
output_video = "./output/frames/output.mp4"
images = sorted(glob(os.path.join(image_folder, '*.png')))
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(1, images[0])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(11, images[10])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
images.insert(21, images[20])
frame = cv2.imread(images[0])
height, width, layers = frame.shape
frame_size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, fps, frame_size)
for img_path in images:
    frame = cv2.imread(img_path)
    video.write(frame)
video.release()


##AI VOICES
ttsClip1 = gTTS(f"Would you rather: Become {aiClip1} for a month or {aiClip2} for a month")
ttsClip1.save("./assets/audio/voices/wyr1tts.mp3")
ttsClip2 = gTTS(f"Would you rather: Get unlimited {aiClip3} or get unlimited {aiClip4}")
ttsClip2.save("./assets/audio/voices/wyr2tts.mp3")
ttsClip3 = gTTS(f"Would you rather: Fight {aiClip5} or fight {aiClip6}")
ttsClip3.save("./assets/audio/voices/wyr3tts.mp3")


##DEFINING MOVIEPY CLIPS
wyr1 = VideoFileClip("./output/frames/output.mp4").subclipped(0, 10)
wyr2 = VideoFileClip("./output/frames/output.mp4").subclipped(10, 20)
wyr3 = VideoFileClip("./output/frames/output.mp4").subclipped(20, 30)
wyr1_tts = AudioFileClip("./assets/audio/voices/wyr1tts.mp3")
wyr2_tts = AudioFileClip("./assets/audio/voices/wyr2tts.mp3")
wyr3_tts = AudioFileClip("./assets/audio/voices/wyr3tts.mp3")
wyr1_music = AudioFileClip("./assets/audio/music/geodashmusic.mp4").subclipped(18, 28).with_effects([afx.MultiplyVolume(0.1)])
wyr2_music = AudioFileClip("./assets/audio/music/geodashmusic.mp4").subclipped(650, 660).with_effects([afx.MultiplyVolume(0.1)])
wyr3_music = AudioFileClip("./assets/audio\music/invincible.mp4").subclipped(10, 20).with_effects([afx.MultiplyVolume(0.1)])


##COMPILING CLIPS
wyr1.audio = CompositeAudioClip([wyr1_tts, wyr1_music])
wyr2.audio = CompositeAudioClip([wyr2_tts, wyr2_music])
wyr3.audio = CompositeAudioClip([wyr3_tts, wyr3_music])
finalOutput = concatenate_videoclips([wyr1, wyr2, wyr3])
final_number = 1
while os.path.exists(f"./output/Done Videos/finalOutput{final_number}.mp4"):
    final_number += 1
finalOutput.write_videofile(f"./output/Done Videos/finalOutput{final_number}.mp4")
