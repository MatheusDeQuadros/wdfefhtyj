import cv2

video=cv2.VideoCapture(0)


if(video.isOpened()==False):
    print("Deu ruim... :( ")

altura=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(altura)

largura=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(largura)

fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):
  ret,frame=video.read()
  cv2.imshow("Resultado da webCam ",frame)
  if cv2.waitKey(25)==27:
    break
video.release()    
