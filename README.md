# Xrayolo
---
**Yolo** 기반 객체 탐지를 활용한 **X-ray** 상의 **위해물품 탐지** 프로그램
<br>

## Video
---
<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/56211221/168593675-e4f09d39-3fa3-462e-b9d6-5d3863b057c3.gif"/>
<img width="80%" src="https://user-images.githubusercontent.com/56211221/168594873-33c0f242-7d1a-4448-8b2e-deed1d1523cb.gif"/>
</p>

**Full presentation video on [YouTube]()**
<br>


## Info
---
#### 서비스 이용 대상 
> **공항 검색대**와 같이 X-ray 물품 검사를 필요로 하는 기업

#### 기대 효과
> + 위험물체 판독 보조를 통한 작업 피로도 감소
> + 판독 과정에 필수적인 비용 감소

<br>

## Role
---

1. Rapiscan 스캐너로 촬영한 X-ray 동영상을 입력으로 받아, 사이트에 업로드합니다.  
2. 서버는 업로드된 동영상을 실시간으로 분할 전처리한 후, 이미지 속의 객체를 탐지하고 DB에 저장합니다.
3. 탐지된 결과는 곧바로 웹 상에서 확인이 가능합니다.

> 탐지 가능한 물품은 공항 위해물품과 기업용 보안물품을 포함한 34종입니다. 

<br>

## Build Guide
---
### Requirements

+ Python 3.9
+ (for GPU) CUDA 10.1 
+ (for GPU) CUdnn 7.6.5 - for CUDA 10.1 ver 
+ (for GPU) Graphic Card - we used NVIDIA Tesla V100 32GB
+ opencv 3.4.0 이상
+ git
+ django
+ numpy
+ Yolo version3

```
pip install numpy
```
```
pip install opencv-python
```
```
pip install Django
```

<br>

## Dataset
---
[**AI hub**](https://aihub.or.kr/aidata/33)
<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/56211221/168599645-fc82521f-e075-4734-8dae-7e39523cb5ad.png"/>
</p>  
<p align="center">
Rapiscan
</p>

<br>

## Test Accuracy
---
+ F1 score 93
+ mAP(0.5) 기준 92.34%

<br>


## References
---
+ Yolo 
> https://github.com/AlexeyAB/darknet
+ Ubuntu OS
> https://kkoma-it.tistory.com/1
+ opencv 설치
> https://j-remind.tistory.com/57
