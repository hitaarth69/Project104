import cv2
img = cv2.imread("solar-system.jpg")

text = "Sun"
cv2.putText(img, text, (100,300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0,0,255))
cv2.imshow("display", img)
cv2.waitKey(0)

text = "Mercury"
cv2.putText(img, text, (110,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,255,255))
cv2.imshow("display2", img)
cv2.waitKey(0)

text = "Venus"
cv2.putText(img, text, (170,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("display2", img)
cv2.waitKey(0)

text = "Earth"
cv2.putText(img, text, (290,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.9, color=(255,255,255))
cv2.imshow("display2", img)
cv2.waitKey(0)

text = "Moon"
cv2.putText(img, text, (290,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.9, color=(255,255,255))
cv2.imshow("display2", img)
cv2.waitKey(0)


text = "Mars"
cv2.putText(img, text, (380,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.9, color=(255,255,255))
cv2.imshow("display2", img)
cv2.waitKey(0)


text1 = "Jupiter"
cv2.putText(img, text1, (500,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("display1", img)
cv2.waitKey(0)

text1 = "Saturn"
cv2.putText(img, text1, (730,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("display1", img)
cv2.waitKey(0)

text1 = "Uranus"
cv2.putText(img, text1, (950,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("display1", img)
cv2.waitKey(0)

text1 = "Neptune"
cv2.putText(img, text1, (1090,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.imshow("display1", img)
cv2.waitKey(0)