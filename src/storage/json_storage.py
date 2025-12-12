import json
import os

class JSONStorage:
    def __init__(self, filename="data/entradas.json"):
        self.filename = filename
        self._ensure_directories()

    def _ensure_directories(self):
        # Crear carpeta "data" si no existe
        folder = os.path.dirname(self.filename)
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[✔] Carpeta creada: {folder}")

        # Crear archivo inicial si no existe
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
            print(f"[✔] Archivo JSON creado: {self.filename}")

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("[✔] Datos guardados en JSON")
