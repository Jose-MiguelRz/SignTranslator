import cv2
import mediapipe as mp
import numpy as np
import pickle
from collections import deque, Counter

class SignLanguageTranslator:
    def __init__(self):
        # Cargar modelo
        with open('../models/sign_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        with open('../models/model_info.pkl', 'rb') as f:
            self.model_info = pickle.load(f)
        
        # Inicializar MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Historial para suavizar
        self.history = deque(maxlen=5)
        self.current_sign = "Esperando..."
        self.confidence = 0
        
        # Colores para cada seña
        self.colors = {
            'HOLA': (0, 255, 0),      # Verde
            'GRACIAS': (255, 165, 0),  # Naranja
            'TE_QUIERO': (255, 0, 0),  # Azul
            'SI': (255, 255, 0),       # Amarillo
            'NO': (0, 0, 255)          # Rojo
        }
        
        print(f"✅ Modelo cargado - Precisión: {self.model_info['accuracy']:.2%}")
        print(f"🔤 Señas: {', '.join(self.model_info['classes'])}")
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: No se puede abrir la cámara")
            return
        
        print("\n🎥 TRADUCTOR EN TIEMPO REAL")
        print("Presiona 'q' para salir\n")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Dibujar mano
                    self.mp_draw.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Extraer landmarks
                    landmarks = []
                    for lm in hand_landmarks.landmark:
                        landmarks.extend([lm.x, lm.y, lm.z])
                    
                    # Predecir
                    features = np.array(landmarks).reshape(1, -1)
                    prediction = self.model.predict(features)[0]
                    prob = np.max(self.model.predict_proba(features)[0])
                    
                    # Actualizar historial
                    self.history.append(prediction)
                    
                    if len(self.history) == 5:
                        self.current_sign = Counter(self.history).most_common(1)[0][0]
                        self.confidence = prob
                    
                    # Mostrar resultado
                    color = self.colors.get(self.current_sign, (255, 255, 255))
                    
                    # Fondo negro
                    cv2.rectangle(frame, (10, 10), (350, 90), (0, 0, 0), -1)
                    
                    # Seña detectada
                    cv2.putText(frame, f"SEÑA: {self.current_sign}", (20, 40),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    
                    # Confianza
                    cv2.putText(frame, f"Confianza: {self.confidence:.1%}", (20, 70),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
            else:
                # No hay mano
                cv2.rectangle(frame, (10, 10), (250, 50), (0, 0, 0), -1)
                cv2.putText(frame, "Esperando mano...", (20, 35),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 1)
                self.history.clear()
            
            # Instrucción
            cv2.putText(frame, "q: salir", (500, 460),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('SignTranslator - Lenguaje de Señas', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    translator = SignLanguageTranslator()
    translator.run()
