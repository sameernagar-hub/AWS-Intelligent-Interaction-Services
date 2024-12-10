import boto3

translate = boto3.client('translate')

def translate_text(text, source_lang, target_lang):
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    print(f"Translated text: {response['TranslatedText']}")

translate_text("Hello, how are you?", "en", "es")
