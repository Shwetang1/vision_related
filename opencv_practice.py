import cv2

# How to add trackbar?
# Useful when we want to change a value in the image dynamically at runtime.
# black_img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

img_lena = cv2.imread("../data/lena.jpg")


def nothing(x):
    print(x)


# CREATE SWITCH !

switch = '0: off \n 1: on'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)  # Switch 0-1 trackbar

# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)

cv2.createTrackbar('CP', 'image', 10, 400, nothing)  # Current position trackbar

while (True):
    # cv2.imshow('image',black_img)

    cv2.imshow('image', img_lena)
    trackbar_pos = cv2.getTrackbarPos('CP', 'image')

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_lena, str(trackbar_pos), (150, 150), font, 4, (255, 0, 0))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    #     r = cv2.getTrackbarPos('R','image')
    #     g = cv2.getTrackbarPos('G','image')
    #     b = cv2.getTrackbarPos('B','image')

    #     if s == 0:
    #         black_img[:] = 0
    #     else:
    #         black_img[:] = [r,g,b]

    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        cv2.cvtColor(img_lena, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image', img_lena)

cv2.destroyAllWindows()