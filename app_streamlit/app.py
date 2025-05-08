import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV  # Importamos GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error # Importamos las metricas

# Cargamos los datos
df = pd.read_csv(r'C:\\Users\\plaza\\Desktop\\Documentos_Clase\\ONLINE_DS_THEBRIDGE_Alejandro_Plaza\\Proyecto_ML\\data\\processed\\estudiantes.csv')
X = df.drop(columns='Exam_Score')
y = df['Exam_Score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Movemos esto aquí

# Cargar el modelo previamente entrenado
try:
    with open(r'C:\Users\plaza\Desktop\Documentos_Clase\ONLINE_DS_THEBRIDGE_Alejandro_Plaza\Proyecto_ML\models\modelo_final.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    # Si el modelo no se encuentra, entrena uno de nuevo (o carga un modelo por defecto)
    st.warning("Modelo no encontrado. Entrenando un modelo por defecto.")


    # Definir y entrenar el modelo
    #model = RandomForestRegressor(n_estimators=100, max_depth=5, max_leaf_nodes=20, random_state=42)  # Parámetros de ejemplo
    #model.fit(X_train, y_train)

    # Definir la cuadrícula de parámetros para GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Crear un objeto GridSearchCV
    grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42),  # Aseguramos la reproducibilidad
                               param_grid=param_grid,
                               cv=5,  # Validación cruzada de 5 pliegues
                               scoring='r2',  # Usamos R2 como métrica para la optimización
                               verbose=1,  # Muestra el progreso del entrenamiento
                               n_jobs=-1) # Usa todos los procesadores disponibles

    # Entrenar el modelo usando GridSearchCV
    grid_search.fit(X_train, y_train)

    # Obtener el mejor modelo
    model = grid_search.best_estimator_
    st.write(f"Mejores parámetros encontrados: {grid_search.best_params_}") # Mostramos los mejores parametros

    # Guardar el modelo
    with open('random_forest_model.pkl', 'wb') as file:
        pickle.dump(model, file)

# Datos de ejemplo para usuarios registrados
usuarios_registrados = {
    "admin@thebridge.com": "Adm1nguel"
}

# Definir las páginas de la aplicación
def pagina_inicio():
    st.title("Bienvenido a la App de Predicción de Notas")
    st.write("Por favor, regístrate o inicia sesión para continuar.")
    if st.button("Registrarse/Iniciar Sesión"):
        st.session_state.pagina_actual = "pagina_registro"

def pagina_registro():
    st.title("Registro/Inicio de Sesión")
    opcion = st.radio("Elige una opción:", ["Iniciar sesión", "Crear una cuenta", "Acceder como invitado"])

    if opcion == "Crear una cuenta":
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")
        email = st.text_input("Correo")
        contrasena = st.text_input("Contraseña", type="password")
        if st.button("Crear cuenta"):
            # Aquí iría la lógica para guardar el nuevo usuario en una base de datos
            st.success(f"Cuenta creada para {email}. Por favor, inicia sesión.")
            st.session_state.pagina_actual = "pagina_prediccion" # Para ir directamente a la predicción
            st.session_state.email = email  # Guardar el email del usuario
    elif opcion == "Iniciar sesión":
        email = st.text_input("Correo")
        contrasena = st.text_input("Contraseña", type="password")
        if st.button("Iniciar sesión"):
            if email in usuarios_registrados and usuarios_registrados[email] == contrasena:
                st.success("Inicio de sesión exitoso.")
                st.session_state.pagina_actual = "pagina_prediccion"
                st.session_state.email = email  # Guardar el email
            else:
                st.error("Correo o contraseña incorrectos.")
    elif opcion == "Acceder como invitado":
        st.success("Accediendo como invitado.")
        st.session_state.pagina_actual = "pagina_prediccion"
        st.session_state.email = "invitado"  # Establecer email como invitado
        st.session_state.invitado_usado = False # Para controlar el uso del invitado

def pagina_prediccion():
    st.title("Predicción de Nota del Examen")
    st.write(f"Bienvenido, {st.session_state.email}!") # Mostramos el email

    # Campos para los datos del estudiante
    hours_studied = st.slider("Horas estudiadas (h)", min_value=0, max_value=50, value=0)
    attendance = st.slider("Atención en clase (%)", min_value=0, max_value=100, value=0)
    previous_scores = st.number_input("Notas anteriores", min_value=0, max_value=100, value=None, placeholder="Ingresar valor...")
    tutoring_sessions = st.number_input("Sesiones de Tutoría", min_value=0, max_value=10, value=0, placeholder="Ingresar valor...")

    # Inicializar el estado de los botones si no existen
    if 'pi_high_state' not in st.session_state:
        st.session_state.pi_high_state = False
    if 'pi_low_state' not in st.session_state:
        st.session_state.pi_low_state = False

    if 'atr_high_state' not in st.session_state:
        st.session_state.atr_high_state = False
    if 'atr_low_state' not in st.session_state:
        st.session_state.atr_low_state = False

    # Selector para Parental Influence
    st.subheader("Parental Influence")
    pi_high_checkbox = st.checkbox("High", value=st.session_state.pi_high_state)
    pi_low_checkbox = st.checkbox("Low", value=st.session_state.pi_low_state)

    # Lógica para asegurar que solo un botón esté activo
    if pi_high_checkbox and not st.session_state.pi_high_state:
        st.session_state.pi_high_state = True
        st.session_state.pi_low_state = False
    elif pi_low_checkbox and not st.session_state.pi_low_state:
        st.session_state.pi_low_state = True
        st.session_state.pi_high_state = False

    pi_high = 1 if st.session_state.pi_high_state else 0
    pi_low = 1 if st.session_state.pi_low_state else 0


    # Selector para Access to Resources
    st.subheader("Access to Resources")
    atr_high_toggle = st.toggle("High", value=st.session_state.atr_high_state)
    atr_low_toggle = st.toggle("Low", value=st.session_state.atr_low_state)

    # Lógica para asegurar que solo un botón esté activo
    if atr_high_toggle and not st.session_state.atr_high_state:
        st.session_state.atr_high_state = True
        st.session_state.atr_low_state = False
    elif atr_low_toggle and not st.session_state.atr_low_state:
        st.session_state.atr_low_state = True
        st.session_state.atr_high_state = False

    atr_high = 1 if st.session_state.atr_high_state else 0
    atr_low = 1 if st.session_state.atr_low_state else 0

    boton_predecir_deshabilitado = False
    mensaje_predecir = "Predecir Nota"

    if st.session_state.email != "invitado":
        if not st.session_state.email.endswith("@thebridge.com"):
            boton_predecir_deshabilitado = True
            mensaje_predecir = "No se puede predecir (correo no es @thebridge.com)"
    else:
        if 'invitado_usado' in st.session_state and st.session_state.invitado_usado:
            boton_predecir_deshabilitado = True
            mensaje_predecir = "Invitado: Predicción ya realizada"
        else:
            st.warning("Accediendo como invitado. La predicción solo se permitirá una vez.")


    if st.button(mensaje_predecir, disabled=boton_predecir_deshabilitado):
        # Asegurarse de que los campos requeridos tienen valores
        if  attendance is not None and previous_scores is not None:
            # Crear un DataFrame con los datos de entrada
            input_data = pd.DataFrame({
                'Hours_Studied': [hours_studied],
                'Attendance': [attendance],
                'Previous_Scores': [previous_scores],
                'Tutoring_Sessions': [tutoring_sessions],
                'PI_High': [pi_high],
                'PI_Low': [pi_low],
                'AtR_High': [atr_high],
                'AtR_Low': [atr_low]
            })
            input_data = input_data.fillna(0)
            # Realizar la predicción
            predicted_grade = model.predict(input_data)[0]
            r2 = r2_score(y_test, model.predict(X_test))
            mse = mean_squared_error(y_test, model.predict(X_test))
            st.success(f"La nota predicha es: {predicted_grade:.2f}")
            # st.write(f"R2 del modelo: {r2:.2f}")
            # st.write(f"MSE del modelo: {mse:.2f}")
            if st.session_state.email == "invitado":
                st.session_state.invitado_usado = True # Marca al invitado como usado
        else:
            st.error("Por favor, ingrese valores para 'Atención en clase (%)' y 'Puntuaciones Previas.'")

# Configuración de la aplicación
def main():
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "pagina_inicio"

    if st.session_state.pagina_actual == "pagina_inicio":
        pagina_inicio()
    elif st.session_state.pagina_actual == "pagina_registro":
        pagina_registro()
    elif st.session_state.pagina_actual == "pagina_prediccion":
        pagina_prediccion()

if __name__ == "__main__":
    main()
