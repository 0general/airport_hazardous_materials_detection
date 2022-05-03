import os
from glob import glob

def inference(input_root, delete_root, job_num):
    # 원본 동영상 삭제
    for video in glob(os.path.join(delete_root, "*.mp4")):
        os.system("rm {}/{}".format(delete_root, video))

    # 추론 결과 저장 디렉토리 고유 번호로 생성
    os.system("mkdir /home/ubuntu/result/{}".format(job_num))

    for imgs in glob(os.path.join(input_root, "*.jpg")):

        # 추론 실행
        argument = "/home/ubuntu/yolo/darknet/darknet detector test /home/ubuntu/cfgs/custom_wanda.data /home/ubuntu/cfgs/yolov3_custom_wanda.cfg /home/ubuntu/cfgs/yolov3_custom_last_F1_93.weights {} thresh=0.4".format(imgs)
        os.system(argument)

        # 추론 결과 prediction.jpg 파일명 변경 및 저장
        os.system("cp /home/ubuntu/yolo/darknet/prediction.jpg /home/ubuntu/result/{}/{}".format(job_num, imgs))
        
        # 추론이 끝난 이미지 삭제
        os.system("rm {}/{}".format(input_root, imgs))