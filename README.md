## QR Code Decoder
This is a web application that allows users to upload an image containing a QR code and return the decoded data. The project uses Flask for the backend and OpenCV for QR code detection and decoding.

### Technologies Used

 - Flask (Python web framework)
 - OpenCV (for QR code detection and decoding)
 - HTML, CSS, JavaScript (for the frontend)

### Installation
 Clone the repository:

     git clone https://github.com/prajjawal-kansara/Decode-QR.git
     cd Decode-QR
 
### Install the required dependencies:

      pip install -r requirements.txt

### Run the Flask app:

      python main.py

Open your browser and go to http://127.0.0.1:5000/ to use the application.

### Project Structure

      Decode-QR/
      ├── main.py              # Backend Flask application
      ├── uploads/             # Folder to store uploaded images
      ├── templates/
      │   └── index.html       # Frontend HTML template
      └── requirements.txt     # Dependencies

### Requirements

  - Python 3.x
  - Flask
  - OpenCV
