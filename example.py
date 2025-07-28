import onnxruntime as ort
from PIL import Image
import numpy as np
import json
import io

def load_model():
    session = ort.InferenceSession("captcha_model.onnx")
    
    with open("captcha_model_metadata.json", "r") as f:
        metadata = json.load(f)
        
    return session, metadata

def solve_captcha_image(image_bytes):
    session, metadata = load_model()
    
    # Preprocess
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    height, width = metadata["input_shape"][1:3]
    image = image.resize((width, height), Image.LANCZOS)
    
    image_array = np.array(image, dtype=np.float32)
    mean, std = metadata["normalization"]["mean"][0], metadata["normalization"]["std"][0]
    image_array = (image_array / 255.0 - mean) / std
    image_array = np.expand_dims(np.expand_dims(image_array, 0), 0)
    
    # Inference
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: image_array})
    
    # Decode
    idx_to_char = metadata["idx_to_char"]
    result = ""
    
    for pos in range(4):
        char_idx = np.argmax(outputs[pos][0])
        result += idx_to_char[str(char_idx)]
    
    return result

with open("image.png", "rb") as f:
    image_data = f.read()
    
predicted_text = solve_captcha_image(image_data)