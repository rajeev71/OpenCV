import cv2
import datetime

'Live stream from camera '

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


' To set property on capture image either you can give value or use above one'
'If you pass more value then its height and width ll be maximum allowed for that capture device'

cap.set(3, 450)
cap.set(4, 550)



while cap.isOpened():
    ret, frame = cap.read()

    if ret ==True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width :' + str(cap.get(3)) + 'Height :'+str(cap.get(4))
        display_date = str(datetime.datetime.now())
        frame = cv2.putText(frame, display_date, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)


        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
cap.release()

cv2.destroyAllWindows()
