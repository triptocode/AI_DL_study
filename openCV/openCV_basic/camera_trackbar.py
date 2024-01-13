import cv2

# Read from the first camera device
cap = cv2.VideoCapture(0)

leftTop = (250, 400)
bold = 1
fontScale= 1
text = "openCV!"
textColor = (255, 255, 0)

# Callback function for the trackbar
def on_bold_trackbar(value):
    #print("Trackbar value:", value)
    global bold
    bold = value

def on_fontScale_trackbar(value):
    global fontScale
    fontScale = value

def on_textColor_trackbar(value):
    global textColor
    print(value)
    r = cv2.getTrackbarPos('R',"Camera")
    g = cv2.getTrackbarPos('G',"Camera")
    b = cv2.getTrackbarPos('B',"Camera")
    print(r, g, b)
    textColor_list=list(textColor)
    textColor_list[:] = [b,g,r]
    textColor=tuple(textColor_list)
    
cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)
cv2.createTrackbar("fontScale", "Camera", fontScale, 3, on_fontScale_trackbar)
cv2.createTrackbar('R', "Camera",  0,255, on_textColor_trackbar)
cv2.createTrackbar('G', "Camera",  0,255, on_textColor_trackbar)
cv2.createTrackbar('B', "Camera",  0,255, on_textColor_trackbar)
 
# 성공적으로성공적으로video device 가 열렸으면열렸으면while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Text
    cv2.putText(frame, text, leftTop, cv2.FONT_HERSHEY_SIMPLEX, fontScale, textColor, bold)
    # Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()