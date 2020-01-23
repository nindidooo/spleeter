import youtube2mp3
from spleeter.separator import Separator
import warnings
warnings.filterwarnings('ignore')
import librosa
import matplotlib.pyplot as plt
import numpy as np

# url = "https://www.youtube.com/watch?v=PivWY9wn5ps"
urls = [
# "https://www.youtube.com/watch?v=YcXzU4JOiDE"
"https://www.youtube.com/watch?v=L_XJ_s5IsQc"
# "https://www.youtube.com/watch?v=Lpjcm1F8tY8"

# "https://www.youtube.com/watch?v=MZ6GzmrGHOY"
# "https://www.youtube.com/watch?v=V9bAWAgzz38",
        # "https://www.youtube.com/watch?v=1aVHLL5egRY",
        # "https://www.youtube.com/watch?v=8SbUC-UaAxE",
        # "https://www.youtube.com/watch?v=wssIZOBV9i4",
        # "https://www.youtube.com/watch?v=IwzUs1IMdyQ",
        # "https://www.youtube.com/watch?v=7R6RGsB67zA",
        # "https://www.youtube.com/watch?v=ULj6eH5YfAw",
        # "https://www.youtube.com/watch?v=mn77gzjBl1U",
        # "https://www.youtube.com/watch?v=8iwBM_YB1sE",
        # "https://www.youtube.com/watch?v=MlW7T0SUH0E",
        # "https://www.youtube.com/watch?v=LOZuxwVk7TU",
        # "https://www.youtube.com/watch?v=eBG7P-K-r1Y",
        # "https://www.youtube.com/watch?v=vlB_8TYnt88",
        # "https://www.youtube.com/watch?v=aBaodv5sLok",
        # "https://www.youtube.com/watch?v=PivWY9wn5ps",
        # "https://www.youtube.com/watch?v=SlPhMPnQ58k"

        ]

for url in urls:
    audio_file_path = youtube2mp3.youtube2mp3(url)
    # Using embedded configuration.
    # import pdb
    # pdb.set_trace()
    separator = Separator('spleeter:5stems')

    # Use audio loader explicitly for loading audio waveform :
    # from spleeter.audio.adapter import get_default_audio_adapter
    # audio_loader = get_default_audio_adapter()
    # sample_rate = 44100
    # x, _ = audio_loader.load(audio_file_path, sample_rate=sample_rate)

    # Perform the separation :
    separator.separate_to_file(audio_file_path, 'output')

    # get beats
    # x, sr = librosa.load(audio_file_path)
    # x = np.array(x) 
    # plt.plot(x)
    # plt.show()
    # print(size(x))
    # Perform the separation :
    # prediction = separator.separate(x)
