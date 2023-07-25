from PIL import Image

from skimage.metrics import peak_signal_noise_ratio as psnr
import numpy as np
def frame_expand(path):
    gif_image = None
    try:
        gif_image = Image.open(path)
    except:
        print("Can't open")
    frames_collection = []
    for index in range(gif_image.n_frames - 2):
        gif_image.seek(index)
        frame_1 = gif_image.copy().convert("RGB")
        gif_image.seek(index+1)
        frame_2 = gif_image.copy().convert("RGB")
        diff_1 = psnr(np.array(frame_1), np.array(frame_2))
        if diff_1 < 10.0:
            continue
        gif_image.seek(index+2)
        frame_3 = gif_image.copy().convert("RGB")
        diff_2 = psnr(np.array(frame_2), np.array(frame_3))
        if diff_2 < 10.0:
            continue
        frames_collection.append([frame_1, frame_2, frame_3])
    return frames_collection
result = frame_expand("hp.gif")
print(result)