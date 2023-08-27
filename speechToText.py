import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file_path):
    # Load the MP3 audio file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Convert the audio to WAV format
    wav_file_path = mp3_file_path.replace(".mp3", ".wav")
    audio.export(wav_file_path, format="wav")
    
    return wav_file_path

def convert_speech_to_text(audio_file_path="recorded/recorded-audio.wav"):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file

    try:
        # Recognize the audio using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print(text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    
    return None

# if __name__ == "__main__":
#     mp3_audio_file_path = "./../recorded/recorded-audio.wav"  # Replace with the path to your MP3 audio file
#     wav_audio_file_path = convert_mp3_to_wav(mp3_audio_file_path)
    
#     if wav_audio_file_path:
#         print(f"Converted MP3 to WAV: {wav_audio_file_path}")
        
#         result = convert_speech_to_text(wav_audio_file_path)
        
#         if result:
#             print("Text from audio:")
#             print(result)

convert_speech_to_text()
