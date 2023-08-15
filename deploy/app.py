import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import Normalizer

continuous = ["age", "resting bp s", "cholesterol", "max heart rate", "oldpeak"]
categorical = [
    "sex",
    "chest pain type",
    "fasting blood sugar",
    "resting ecg",
    "exercise angina",
    "ST slope",
]


# loading in the model to predict on the data
pickle_in = open("../model.pkl", "rb")
classifier = pickle.load(pickle_in)

# loading the dataset used in model creation
data = pd.read_csv("../data_processed.csv")
data = data.drop("target", axis=1)


def welcome():
    return "welcome all"


# defining the function which will make the prediction using
# the data which the user inputs
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


# this is the main function in which we define our webpage
def main():
    st.set_page_config(layout="wide")
    # giving the webpage a title
    st.title("Heart Disease Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed

    # this line allows us to display the front end aspects we have
    # defined in the above code
    # st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        age = st.slider("Idade", 23, 77, 30)

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

        # the below line ensures that when the button called 'Predict' is clicked,
        # the prediction function defined above is called to make the prediction
        # and store it in the variable result

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
            st.success("A pessoa pode apresentar alguma doença cardíaca")


if __name__ == "__main__":
    main()