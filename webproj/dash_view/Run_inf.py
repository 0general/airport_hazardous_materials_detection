import os
from glob import glob

def inference(input_root):

    for imgs in glob(os.path.join(input_root, "*.jpg")):
        argument = "/home/ubuntu/yolo_pjr/darknet/darknet detector test /home/ubuntu/cfgs/custom_wanda.data /home/ubuntu/cfgs/yolov3_custom_wanda.cfg /home/ubuntu/cfgs/yolov3_custom_last_F1_93.weights {} thresh=0.4".format(imgs)
        os.system(argument)