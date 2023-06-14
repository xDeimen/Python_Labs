import cv2
import numpy as np

# Inițializarea capturii video
cap = cv2.VideoCapture(0)  # Utilizați 0 pentru camera principală sau specificați un fișier video

# Sau citirea imaginii de intrare
# image = cv2.imread('nume_imagine.jpg')

def detect_and_classify_objects(frame):
    # Convertiți imaginea la spațiul de culoare HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definiți intervalul culorilor pe care doriți să le detectați
    lower_color = np.array([H_MIN, S_MIN, V_MIN])  # Definiți valorile minime ale culorii în HSV
    upper_color = np.array([H_MAX, S_MAX, V_MAX])  # Definiți valorile maxime ale culorii în HSV

    # Creați un masca pe baza intervalului de culori
    color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Aplicați un filtru de erodare și dilatare pentru a elimina zgomotul
    kernel = np.ones((5, 5), np.uint8)
    color_mask = cv2.erode(color_mask, kernel, iterations=2)
    color_mask = cv2.dilate(color_mask, kernel, iterations=2)

    # Găsiți contururile obiectelor detectate
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Parcurgeți contururile și clasificați obiectele pe baza culorilor
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > MIN_OBJECT_AREA:
            # Desenați conturul obiectului detectat
            cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

            # Aici puteți implementa logica de clasificare a obiectelor în funcție de culoare

    return frame

while True:
    # Capturarea unui cadru video
    ret, frame = cap.read()

    # Sau utilizarea imaginii de intrare
    # frame = image.copy()

    # Detectarea și clasificarea obiectelor
    result_frame = detect_and_classify_objects(frame)

    # Afișarea rezultatului
    cv2.imshow("Object Classification", result_frame)

    # Ieșirea din buclă la apăsarea tastei 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Eliberați resursele
cap.release()
cv2.destroyAllWindows()
