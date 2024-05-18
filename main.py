import cv2
import numpy as np
import torch
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from ultralytics import YOLO

class YOLOApp(App):
    def build(self):
        self.model = YOLO('yolov8n.pt')
        self.capture = cv2.VideoCapture(0)

        layout = BoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)
        self.button = Button(text="Capture")
        self.button.bind(on_press=self.capture_frame)
        layout.add_widget(self.button)
        self.label = Label(text="Detection Results")
        layout.add_widget(self.label)

        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            self.frame = frame
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture

    def capture_frame(self, *args):
        # Convertir l'image en tensor
        frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        tensor_img = torch.from_numpy(frame_rgb).permute(2, 0, 1).float() / 255.0
        tensor_img = tensor_img.unsqueeze(0)  # Ajouter une dimension pour le batch

        # Passer l'image tensorisée au modèle
        results = self.model(tensor_img)
        annotated_frame = results[0].plot()

        # Afficher les résultats de la détection
        detection_results = results[0].boxes
        detection_text = "Detected objects:\n"

        for box in detection_results:
            print(box)  # Inspecter le contenu de box
            try:
                class_id = int(box.cls.item())
                score = box.conf.item()
                label = self.model.names[class_id]
                detection_text += f"{label} ({score:.2f})\n"
            except Exception as e:
                detection_text += f"Unknown object detected: {e}\n"
                print(f"Error processing box: {e}")

        self.label.text = detection_text

        buf = cv2.flip(annotated_frame, 0).tobytes()
        texture = Texture.create(size=(annotated_frame.shape[1], annotated_frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

if __name__ == '__main__':
    YOLOApp().run()
