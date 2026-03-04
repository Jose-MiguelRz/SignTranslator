import cv2
import mediapipe as mp
import csv
import os
from datetime import datetime

class DataCollector:
    def __init__(self):
        # Inicializar MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Señás a recolectar
        self.signs = ['HOLA', 'GRACIAS', 'TE_QUIERO', 'SI', 'NO']
        self.current_sign = None
        self.samples_count = 0
        
        # Crear archivo CSV
        self.csv_file = 'data/sign_data.csv'
        # make sure the folder exists before trying to write the CSV
        os.makedirs(os.path.dirname(self.csv_file), exist_ok=True)
        self.init_csv()
        
    def init_csv(self):
        """Inicializar archivo CSV"""
        headers = []
        for i in range(21):
            headers.extend([f'x{i}', f'y{i}', f'z{i}'])
        headers.append('label')
        
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
            print(f"✅ Archivo CSV creado: {self.csv_file}")
    
    def collect_data(self):
        """Capturar datos"""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: No se puede abrir la cámara")
            return
        
        print("\n=== COLECTOR DE DATOS ===")
        print("1: HOLA   2: GRACIAS   3: TE QUIERO")
        print("4: SI     5: NO")
        print("ESPACIO: guardar muestra   q: salir")
        print("\n📸 Instrucciones:")
        print("1. Presiona el número de la seña que harás")
        print("2. Haz la seña con tu mano")
        print("3. Presiona ESPACIO para guardar")
        print("4. Repite 30+ veces por cada seña")
        print("-" * 40)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Voltear imagen
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            
            # Dibujar landmarks si hay manos
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Dibujar puntos y conexiones
                    self.mp_draw.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    if self.current_sign:
                        # Mostrar estado
                        cv2.putText(
                            frame, 
                            f"📝 Recolectando: {self.current_sign} ({self.samples_count})", 
                            (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
                        )
                        
                        # Guardar con ESPACIO
                        key = cv2.waitKey(1) & 0xFF
                        if key == 32:  # Tecla ESPACIO
                            landmarks = []
                            for lm in hand_landmarks.landmark:
                                landmarks.extend([lm.x, lm.y, lm.z])
                            landmarks.append(self.current_sign)
                            
                            with open(self.csv_file, mode='a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(landmarks)
                            self.samples_count += 1
                            print(f"✅ Guardado: {self.current_sign} #{self.samples_count}")
            
            # Mostrar menú
            cv2.putText(frame, "1:HOLA 2:GRACIAS 3:TE QUIERO", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            cv2.putText(frame, "4:SI 5:NO ESPACIO:guardar q:salir", (10, 80), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            
            cv2.imshow('Colector de Datos - Lenguaje de Señas', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('1'):
                self.current_sign = 'HOLA'
                self.samples_count = 0
                print(f"\n🔤 Cambiado a: HOLA")
            elif key == ord('2'):
                self.current_sign = 'GRACIAS'
                self.samples_count = 0
                print(f"\n🔤 Cambiado a: GRACIAS")
            elif key == ord('3'):
                self.current_sign = 'TE_QUIERO'
                self.samples_count = 0
                print(f"\n🔤 Cambiado a: TE QUIERO")
            elif key == ord('4'):
                self.current_sign = 'SI'
                self.samples_count = 0
                print(f"\n🔤 Cambiado a: SI")
            elif key == ord('5'):
                self.current_sign = 'NO'
                self.samples_count = 0
                print(f"\n🔤 Cambiado a: NO")
        
        cap.release()
        cv2.destroyAllWindows()
        print(f"\n💾 Datos guardados en: {self.csv_file}")

if __name__ == "__main__":
    collector = DataCollector()
    collector.collect_data()
