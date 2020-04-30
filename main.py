from PIL import Image
import pytesseract
import cv2
import os


def main():
    cap = cv2.VideoCapture(0)
    filename = "received.png"
    text = ""

    while True:
        ret, image = cap.read()
        image = cv2.resize(image, (640, 380))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        gray = cv2.medianBlur(gray, 3)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("p"):
            cv2.imwrite(filename, gray)
            text = pytesseract.image_to_string(Image.open(filename))
            os.remove(filename)

        cv2.putText(image, text, (30, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Output", gray)
        cv2.imshow("in", image)
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
