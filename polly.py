import boto3

polly = boto3.client('polly')

def text_to_speech(text):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  # You can change to other voices like 'Matthew', 'Amy', etc.
    )
    with open('output.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())
    print("Speech saved to output.mp3")

text_to_speech("Hello, welcome to the Amazon Polly demo!")
