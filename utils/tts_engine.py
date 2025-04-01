from gtts import gTTS
import tempfile
import os
from playsound import playsound

def generate_speech(text, voice="default", speed=1.0):
    """
    Generate speech from text using gTTS.
    
    Args:
        text (str): The text to convert to speech
        voice (str): Voice type (maps to language and tld in gTTS)
        speed (float): Speed factor for playback
    
    Returns:
        dict: Configuration and audio data for the generated speech
    """
    # Map voice to language and TLD
    voice_config = {
        "default": {"lang": "en", "tld": "com"},
        "male": {"lang": "en", "tld": "co.uk"},
        "female": {"lang": "en", "tld": "com.au"},
        "child": {"lang": "en", "tld": "ie"}
    }
    
    config = voice_config.get(voice, voice_config["default"])
    
    # Create a temporary file to store audio
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()
    
    # Generate TTS audio
    tts = gTTS(text=text, lang=config["lang"], tld=config["tld"], slow=(speed < 1.0))
    tts.save(temp_file.name)
    
    # Return audio data and configuration
    return {
        "temp_file": temp_file.name,
        "text": text,
        "voice": voice,
        "speed": speed
    }

def save_audio(audio_data, output_file="output.mp3"):
    """
    Save audio data to the specified output file.
    
    Args:
        audio_data (dict): Audio data from generate_speech
        output_file (str): Path to save the final audio file
    
    Returns:
        str: Path to the saved audio file
    """
    # Copy temp file to output location
    temp_file = audio_data["temp_file"]
    
    # Read temp file data
    with open(temp_file, "rb") as f:
        audio_bytes = f.read()
    
    # Write to output file
    with open(output_file, "wb") as f:
        f.write(audio_bytes)
    
    # Clean up temporary file
    try:
        os.unlink(temp_file)
    except:
        pass
    
    print(f"Audio saved to {output_file}")
    return output_file

def play_audio(audio_file):
    """
    Play the generated audio file.
    
    Args:
        audio_file (str): Path to the audio file to play
    
    Returns:
        bool: True if playback was successful, False otherwise
    """
    try:
        playsound(audio_file)
        return True
    except Exception as e:
        print(f"Error playing audio: {e}")
        return False

# Test function
if __name__ == "__main__":
    text = "Hello, this is a test of the text to speech system."
    audio_data = generate_speech(text)
    output_file = save_audio(audio_data)
    play_audio(output_file)