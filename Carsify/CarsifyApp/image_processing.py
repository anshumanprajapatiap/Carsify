import cv2
import numpy as np

def resize_img(img_path):
    pic=cv2.imread(img_path)
    print(pic.shape)

    # canvas_size=(333,500)
    if 333/500 < pic.shape[0]/pic.shape[1]:
        x=333
        temp=(333-pic.shape[0])/pic.shape[0]
        y=pic.shape[1]+(temp*pic.shape[1])
    else:
        y=500
        temp=(500-pic.shape[1])/pic.shape[1]
        x=pic.shape[0]+(temp*pic.shape[0])
    
    width = int(y)
    height = int(x)
    dim = (width, height)
    resized = cv2.resize(pic, dim, interpolation = cv2.INTER_AREA)
    print(resized.shape)
    
    cv2.imshow("tt",resized)
    if cv2.waitKey()==13:
        cv2.destroyAllWindows()
        
    img_pic = np.zeros([333,500,3],dtype=np.uint8)
    img_pic[:] = 255
    pad_x=0
    pad_y=0
    if width<500:
        pad_x=(500-width)//2
    if height<333:
        pad_y=(333-height)//2
    img_pic[pad_y:pad_y+height,pad_x:pad_x+width]=resized

    cv2.imshow("t",img_pic)
    cv2.imshow("test",pic)
    if cv2.waitKey()==13:
        cv2.destroyAllWindows()





img_path="../media/c1.jpeg"
resize_img(img_path)