# Diagnosis-of-X-ray-with-YOLOv5

Now you zip the yolov5 folder into yolov5.zip file and upload that zip file to the root of your Google Drive (don't put it in any folder).

Next you go to Google Colab to train step by step!

ON GPU ENVIRONMENT
Go to Runtime > Change runtime type menu and select GPU. Then click Connect to connect to the GPU environment!

Connect Google Colab to Google Drive

Create a Code block and type this and follow the on-screen instructions. If you are not familiar with Colab, you can see more here.

from google.colab import drive
drive.mount('/content/gdrive')


Unzip the source code and train
You create a new code block, run the following command to extract the source code:

%cd /content/gdrive/MyDrive
!unzip yolov5.zip
Then you will see the yolov5 folder on Google Drive (and Colab), you create a new code block and continue running

%cd /content/gdrive/MyDrive/yolov5
!pip install -r requirements.txt

And finally train, you create a new code block and run:

%cd /content/gdrive/MyDrive/yolov5
!python train.py --img 640 --batch 16 --epochs 5 --data models/data.yaml --weights yolov5x.pt

With this command, you notice:


 
–img 640: input image size, temporary default.
–batch 16: batch_size. If you run it and run out of memory, change it back to 8.
–epochs 5: The number of epochs, you can adjust the increase/decrease arbitrarily so that the model with converged mAP is okie (I will talk later).
–data models/data.yaml: is pointing to the data.yaml file that we created.
