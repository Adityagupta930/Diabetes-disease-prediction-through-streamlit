# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set page configuration
# st.set_page_config(page_title="Health Assistant",
#                    layout="wide",
#                    page_icon="🧑‍⚕️")

# diabetis_model = pickle.load(open('E:\Project\disease\model\diabetes_model.sav','rb'))

# st.title("Diabetis prediction system")
# col1, col2, col3 = st.columns(3)

# with col1:
#     Pregnancies = st.text_input('Number of Pregnancies')

# with col2:
#     Glucose = st.text_input('Glucose Level')

# with col3:
#     BloodPressure = st.text_input('Blood Pressure value')

# with col1:
#     SkinThickness = st.text_input('Skin Thickness value')

# with col2:
#     Insulin = st.text_input('Insulin Level')

# with col3:
#     BMI = st.text_input('BMI value')

# with col1:
#     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

# with col2:
#     Age = st.text_input('Age of the Person')
    
# diabetis_dia=''



# user_input=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
#                       BMI, DiabetesPedigreeFunction, Age]
# user_input=[float(x) for x in user_input]
# diab_prediction= diabetis_model.predict([user_input])
# if diab_prediction[0] == 1:
#     diab_diagnosis = 'The person is diabetic'
# else:
#     diab_prediction = 'The person is not diabetic'
# st.success(diabetis_dia)
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Companion",
                   layout="wide",
                   page_icon="🚀",
                   initial_sidebar_state="expanded")

# Load the pre-trained model
diabetis_model = pickle.load(open('E:\Project\disease\model\diabetes_model.sav', 'rb'))

# Custom function to get a friendly diagnosis message
def get_diagnosis_message(prediction):
    if prediction == 1:
        message = "💊 It appears that you may have diabetes based on the provided information. We recommend consulting a healthcare professional for proper diagnosis and treatment."
    else:
        message = "💚 Great news! Based on the information you provided, you are unlikely to have diabetes. However, it's always a good idea to maintain a healthy lifestyle and get regular check-ups."
    return message

# Streamlit app
st.title("🩺 Diabetes Prediction System")

# Sidebar navigation menu
selected = option_menu(
    menu_title="Navigation",
    options=["Prediction", "Information"],
    icons=["activity", "info-circle"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# Prediction page
if selected == "Prediction":
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, step=0.1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=0.1)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=0.1)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, step=0.1)
        BMI = st.number_input('BMI value', min_value=0.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.42, step=0.001)

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)

    if st.button("Predict"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetis_model.predict([user_input])
        diagnosis_message = get_diagnosis_message(diab_prediction[0])
        st.success(diagnosis_message)

# Information page
elif selected == "Information":
    st.header("🔍 About Diabetes")
    st.write("""
    Diabetes is a chronic condition characterized by high levels of blood glucose (sugar) due to the body's inability to produce or effectively use insulin, a hormone that regulates blood sugar levels. There are two main types of diabetes:

    1. **Type 1 Diabetes**: This type occurs when the body's immune system attacks and destroys the insulin-producing cells in the pancreas. As a result, the body cannot produce insulin, and people with type 1 diabetes require daily insulin injections or an insulin pump to regulate their blood sugar levels.

    2. **Type 2 Diabetes**: This is the most common form of diabetes, accounting for around 90% of all cases. It occurs when the body becomes resistant to insulin or doesn't produce enough insulin to maintain normal blood sugar levels. Type 2 diabetes is often associated with lifestyle factors such as obesity, physical inactivity, and an unhealthy diet.

    Early diagnosis and proper management of diabetes are crucial to prevent or delay complications such as heart disease, stroke, kidney disease, nerve damage, and vision problems.

    If you have any concerns or questions about diabetes, please consult a healthcare professional for personalized advice and guidance.
    """)

# Run the Streamlit app
if __name__ == "__main__":
    st.sidebar.markdown("""
    <h3 style='text-align: center; color: #02ab21;'>Health Companion</h3>
    <p style='text-align: center;'>Your journey to wellness starts here.</p>
    """, unsafe_allow_html=True)
    st.sidebar.image('images.jpeg', use_column_width=True)