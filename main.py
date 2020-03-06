import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
def bubbleSort(arr): 
    n = len(arr) 
    gif_path="mygif.gif"
    frames_path="{k}.jpg"
    plt.figure(figsize=(4,4))
    k=0
    ax=plt.gca()
    ax.set_facecolor('xkcd:black')

    #Bubble sort logic 
    for i in range(n): 
          for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                #saving a new image for each swap
                plt.bar(range(n),arr,color=(1, 1, 1, 0.6))
                plt.xlim(0, 10)
                plt.ylim(0, 10)
                plt.savefig("{k}.jpg".format(k=k))
                k+=1
                
    im=Image.open("1.jpg")
    width,height=im.size
    video_name="myvideo.avi"           
    images=[]           
    video = cv2.VideoWriter(video_name, 0, 1, (width,height))  
    for i in range(k):
        images=images+[frames_path.format(k=i)]
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(image)) 
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 
    
bubbleSort([5,4,3,2,1])                
                
  
