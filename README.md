
# 🌾 Crop Disease Detection using Deep Learning

Welcome to the Crop Disease Detection project! This Django-based web application allows users to detect crop diseases by uploading an image or entering an image URL. The application utilizes a TensorFlow Lite model to predict the disease and provides the result with an accuracy score.

## 🛠️ Features
- **Upload Image**: Upload an image from your device to detect crop diseases.
- **Enter Image URL**: Provide an image URL for disease detection.
- **Modern UI**: Clean and modern user interface with nature-inspired themes.

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- Django 3.0+
- TensorFlow Lite
- PIL (Pillow)
- Requests library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crop-disease-detection.git
   cd crop-disease-detection
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Django project:**
   ```bash
   python manage.py migrate
   ```

5. **Load the TensorFlow Lite model and labels:**
   - Place your `.tflite` model and `labels.txt` file in the appropriate directory.
   - Update the paths in `views.py`:
     ```python
     model_path = "path_to_your_model.tflite"
     labels_path = "path_to_your_labels.txt"
     ```

### Running the Application

1. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Open your web browser and navigate to `http://127.0.0.1:8000`.

### File Structure
- `views.py`: Handles the image upload and prediction logic.
- `templates/`: Contains the HTML files for the web pages.
- `static/`: Stores the CSS and JS files for the UI.
- `models.py`: Defines the data models for the project.



## 🤝 Contributing

Feel free to contribute to this project by submitting pull requests, reporting issues, or suggesting features.

