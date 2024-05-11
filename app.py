import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os

class GestureRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconhecimento de Gestos - Douglas Graeff")
        root.geometry("1020x800")  # Definir tamanho inicial da janela


        # Frame para exibição do vídeo
        self.video_frame = tk.Label(root)
        self.video_frame.pack()

        # Botão para carregar o vídeo
        self.load_video_button = ttk.Button(root, text="Carregar Vídeo", command=self.load_video)
        self.load_video_button.pack(pady=10)

        # Variável para armazenar o caminho do vídeo
        self.video_path = None

        # Variável para controlar a reprodução do vídeo
        self.playing_video = False

    def load_video(self):
        video_path = os.path.join("video", "video.mp4")
        if os.path.exists(video_path):
            self.video_path = video_path
            self.play_video()
        else:
            print("Arquivo de vídeo não encontrado.")

    def play_video(self):
        if self.video_path:
            self.playing_video = True
            video_capture = cv2.VideoCapture(self.video_path)
            while self.playing_video:
                ret, frame = video_capture.read()
                if not ret:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (580, 780))
                photo = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=photo)
                self.video_frame.configure(image=photo)
                self.video_frame.image = photo
                self.video_frame.update()
            video_capture.release()

    def stop_video(self):
        self.playing_video = False

# Inicializar a aplicação
root = tk.Tk()
app = GestureRecognitionApp(root)
root.mainloop()
