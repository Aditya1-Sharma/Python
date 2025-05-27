import cv2
import os

# Create the folder if it doesn't exist
os.makedirs("photos", exist_ok=True)

cap = cv2.VideoCapture(0)
photo_count = 0


def get_video_fps(video_file):
    vcap = cv2.VideoCapture(video_file)
    fps = vcap.get(cv2.CAP_PROP_FPS)
    return fps


print("Press 'q' to quit, 's' to save a photo, and 'f' to get the FPS.")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        photo_path = f"photos/photo_{photo_count}.jpg"
        cv2.imwrite(photo_path, frame)
        print(f"Photo saved: {photo_path}")
        photo_count += 1
    elif key == ord("f"):
        fps = get_video_fps(0)
        print(f"FPS: {fps}")

cap.release()
cv2.destroyAllWindows()
