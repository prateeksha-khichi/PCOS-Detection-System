
import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your CNN model

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Always resolves to the current file path
MODEL_PATH = os.path.join(BASE_DIR, "model.h5")
model = load_model(MODEL_PATH)



# Rule-based chatbot response
def generate_advice(prediction):
    if "PCOS" in prediction:
        return (
            "🌼 It looks like PCOS is detected. Here are some suggestions:\n\n"
            "- 🍎 Eat a balanced, low-carb diet.\n"
            "- 🧘 Practice yoga or regular exercise.\n"
            "- 💊 Consider consulting a doctor for hormonal medication.\n"
            "\n📢 Disclaimer: This is general advice, not a medical diagnosis."
        )
    else:
        return (
            "✅ Great! No signs of PCOS detected.\n"
            "- 🌸 Maintain a healthy lifestyle and regular cycles.\n"
            "- 🍏 Eat fruits, veggies, and whole grains.\n"
            "- 🧘 Stay active and hydrated!"
        )

# Prediction function
def pcos_predict(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    result = "PCOS Detected 🚨" if prediction[0][0] > 0.5 else "Not PCOS ✅"
    advice = generate_advice(result)
    return result, advice

# Launch Gradio Interface
iface = gr.Interface(
    fn=pcos_predict,
    inputs=gr.Image(type="pil", label="Upload Ultrasound Image"),
    outputs=[
        gr.Text(label="Prediction"),
        gr.Text(label="Health Assistant Advice"),
    ],
    title="PCOS Detection & Health Chatbot",
    description="Upload an ultrasound image to check for PCOS and get health guidance.",
    theme="default"
)

iface.launch()

