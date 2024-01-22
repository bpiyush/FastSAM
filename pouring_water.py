import os
from fastsam import FastSAM, FastSAMPrompt

model = FastSAM('./weights/FastSAM-x.pt')
IMAGE_PATH = './pouring_water_images/VID_20240116_230040.png'
DEVICE = 'cpu'

everything_results = model(IMAGE_PATH, device=DEVICE, retina_masks=True, imgsz=1024, conf=0.4, iou=0.9,)
prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)

# everything prompt
ann = prompt_process.everything_prompt()

# # bbox default shape [0,0,0,0] -> [x1,y1,x2,y2]
# ann = prompt_process.box_prompt(bboxes=[[200, 200, 300, 300]])

# # text prompt
# ann = prompt_process.text_prompt(text='a photo of a dog')

# point prompt
# points default [[0,0]] [[x1,y1],[x2,y2]]
# point_label default [0] [1,0] 0:background, 1:foreground
ann = prompt_process.point_prompt(points=[[135,400], [135,380],[135,300]], pointlabel=[1,1,0])

IMAGE_ID = os.path.basename(IMAGE_PATH).split('.')[0]
prompt_process.plot(annotations=ann,output_path=f'./output/{IMAGE_ID}.png')
import ipdb; ipdb.set_trace()