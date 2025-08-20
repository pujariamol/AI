from openai import OpenAI
import os
import glob
from pathlib import Path

def transcribe(file_name):
    print("Transcribing file:", file_name)
    audio_file = open(file_name, "rb")
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="text",
        temperature=0.2,
        prompt="ogg wav"
    )
    # output_file = file_name.replace('.ogg', '_transcript.txt')
    # with open(output_file, 'w') as f:
    #     f.write(transcription)
    # print(f"Transcription saved to: {output_file}")
    # # print("Transcription:", transcription)
    # audio_file.close()
    return transcription

def translate_to_english(file_name):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role":"system", "content":"You are a helpful assistant."},
            {"role":"user", "content":
                f"""
                Translate into English the following text that is surrounded by 3 stars (***).
                Create a JSON document with the following element:
                - Put the translated text here.
                - audio_file_name. The Value must be: {file_name}
                ***
                {transcription}
                ***
                """
            }
        ], response_format={"type":"json_object"}
    )
    return completion

if __name__ == '__main__':
    key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=key)

    folder_path = "audio"
    formats_to_read = ["*.ogg", "*.wav"]

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    for file_format in formats_to_read:
        all_files = glob.glob(f"{folder_path}/{file_format}")
        for file_name in all_files:
            transcription = transcribe(file_name)
            translated_json = translate_to_english(file_name)
            json_file_name = Path(file_name).stem

            with open(f"{output_dir}/{json_file_name}.json", "w") as file:
                file.write(translated_json.choices[0].message.content)
        
            print("Done!!")
    