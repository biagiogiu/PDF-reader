from gui import MyWindow
from pdf_parser import MyParser
from google.cloud import texttospeech


# Instantiates a client
client = texttospeech.TextToSpeechClient()


def read_pdf(window):
    if window.folder_path == "":
        window.empty_path()
    else:
        sentences = MyParser(window.folder_path)
        if sentences is not None:
            print(sentences.records)
            for i, record in enumerate(sentences.records[:3]):
                # Set the text input to be synthesized
                synthesis_input = texttospeech.SynthesisInput(text=record)
                # Build the voice request, select the language code ("en-US") and the ssml
                # voice gender ("neutral")
                voice = texttospeech.VoiceSelectionParams(
                    language_code="it-IT", ssml_gender=texttospeech.SsmlVoiceGender.MALE
                )

                # Select the type of audio file you want returned
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3
                )

                # Perform the text-to-speech request on the text input with the selected
                # voice parameters and audio file type
                response = client.synthesize_speech(
                    input=synthesis_input, voice=voice, audio_config=audio_config
                )

                # The response's audio_content is binary.
                with open(f"output_{i}.mp3", "wb") as out:
                    # Write the response to the output file.
                    out.write(response.audio_content)
                    print(f'Audio content written to file "output_{i}.mp3"')


root = MyWindow()
root.btnRead.bind("<Button-1>", lambda event, window=root: read_pdf(window))


root.mainloop()
