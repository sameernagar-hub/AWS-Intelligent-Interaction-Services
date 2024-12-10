import boto3

rekognition = boto3.client('rekognition')

def analyze_image(image_path):
    with open(image_path, 'rb') as image:
        response = rekognition.detect_labels(
            Image={'Bytes': image.read()},
            MaxLabels=5,
            MinConfidence=75
        )
    print("Detected Labels:")
    for label in response['Labels']:
        print(f"{label['Name']} - {label['Confidence']:.2f}%")

analyze_image('C:/Users/sameernagar/Downloads/demo.jpg')
