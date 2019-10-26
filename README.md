# traffic-sign-detection
This is a project which we have done as a part of college mini project  
The aim of the project is to detect the traffic signs from a video  
First we are gonna develop a cnn model which takes the traffic sign and classifies it to one of the classes  
For this project we have used the german traffic sign dataset benchmark (GTSDB) which consists of around 43 classes In the dataset all the classes are divided into different folders  
First We are gonna divide the 43 classes into 3 groups and we are gonna train 3 models to train images(Single model is giving less accuracy)
![test image 1](/images/dataset-classes.png)
The above picture contains images of all classes which are there in the dataset.    

The below image contains 3 groups which we have classified as triangle, circle and other
![test image 2](/images/3-groups.png)  

The final output is gonna look like this  

![Output image 1](/images/image&#32;(1).png)  

![Output image 2](/images/image&#32;(2).png)  

# Steps to do
1.Create an model for other classes with high accuracy\
2.Classify whether the traffic sign contains red circle or red triangle or other shape\
3.Detect whether the image contains a traffic sign or not from video
