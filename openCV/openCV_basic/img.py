import cv2

##ubuntu /Home = /home/kk
image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_ANYCOLOR)
# image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_COLOR)

# image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
# image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_REDUCED_GRAYSCALE_4)

# image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_REDUCED_COLOR_2)
# image = cv2.imread("/home/kk/img/earth.jpeg", cv2.IMREAD_REDUCED_COLOR_4)


# option info
print("image.shape Info: ", image.shape)
height, width, channel = image.shape #(401, 602, 3) 
print("height Info: ", height) #401
print("height, width, channel Info: ", height, width, channel) #401, 602, 3


cv2.imshow("Earth", image)

cv2.waitKey()
cv2.destroyAllWindows()



