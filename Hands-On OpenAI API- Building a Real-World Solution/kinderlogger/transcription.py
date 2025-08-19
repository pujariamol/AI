from openai import OpenAI
import os
import glob

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)
pattern = "audio/*.ogg"  # for windows use "audio\\*.ogg"

ogg_files = glob.glob(pattern)
print(ogg_files)
for file_name in ogg_files:
    print("Transcribing file:", file_name)
    audio_file = open(file_name, "rb")
    response = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="text",
        temperature=0.2,
        prompt="ogg"
    )
    output_file = file_name.replace('.ogg', '_transcript.txt')
    with open(output_file, 'w') as f:
        f.write(response)
    print(f"Transcription saved to: {output_file}")
    # print("Transcription:", response)
    audio_file.close()