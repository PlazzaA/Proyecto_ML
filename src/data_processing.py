import numpy as np
import pandas as pd
from utils import generar_datos_suspensos
from utils import generar_datos_aprobados

df = pd.read_csv(r'C:\Users\plaza\Desktop\Documentos_Clase\ONLINE_DS_THEBRIDGE_Alejandro_Plaza\Proyecto_ML\data\raw\StudentPerformanceFactors.csv')

Parental_Involvement = pd.get_dummies(data = df['Parental_Involvement'], prefix = 'PI').astype(int)
df = pd.concat([df, Parental_Involvement], axis = 1)

Access_to_Resources	= pd.get_dummies(data = df['Access_to_Resources'], prefix = 'AtR').astype(int)
df = pd.concat([df, Access_to_Resources], axis = 1)

df = df.select_dtypes('number')

df.drop(columns = ['Sleep_Hours', 'Physical_Activity', 'PI_Medium', 'AtR_Medium'], inplace = True)

suspensos = generar_datos_suspensos(num_muestras=3000)
df = pd.concat([df, suspensos])

aprobados = generar_datos_aprobados(num_muestras = 2000)
df = pd.concat([df, aprobados])

df.to_csv(r'C:\Users\plaza\Desktop\Documentos_Clase\ONLINE_DS_THEBRIDGE_Alejandro_Plaza\Proyecto_ML\data\processed\estudiantes.csv', index = False)