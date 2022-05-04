import os
from glob import glob
from pathlib import Path
from sqlite3 import Timestamp
from tkinter import image_names
from . import models
from datetime import datetime

def inference(input_root, delete_root, job_num):
    # 원본 동영상 삭제
    for video in glob(os.path.join(delete_root, "*.mp4")):
        os.system("rm {}".format(video))

    # 추론 결과 저장 디렉토리 고유 번호로 생성
    os.system("mkdir /home/ubuntu/result/{}".format(job_num))

    os.system("/home/ubuntu/yolo/darknet/darknet detector test /home/ubuntu/cfgs/custom_wanda.data /home/ubuntu/cfgs/yolov3_custom_wanda.cfg /home/ubuntu/cfgs/yolov3_custom_last_F1_93.weights")
    count = 0
    for imgs in glob(os.path.join(input_root, "*.jpg")):
        name = Path(imgs).stem 

        # 추론 실행
        # argument = "/home/ubuntu/yolo/darknet/darknet detector test /home/ubuntu/cfgs/custom_wanda.data /home/ubuntu/cfgs/yolov3_custom_wanda.cfg /home/ubuntu/cfgs/yolov3_custom_last_F1_93.weights {} thresh=0.4".format(imgs)
        
        # os.system(argument)
        print(imgs)
        # os.system(imgs)

        # 추론 결과 prediction.jpg 파일명 변경 및 저장
        result_img = "/home/ubuntu/result/{}/inf_{}.jpg".format(job_num, name)
        os.system("cp /home/ubuntu/jonghyeon/airport_hazardous_materials_detection/webproj/predictions.jpg " + result_img)
        noti_data = models.Noti(
            id = count,
            Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            img_name = name,
            # confidence
            # item_class
        )
        noti_data.save()
        # 추론이 끝난 이미지 삭제
        os.system("rm {}".format(imgs))
        count += 1
    
    os.system("^C")