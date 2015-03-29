import cv2
import sys
imagePath = sys.argv[1]
cscPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cscPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))
c=0
# Crop faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face = image[y:y+h,x:x+h]
    cv2.imwrite('face%d.jpg'%c,face)
    c+=1

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
