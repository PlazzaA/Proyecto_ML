# 📊 ¿A(Proba)ré? - Predicción del Éxito Académico  

**¡Tranquilidad y control en tus manos!**  
Herramienta de Machine Learning para predecir el rendimiento académico de estudiantes basado en sus hábitos y desempeño previo.  

---

## 🚀 Descripción del Proyecto  
¿A(Proba)ré? es una aplicación web que utiliza un modelo de **Random Forest Regressor** para predecir las calificaciones futuras de estudiantes, analizando variables como:  
- Horas de estudio  
- Asistencia a clases  
- Notas previas  
- Participación en tutorías  
- Atención en clase  

El nombre es un juego de palabras entre *"¿Aprobaré?"* y *"Probabilidad"*, reflejando el enfoque estadístico del proyecto.  

---

## 📂 Estructura del Proyecto  

```
Proyecto_ML/  
├── app_streamlit/            # Aplicación web interactiva  
│   └── app.py                # Código principal de Streamlit  
├── data/  
│   ├── processed/            # Datos limpios (estudiantes.csv, dfdefinitivo.csv)  
│   ├── raw/                  # Datos brutos (Kaggle)  
│   ├── test/                 # Conjunto de prueba  
│   └── train/                # Conjunto de entrenamiento  
├── docs/                     # Documentación del modelo de negocio y gráficas  
├── models/  
│   └── modelo_final.pkl      # Modelos entrenados  
├── notebooks/                # Análisis y desarrollo  
│   ├── Fuentes_y_Dataset.ipynb  
│   ├── Gráficos.ipynb
│   ├── GridSearch.ipynb  
│   ├── lassoR_ridgeR.ipynb
│   ├── LimpiezaDataset.ipynb  
│   ├── LinearReg.ipynb
│   ├── NuevoDataset.ipynb  
│   ├── PolyReg.ipynb   
│   └── random_forest.ipynb  
└── src/  
    ├── .gitattributes  
    └── README.md             # Este archivo
```

---

## 🔍 Contexto Técnico  
- **Dataset**: Original de Kaggle ([enlace al dataset](https://www.kaggle.com/)) con métricas de desempeño estudiantil.  
- **Limpieza**: Procesamiento en `LimpiezaDataset.ipynb` para manejar valores nulos y outliers.  
- **Modelo**: **Random Forest Regressor** entrenado para predecir notas finales.  
- **Stack**: Python, Pandas, Scikit-learn, Streamlit.  

---

## ✨ Beneficios para Padres  
✅ **Transparencia**: Predicciones objetivas basadas en datos.  
✅ **Detección temprana**: Identifica riesgos académicos antes de que sea tarde.  
✅ **Comunicación**: Facilita diálogos constructivos con profesores y estudiantes.  

---

## 🛠️ Instalación y Uso  
1. Clonar el repositorio:  
   ```
   git clone [URL_del_repositorio]
   cd Proyecto_ML
   ```

2. Instalar dependencias
   ```
   pip install -r requirements.txt
   ```
   
3. Ejecutar la app
  ```
  streamlit run app_streamlit/app.py
  ```
