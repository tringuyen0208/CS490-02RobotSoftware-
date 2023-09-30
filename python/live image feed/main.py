import cv2
vidcap = cv2.VideoCapture(0)
vidcap.read()
input("Is the camera on?")
success,image = vidcap.read()
#image = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
count = 0
while success:
  success = cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  if (input("Continue? ")).lower() == "n":
    break 
  success,image = vidcap.read()
  #image = cv2.resize(image, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
  print('Read a new frame: ', success)
  count += 1

vidcap.release()
cv2.destroyAllWindows()
