import cv2

image = cv2.imread("Assets/solar-system.jpg")

cv2.putText(
  image,
  "Sun",
  (100, 50),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Mercury",
  (130, 250),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Venus",
  (200, 260),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Earth",
  (300, 260),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Mars",
  (400, 250),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Jupiter",
  (650, 300),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Saturn",
  (900, 300),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Uranus",
  (1000, 300),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)
cv2.putText(
  image,
  "Neptune",
  (1200, 300),
  cv2.FONT_HERSHEY_COMPLEX_SMALL,
  0.5,
  (255, 255, 255)
)

cv2.imshow("image-viewer.exe", image)
cv2.waitKey(3000)