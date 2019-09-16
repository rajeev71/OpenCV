import cv2

'Live stream from camera '

cap = cv2.VideoCapture(0)

'Write Video'

fourcc = cv2.VideoWriter_fourcc(*'MPG4')
out = cv2.VideoWriter('video.mp4', fourcc, 20, (640, 480))



while cap.isOpened():
    ret, frame = cap.read()

    if ret ==True:
        'convert into grayscale '
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        out.write(gray)

        if cv2.waitKey(1)&0xFF == ord('q'):
             break
cap.release()

cv2.destroyAllWindows()
