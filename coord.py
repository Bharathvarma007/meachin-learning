
import cv2
def coord(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK: #check for left double click
        print(x,' ',y)            #printing coords in shell
        cv2.putText(img,"coordinates(%d,%d)"%(x,y),(60,60),2,1,(0,255,0)) #coords on image
        cv2.imshow('image',img)      #showing new image with coords
        #------inetialize-------
img = cv2.imread("cer.jpg")  #reading the image using cv2
cv2.imshow('image',img)      #displaying the image
cv2.setMouseCallback('image',coord) # default function to use mouse clicks
                                    #where we pass the image window and user fun'coord'
cv2.waitKey(0)                      
cv2.destroyAllWindows()             #clears the window


