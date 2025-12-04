import cv2
import numpy as np
from ultralytics import YOLO

class OrientationClassifier:
    def _init_(self, model_name='yolov8n.pt'):
        print(f"Cargando modelo Deep Learning ({model_name})...")
        self.model = YOLO(model_name)

        self.colors = {
            'Horizontal': (0, 255, 0), 
            'Vertical': (0, 0, 255),   
            'Inclinado': (0, 255, 255)
        }

    def get_angle_pca(self, mask):
        """
        Calcula el ángulo principal del objeto usando PCA.
        """
        pts = cv2.findNonZero(mask)
        if pts is None or len(pts) < 5:
            return None

        pts = np.squeeze(pts)
        mean, eigenvectors, eigenvalues = cv2.PCACompute2(pts.astype(np.float32), mean=None)

        vx, vy = eigenvectors[0]
        angle = np.degrees(np.arctan2(vy, vx))

        # Normalizar a rango [-90, 90]
        if angle > 90:
            angle -= 180
        elif angle < -90:
            angle += 180

        return float(angle)

    def classify_angle(self, angle):
        """
        Clasifica según ángulo PCA con umbrales mejorados.
        """
        if angle is None:
            return "Inclinado"

        a = abs(angle)

        if a <= 10:
            return "Horizontal"
        elif a >= 80:
            return "Vertical"
        else:
            return "Inclinado"

    def process_frame(self, frame):
        results = self.model(frame, verbose=False, conf=0.5)
        annotated_frame = frame.copy()

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cls = int(box.cls[0])
                label_name = self.model.names[cls]
                conf = float(box.conf[0])

                if label_name == "person":
                    continue

                roi = frame[y1:y2, x1:x2]
                if roi.size == 0:
                    continue

                gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

                angle = self.get_angle_pca(thresh)
                orientation = self.classify_angle(angle)
                color = self.colors[orientation]

                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 3)

                # Texto sin "??"
                info_text = f"{label_name} ({conf:.2f})"
                cv2.putText(annotated_frame, info_text, (x1, y1 - 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                if angle is not None:
                    cv2.putText(annotated_frame, f"Angulo: {angle:.1f}°", (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                else:
                    cv2.putText(annotated_frame, "Angulo: N/A", (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                cv2.putText(annotated_frame, orientation, (x1, y2 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                # Flecha PCA
                if angle is not None:
                    center = (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
                    length = 60
                    dx = int(np.cos(np.radians(angle)) * length)
                    dy = int(np.sin(np.radians(angle)) * length)

                    cv2.arrowedLine(
                        annotated_frame,
                        center,
                        (center[0] + dx, center[1] + dy),
                        color,
                        3
                    )

        return annotated_frame

    def run(self):
        cap = cv2.VideoCapture(0)
        print("\n--- CLASIFICADOR DE ORIENTACIÓN (Deep Learning + PCA) ---")
        print("Presiona 'q' para salir.\n")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            output = self.process_frame(frame)
            cv2.imshow('Proyecto 3: Orientación', output)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if _name_ == "_main_":
    app = OrientationClassifier()
    app.run()
