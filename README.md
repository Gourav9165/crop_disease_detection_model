
# 🌾 Crop Disease Detection 🚜  
**Detect crop diseases and check weather conditions effortlessly using deep learning and an intuitive web interface!**

---

## 🌟 **Overview**  
Welcome to the **Crop Disease Detection project!** This Django-based web application allows users to detect crop diseases by uploading an image or providing an image URL. It leverages a **TensorFlow Lite (TFLite) model** for predictions and includes additional features like weather updates for user convenience.

## 🌟 Features  

- **Upload Images** 📷: Upload a crop image to analyze for diseases.  
- **Predict Diseases** 🔍: Powered by TensorFlow Lite for accurate predictions with confidence levels.  
- **Use URLs** 🌐: Analyze images directly from a URL.  
- **Check Weather** ☁️: Get real-time weather details based on your location.  

---

## 🛠️ Technology Stack  

- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, JavaScript  
- **Machine Learning**: TensorFlow Lite  
- **Database**: SQLite  
- **APIs Used**: OpenWeatherMap  

---

## ⚙️ Setup and Installation  

### 1️⃣ Clone the Repository  

```bash  
git clone https://github.com/Gourav9165/crop_disease_detection_model.git 
cd crop-disease-detection  
```  

### 2️⃣ Install Dependencies  

```bash  
pip install -r requirements.txt  
```  

### 3️⃣ Apply Migrations  

```bash  
python manage.py migrate  
```  

### 4️⃣ Run the Development Server  

```bash  
python manage.py runserver  
```  

Access the app at `http://127.0.0.1:8000/`. 🎉  

---

## 🔬 How It Works  

1. **Upload or Provide URL**: Use the interface to upload a crop image or provide an image URL.  
2. **Model Prediction**: The uploaded image is resized, normalized, and passed to a TensorFlow Lite model for disease detection.  
3. **Get Results**: View the predicted disease name and confidence percentage.  


## 📜 Usage Details  

- **File Upload**: Click "Upload Image" to browse and upload a file.  
- **URL Input**: Click "Enter Image URL" to analyze an image using its URL.  
- **Weather**: Access real-time weather information for your region.  

---

## 🧩 Future Enhancements  

- 🌍 Multi-language support.  
- 📊 Detailed disease treatment recommendations.  
- 📱 Mobile-friendly responsive design.   

---

## 📜 License  

This project is licensed under the MIT License.  

---

## 🌟 Acknowledgments  

- **TensorFlow Lite**: For enabling lightweight ML predictions.  
- **OpenWeatherMap API**: For weather data integration.  

---
