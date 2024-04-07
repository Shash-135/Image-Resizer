import cv2

Source = input("Enter the Path of the image to resize :")
Width_percent = int(input("Enter the width you want the image in :"))
Height_percent = int(input("Enter the Height you want the image in :"))

image = cv2.imread(Source, cv2.IMREAD_UNCHANGED)

new_width = int(image.shape[1] * Width_percent/100)
new_height = int(image.shape[0] * Height_percent/100)

output = cv2.resize(image, (new_height, new_width))

cv2.imwrite(Source, output)
cv2.imshow("title", image)
cv2.waitKey(0)
