import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load a better healthcare-specific model
chatbot = pipeline('text-generation', model='distilgpt2')

def Healthcare_Chatbot(user_input):
    if 'symptoms' in user_input:
        return 'Please consult a doctor for accurate advice.'
    elif 'appointment' in user_input:
        return 'Would you like to schedule an appointment with a doctor?'
    elif 'medication' in user_input:
        return "It's important to take medication as prescribed by the doctor."
    elif 'fever' in user_input:
        return """Based on your symptoms of fever and sore throat, here are some things you can do to feel better:

                    ✅ Rest & Hydration: Get plenty of rest and drink warm fluids like herbal tea or warm water with honey to soothe your throat. Stay hydrated by drinking lots of water.
                    ✅ Home Remedies: Try gargling with warm salt water and using a humidifier or steam inhalation to ease discomfort. Lozenges or honey can also help! 🍯
                    ✅ Medication: If needed, you can take paracetamol or ibuprofen to reduce fever and pain (follow dosage instructions carefully!).

                    ⚠️ See a doctor if:
                    🔸 Your fever lasts more than 3 days or is above 102°F (38.9°C).
                    🔸 You have severe throat pain, trouble swallowing, or difficulty breathing.
                    🔸 You notice white patches on your throat (could be strep throat)."""
    else:
        response = chatbot(user_input, max_length=200, num_return_sequences=1) 
        return response[0]['generated_text']

# Streamlit UI
def main():
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="🩺", layout="centered")
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
            body {
                background: linear-gradient(to right, #4A90E2, #50A7C2);
                color: white;
            }
            .stApp {
                background-color: #E3F2FD;
                padding: 20px;
                border-radius: 15px;
            }
            .chat-container {
                background-color: #FFFFFF;
                padding: 15px;
                border-radius: 10px;
                color: black;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }
            .stTextInput, .stButton > button {
                font-size: 16px !important;
                border-radius: 10px !important;
            }
            .stButton > button {
                background: linear-gradient(90deg, #1D2671, #C33764);
                color: white;
                padding: 10px 15px;
                border: none;
                font-weight: bold;
                transition: 0.3s;
            }
            .stButton > button:hover {
                background: linear-gradient(90deg, #C33764, #1D2671);
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🩺 Healthcare Assistant Chatbot")
    st.markdown("### How can I assist you today?")
    
    user_input = st.text_input("Type your query here...", placeholder="e.g., What are the symptoms of flu?")
    
    if st.button("Ask Chatbot 💬"):
        if user_input:
            st.write("👤 **You:**", user_input)
            with st.spinner("Processing your query... ⏳"):
                response = Healthcare_Chatbot(user_input.lower())
            st.markdown(f'<div class="chat-container">💡<b>Chatbot:</b>  {response}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a message to get a response.")

if __name__ == '__main__':
    main()
