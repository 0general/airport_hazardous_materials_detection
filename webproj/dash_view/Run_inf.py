import os
from glob import glob
from pathlib import Path
import random
import cv2
from sqlite3 import Timestamp
from tkinter import image_names
from . import models
from .inference import darknet, darknet_images
from datetime import datetime

def inference(input_root, delete_root, job_num):
    # 원본 동영상 삭제
    for video in glob(os.path.join(delete_root, "*.mp4")):
        os.system("rm {}".format(video))

    # 추론 결과 저장 디렉토리 고유 번호로 생성
    os.system("mkdir /home/ubuntu/jonghyeon/airport_hazardous_materials_detection/webproj/dash_view/static/images/{}".format(job_num))
    
    count = 0
    random.seed(3)  # deterministic bbox colors

    network, class_names, class_colors = darknet.load_network(
        "/home/ubuntu/cfgs/yolov3_custom_wanda.cfg",
        "/home/ubuntu/cfgs/custom_wanda.data",
        "/home/ubuntu/cfgs/yolov3_custom_last_F1_93.weights",
        batch_size=1
    )

    for imgs in glob(os.path.join(input_root, "*.jpg")):
        name = Path(imgs).stem 

        image, detections = darknet_images.image_detection(
            imgs, network, class_names, class_colors, 0.4
            )
        darknet.print_detections(detections)
      
        for label, conf, bbox in detections:
            if conf:
                result_img = "/home/ubuntu/jonghyeon/airport_hazardous_materials_detection/webproj/dash_view/static/images/{}/inf_{}.jpg".format(job_num, name)
                cv2.imwrite(result_img, image)
                noti_data = models.Noti(
                    id = job_num* 100000 + count, # id 중복안되게 count 말고 다른거로 변경해야됨.
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    img_name = "{}/inf_{}.jpg".format(job_num, name),
                    confidence = conf,
                    item_class = label,
                )
                noti_data.save()

        
        # 추론이 끝난 이미지 삭제
        os.system("rm {}".format(imgs))
        count += 1
    