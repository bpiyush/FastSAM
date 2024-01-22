
* Link the models
```sh
ln -s /work/piyush/pretrained_checkpoints/LargeModels/FastSAM ./weights
```
* Link the sample pouring water images
```sh
ln -s /scratch/shared/beegfs/piyush/datasets/PouringLiquidsData/mid_frames ./pouring_water_images
```

*Example command:* To run inference:

```sh
python Inference.py --model_path ./weights/FastSAM-x.pt --img_path ./pouring_water_images/VID_20240116_230040.png --point_prompt "[[135,400],[135,300]]" --point_label "[1,0]"
```