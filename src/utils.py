import numpy as np
import pandas as pd

def generar_datos_suspensos(num_muestras=400):
    """
    Genera datos sintéticos para estudiantes suspensos (Exam_Score < 50)
    considerando las relaciones entre las variables.

    Args:
        num_muestras (int): El número de muestras a generar. Por defecto 400.

    Returns:
        pandas.DataFrame: Un DataFrame con los datos generados.
    """
    # Inicializamos un diccionario para almacenar los datos generados
    data = {
        'Hours_Studied': [],
        'Attendance': [],
        'Previous_Scores': [],
        'Tutoring_Sessions': [],
        'Exam_Score': [],
        'PI_High': [],
        'PI_Low': [],
        'AtR_High': [],
        'AtR_Low': []
    }

    # Generamos los datos para cada muestra
    for _ in range(num_muestras):
        # Generamos las horas de estudio, con una media más baja para los suspensos
        hours_studied = np.random.normal(loc=10, scale=5)
        hours_studied = max(0, min(hours_studied, 15))  # Aseguramos que no sea negativo

        # Generamos la asistencia, también con una media más baja
        attendance = np.random.normal(loc=50, scale=10)
        attendance = max(0, min(attendance, 65))  # Aseguramos el rango 0-100

        # Generamos las notas previas, también con una media más baja
        previous_scores = np.random.normal(loc=40, scale=10)
        previous_scores = max(0, min(previous_scores, 100)) # Aseguramos el rango 0-100

        # Generamos las sesiones de tutoría, con valores bajos
        tutoring_sessions = np.random.poisson(lam=1)  # La mayoría tendrá 0 o 1

        # Generamos la nota del examen, dependiente de las otras variables
        exam_score = (0.6 * hours_studied + 0.2 * attendance + 0.1 * previous_scores +
                      2 * tutoring_sessions + np.random.normal(loc=0, scale=8))
        exam_score = max(0, min(exam_score, 49.9999))  # Aseguramos que esté por debajo de 50

        # Generamos la implicación de los padres
        pi_high = np.random.choice([0, 1], p=[0.7, 0.3])  # Más probable que sea baja implicación
        pi_low = 1 - pi_high if pi_high == 1 else np.random.choice([0, 1]) #Si PI_High es 1, PI_Low es 0

        # Generamos el acceso a recursos
        atr_high = np.random.choice([0, 1], p=[0.6, 0.4])  # Más probable que sea bajo acceso
        atr_low = 1 - atr_high if atr_high == 1 else np.random.choice([0, 1]) #Si ATR_High es 1, ATR_Low es 0

        # Añadimos los datos generados al diccionario
        data['Hours_Studied'].append(round(hours_studied))
        data['Attendance'].append(round(attendance))
        data['Previous_Scores'].append(round(previous_scores))
        data['Tutoring_Sessions'].append(round(tutoring_sessions))
        data['Exam_Score'].append(round(exam_score))
        data['PI_High'].append(round(pi_high))
        data['PI_Low'].append(round(pi_low))
        data['AtR_High'].append(round(atr_high))
        data['AtR_Low'].append(round(atr_low))

    # Convertimos el diccionario a un DataFrame
    df = pd.DataFrame(data)
    return df


def generar_datos_aprobados(num_muestras=400):
    """
    Genera datos sintéticos para estudiantes aprobados (Exam_Score > 80)
    considerando las relaciones entre las variables.

    Args:
        num_muestras (int): El número de muestras a generar. Por defecto 400.

    Returns:
        pandas.DataFrame: Un DataFrame con los datos generados.
    """
    # Inicializamos un diccionario para almacenar los datos generados
    data = {
        'Hours_Studied': [],
        'Attendance': [],
        'Previous_Scores': [],
        'Tutoring_Sessions': [],
        'Exam_Score': [],
        'PI_High': [],
        'PI_Low': [],
        'AtR_High': [],
        'AtR_Low': []
    }

    # Generamos los datos para cada muestra
    for _ in range(num_muestras):
        # Generamos las horas de estudio, con una media más alta para los aprobados
        hours_studied = np.random.normal(loc=30, scale=10)
        hours_studied = max(10, min(hours_studied, 60))  # Aseguramos que no sea negativo

        # Generamos la asistencia, también con una media más alta
        attendance = np.random.normal(loc=90, scale=5)
        attendance = max(85, min(attendance, 100))  # Aseguramos el rango 70-100

        # Generamos las notas previas, también con una media más alta
        previous_scores = np.random.normal(loc=85, scale=8)
        previous_scores = max(50, min(previous_scores, 100))

        # Generamos las sesiones de tutoría, con valores más altos, pero con menos varianza
        tutoring_sessions = np.random.poisson(lam=3)  # La mayoría tendrá 2 o 3

        # Generamos la nota del examen, dependiente de las otras variables, con media más alta
        exam_score = (0.6 * hours_studied + 0.2 * attendance + 0.1 * previous_scores +
                      2 * tutoring_sessions + np.random.normal(loc=10, scale=5))
        exam_score = max(80, min(exam_score, 100))  # Aseguramos que esté por encima de 80

        # Generamos la implicación de los padres
        pi_high = np.random.choice([0, 1], p=[0.9, 0.1])  # Más probable que sea alta implicación
        pi_low = 1 - pi_high if pi_high == 1 else np.random.choice([0, 1])

        # Generamos el acceso a recursos
        atr_high = np.random.choice([0, 1], p=[0.8, 0.2])  # Más probable que sea alto acceso
        atr_low = 1 - atr_high if atr_high == 1 else np.random.choice([0, 1])

        # Añadimos los datos generados al diccionario
        data['Hours_Studied'].append(round(hours_studied))
        data['Attendance'].append(round(attendance))
        data['Previous_Scores'].append(round(previous_scores))
        data['Tutoring_Sessions'].append(round(tutoring_sessions))
        data['Exam_Score'].append(round(exam_score))
        data['PI_High'].append(round(pi_high))
        data['PI_Low'].append(round(pi_low))
        data['AtR_High'].append(round(atr_high))
        data['AtR_Low'].append(round(atr_low))

    # Convertimos el diccionario a un DataFrame
    df = pd.DataFrame(data)
    return df