# Sops-Monitoring-and-Detection-YoloV5


<p align="center">
  <img src="/Figures/9.-WearMaskNet-Real-Time-Face-Mask-Detection.png" align="center" width="800" height="400">
</p>

## Yolo Architecture
YOLO stands for You Only Look Once, this model is used for Object Detection as well as Object Tracking with the help of CNN, our research uses YOLO for calculating the social distancing with the help of Object Detection and feature extraction from the data, whereas tracking the face and people in the frame for counting the objects and keeping a record of that object in the next frame is done by Object Tracking. The minimum distance to keep in social distancing is 2 meters, the model was trained and used for object detection as well as object tracking. 


<p align="center">
  <img src="/Figures/yolo.png" align="center">
</p>



YOLOv3 is fast and accurate in terms of mean average precision (mAP) and intersection over union (IOU) values as well. It runs significantly faster than other detection methods with comparable performance (hence the name – You only look once). Moreover, you can easily trade-off between speed and accuracy simply by changing the model’s size, without the need for model retraining.


## Inception Res-Net-V2
The Inception-ResNet v2 architecture was released by Szegedy et al. and is based on the combination of two ideas: residual connections and the Inception architecture. Inception-ResNet-v2 is a convolutional neural network that is trained on more than a million images from the ImageNet database. The network is 164 layers deep and can classify images into 1000 object categories, such as the keyboard, mouse, pencil, and many animals. As a result, the network has learned rich feature representations for a wide range of images. The network has an image input size of 299-by-299, and the output is a list of estimated class probabilities.

<p align="center">
  <img src="/Figures/Inception-Resnet-V2-Architecture.png" align="center" width="700" height="400">
</p>
 
## Model Consider

<p align="center">
  <img src="/Figures/table.jpg" align="center" width="700" height="400">
</p>


## Dataset
Facemask dataset is available in Kaggle. We have Total 14 thousand face images. These images divided based on face have mask or not. For the with mask, we have 8000 thousand images and without mask we have 7000 images. 

<p align="center">
  <img src="/Figures/dataset.jpg" align="center" width="300" height="200">
</p>

## Front-end

<p align="center">
  <img src="/Figures/1.jpg" align="center" width="500" height="300">
</p>

### Register
<p align="center">
  <img src="/Figures/sign.jpg" align="center" width="500" height="300">
</p>

### Dashboard
<p align="center">
  <img src="/Figures/3.jpg" align="center" width="500" height="300"><img src="/Figures/4.jpg" align="center" width="500" height="300">
</p>

### Detection
<p align="center">
  <img src="/Figures/5.jpg" align="center" width="500" height="300"> <img src="/Figures/mask.jpg" align="center" width="500" height="300">
</p>

## Tools and Technologies
1) Jupyter notebook (anaconda3) 6.4.8
2) Visual Studio Code 1.67.2
3) Python 3.7
4) HTML 5
5) CSS 4.13
6) Flask 1.1.x
7) YOLO
8) Inception ResNet v2


