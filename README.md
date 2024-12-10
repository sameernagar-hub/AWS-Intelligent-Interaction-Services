# AWS Intelligent Interaction Services

## Description

AWS Intelligent Interaction Hub is a web application that integrates three powerful AWS services:

- **AWS Translate** for text translation.
- **AWS Polly** for text-to-speech conversion.
- **AWS Rekognition** for image analysis.

The application allows users to interact with these services through a simple and intuitive interface. Users can enter text to be translated, convert text into speech, and upload images to analyze using AWS's machine learning models. The hub also includes a dark mode toggle and a dynamic interface for improved user experience.

## Features

- **Text Translation**: Translates entered text between languages using AWS Translate.
- **Text-to-Speech**: Converts text to lifelike speech using AWS Polly.
- **Image Analysis**: Analyzes images to detect labels using AWS Rekognition.
- **Dark Mode**: Toggle between light and dark mode for the interface.
- **User-friendly Interface**: Interactive and responsive UI with Bootstrap.

## Technologies Used

- **AWS Services**: 
  - AWS Translate
  - AWS Polly
  - AWS Rekognition
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Deployment**: Can be deployed on any server with Python support (e.g., AWS EC2, Heroku).

## Prerequisites

- Python 3.x
- Flask
- AWS Account with access to AWS Translate, Polly, and Rekognition services.
- Basic knowledge of HTML, CSS, JavaScript, and API integration.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/AWS-Intelligent-Interaction-Services.git
   cd AWS-Intelligent-Interaction-Services
   ```

2. **Install dependencies**:

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**:

   Ensure that your AWS credentials are configured with the necessary access to AWS Translate, Polly, and Rekognition services. You can set this up using the AWS CLI:

   ```bash
   aws configure
   ```

   Provide your AWS Access Key, Secret Key, region, and output format.

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

   The server will start, and you can access the application in your browser at `http://127.0.0.1:5000`.

## Usage

- **Translate Text**: Input any text, select the source and target languages, and click "Translate" to get the translation.
- **Convert Text to Speech**: Enter text in the provided text box and click "Generate Speech" to listen to the converted audio.
- **Analyze Image**: Upload an image and click "Analyze Image" to get the labels detected by AWS Rekognition.
- **Dark Mode**: Click the moon/sun button to toggle between light and dark modes.

## Contributing

Feel free to fork the repository and contribute to the project. Any improvements, bug fixes, or suggestions are welcome.

### Steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sameer Nagar

## Acknowledgements

- [AWS Documentation](https://aws.amazon.com/documentation/) for providing the powerful services used in this project.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the responsive front-end design.
