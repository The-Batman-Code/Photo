import jsonlines
import cv2
num=0
with jsonlines.open('Address of .jsonl file') as data:
 for line in data:
    address=line['image']['address'].replace('_','\\')     #accessing and storing the address of image from .jsonl file 
    temp_img = cv2.imread(address, cv2.IMREAD_COLOR)
    img=cv2.resize(temp_img,(720,500))
    x_min=line['about']['coordinates'][0][0]    #accessing coordinates to draw box from .jsonl file
    y_min=line['about']['coordinates'][0][1]
    x_max=line['about']['coordinates'][0][2]
    y_max=line['about']['coordinates'][0][3]
    image = cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (255,0,0), 2)   #drawing boxe over the image
    cv2.imwrite('Address where the images are to be stored'+str(num)+'.jpg',image)   #saving the new image at a specified address
    num+=1