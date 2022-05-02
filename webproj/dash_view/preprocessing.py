import os
from glob import glob
import cv2
from pathlib import Path
import shutil
from time import sleep, strftime, localtime, time


def make_frame(video_root, save_root, debug, delete_root=None):

    for video_file in glob(os.path.join(video_root, "*.mp4")):
        video = cv2.VideoCapture(video_file)
        # new file name -> time
        now = strftime('%y%m%d_%H%M%S', localtime(time()))
        if debug:
            print(video_file)
            print(now)

        if not video.isOpened():
            print("Could not open : ", video_file)
            exit(0)

        # 초당 프레임 (1초에 한 프레임 뽑아내도록)
        fps = int(video.get(cv2.CAP_PROP_FPS))
        print(fps)

        # 최대 16분까지
        count = 0
        while(video.isOpened()):
            ret, image = video.read()
            if not ret:
                print("Failed to read frame")
                break
            if (int(video.get(1)) % fps == 0):  # 1 frame per 1 second
                new_name = now + f"_{count:03}" + ".jpg"
                image_path = os.path.join(save_root, new_name)
                cv2.imwrite(image_path, image)
                count += 1
                if debug:
                    print(image_path)
                    cv_img = cv2.imread(image_path)
                    winname = "check image"
                    # 영상을 창 크기에 맞춤
                    cv2.namedWindow(winname, flags=cv2.WINDOW_NORMAL)
                    cv2.resizeWindow(winname=winname, width=1000, height=700)
                    cv2.moveWindow(winname=winname, x=40, y=30)
                    cv2.imshow(winname, cv_img)
                    cv2.waitKey(1000)  # 0->키보드 입력 대기, 1000(단위가 ms)-> 1초 후 종료
                    cv2.destroyAllWindows()
        video.release()
        if delete_root is not None:
            video_name = Path(video_file).stem
            shutil.move(video_file, os.path.join(
                delete_root, video_name+".mp4"))
        sleep(1)  # 최소한 1초의 차이를 두기 위해


if __name__ == "__main__":
    test_root = r"C:/Users/YunA/Desktop/media"
    save_root = r"C:/Users/YunA/Desktop/media/result"
    debug_ok = False

    # make_frame(test_root, save_root, debug_ok)
    make_frame(test_root, save_root, debug_ok, r"C:/Users/YunA/Desktop/media/delete")
