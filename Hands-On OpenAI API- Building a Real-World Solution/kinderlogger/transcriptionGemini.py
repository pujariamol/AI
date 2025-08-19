import google.generativeai as genai
import os

# Set your API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def transcribe_ogg_audio(file_path):
    """Transcribes an OGG audio file using the Gemini API."""

    # Upload the audio file to the Gemini API
    # The file is a genai.Part object, which the model understands
    audio_file = genai.upload_file(path=file_path)

    # Wait for the file to be processed
    while audio_file.state.name == "PROCESSING":
        print('.', end='')
        # time.sleep(1)
        audio_file = genai.get_file(name=audio_file.name)
    
    # If the file upload fails, raise an error
    if audio_file.state.name == "FAILED":
        raise ValueError(f"Failed to process file: {audio_file.state.name}")

    # Pass the audio file and a prompt to the model
    # 'gemini-1.5-pro' is a good choice for this task
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([
        "Please transcribe the following audio file:",
        audio_file
    ])

    return response.text

if __name__ == '__main__':
    # Replace with the path to your OGG file
    ogg_file = 'audio/Example.ogg'
    
    if not os.path.exists(ogg_file):
        print(f"Error: The file {ogg_file} was not found.")
    else:
        try:
            transcript = transcribe_ogg_audio(ogg_file)
            print("Transcription:")
            print(transcript)
        except ValueError as e:
            print(f"An error occurred: {e}")