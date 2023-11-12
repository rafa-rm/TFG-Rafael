import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import Normalizer
from pathlib import Path


continuous = ["age", "resting bp s", "cholesterol", "max heart rate", "oldpeak"]
categorical = [
    "sex",
    "chest pain type",
    "fasting blood sugar",
    "resting ecg",
    "exercise angina",
    "ST slope",
]


pkl_path = Path(__file__).parents[1] / 'Streamlit/model.pkl'

# loading the model to predict on the data
pickle_in = open(pkl_path, "rb")
classifier = pickle.load(pickle_in)

data_path = Path(__file__).parents[1] / 'Streamlit/data_processed.csv'

# loading the dataset used in model creation
data = pd.read_csv(data_path)
data = data.drop("target", axis=1)


def welcome():
    return "welcome all"

def prediction(features):
    columns = [
        "age",
        "sex",
        "chest pain type",
        "resting bp s",
        "cholesterol",
        "fasting blood sugar",
        "resting ecg",
        "max heart rate",
        "exercise angina",
        "oldpeak",
        "ST slope",
    ]
    data_aux = pd.concat(
        [data, pd.DataFrame([features], columns=columns)], ignore_index=True
    )
    data_aux = pd.get_dummies(data_aux, columns=categorical, drop_first=True)
    scaler = Normalizer()
    data_aux[continuous] = scaler.fit_transform(data_aux[continuous])

    prediction = classifier.predict(data_aux.tail(1))
    if prediction == 1:
        return "Doença Cardíaca"
    if prediction == 0:
        return "Sem doença"
    return prediction


def main():
    st.set_page_config(layout="wide")
    st.title("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        age = st.slider("Idade", 28, 77, 36)

        rbps = st.slider("Pressão sanguínea em repouso (mm Hg)", 92, 200, 110)

        chol = st.slider("Colesterol Sérico (mg/dl)", 85, 603, 200)

        max_heart = st.slider("Máxima frequência cardíaca", 69, 202, 120)

    with col2:
        oldpeak = st.slider(
            "Oldpeak (Depressão ST induzida por exercício em relação ao repouso)",
            0.0,
            6.2,
            0.2,
            0.1,
        )

        sexOptions = ("Masculino", "Feminino")
        sex = st.selectbox("Sexo", sexOptions)

        cpOptions = (
            "Angina Típica",
            "Angina Atípica",
            "Dor não anginosa",
            "Assintomático",
        )
        cp = st.selectbox("Tipo de dor no peito", cpOptions)
        fbsOptions = ("Não", "Sim")
        fbs = st.selectbox(
            "Acúcar no sangue em jejum é maior que 120 mg/dl?", fbsOptions
        )

    with col3:
        ecgOptions = ("Normal", "Anormalidade ST-T", "Hipertrofia")
        ecg = st.selectbox("Resultado do eletrocardiograma em repouso", ecgOptions)

        exAnginaOptions = ("Não", "Sim")
        exAngina = st.selectbox("Angina induzida por exercício?", exAnginaOptions)

        slpOptions = ("Ascendente", "Plana", "Descendente")
        slp = st.selectbox("Inclinação do pico do segmento ST no exercício", slpOptions)

        result = ""
        if st.button("Predict"):
            result = prediction(
                [
                    age,
                    sexOptions.index(sex),
                    cpOptions.index(cp) + 1,
                    rbps,
                    chol,
                    fbsOptions.index(fbs),
                    ecgOptions.index(ecg),
                    max_heart,
                    exAnginaOptions.index(exAngina),
                    oldpeak,
                    slpOptions.index(slp) + 1,
                ]
            )
        if result == "Sem doença":
            st.success("A pessoa está saudável")
        if result == "Doença Cardíaca":
            st.success("A pessoa pode apresentar alguma doença cardíaca. Procure um atendimento médico!")


if __name__ == "__main__":
    main()