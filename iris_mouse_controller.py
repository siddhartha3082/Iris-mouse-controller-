import cv2
import mediapipe as mp
import pyautogui

def smooth(coordinates, alpha=0.5):
    if not hasattr(smooth, 'previous_coordinates'):
        smooth.previous_coordinates = coordinates
    smoothed_coordinates = []
    for (x, y), (prev_x, prev_y) in zip(coordinates, smooth.previous_coordinates):
        smoothed_x = int(prev_x * alpha + x * (1 - alpha))
        smoothed_y = int(prev_y * alpha + y * (1 - alpha))
        smoothed_coordinates.append((smoothed_x, smoothed_y))
    smooth.previous_coordinates = smoothed_coordinates
    return smoothed_coordinates

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb)
    points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if points:
        lms = points[0].landmark
        coords = [(int(lm.x * frame_w), int(lm.y * frame_h)) for lm in lms[:468]]

        smooth_coords = smooth(coords)

        for (x, y) in smooth_coords:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        x, y = smooth_coords[1]

        if abs(coords[145][1] - coords[159][1]) < 5:
            pyautogui.click()
            pyautogui.sleep(0.25)

        sx = int(screen_w * x / frame_w)
        sy = int(screen_h * y / frame_h)
        pyautogui.moveTo(sx, sy)

    cv2.imshow("Iris Mouse Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
