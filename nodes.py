from pocketflow import Node
from utils.call_llm import call_llm
from utils.tts_engine import generate_speech, save_audio, play_audio

class GetTextNode(Node):
    def exec(self, _):
        # Get text from user input
        user_text = input("Enter text to convert to speech: ")
        return user_text
    
    def post(self, shared, prep_res, exec_res):
        # Store the user's text
        shared["text"] = exec_res
        return "default"  # Go to the next node

class SelectVoiceNode(Node):
    def prep(self, shared):
        # No special preparation needed
        return None
    
    def exec(self, _):
        # List available voices
        voices = ["default", "male", "female", "child"]
        print("\nAvailable voices:")
        for i, voice in enumerate(voices):
            print(f"{i+1}. {voice}")
        
        # Get voice selection from user
        choice = input("\nSelect voice (enter number or name, default is 1): ")
        
        # Process user selection
        try:
            if choice.isdigit() and 1 <= int(choice) <= len(voices):
                return voices[int(choice)-1]
            elif choice.lower() in [v.lower() for v in voices]:
                return next(v for v in voices if v.lower() == choice.lower())
            else:
                print("Invalid selection, using default voice.")
                return "default"
        except:
            return "default"
    
    def post(self, shared, prep_res, exec_res):
        # Store selected voice
        shared["voice"] = exec_res
        return "default"  # Go to the next node

class GenerateSpeechNode(Node):
    def prep(self, shared):
        # Read text and voice from shared
        return {
            "text": shared["text"],
            "voice": shared["voice"],
            "speed": shared["speed"]
        }
    
    def exec(self, params):
        # Call TTS engine to generate speech
        print(f"\nGenerating speech for: '{params['text']}'")
        print(f"Using voice: {params['voice']}")
        
        return generate_speech(
            text=params["text"],
            voice=params["voice"],
            speed=params["speed"]
        )
    
    def post(self, shared, prep_res, exec_res):
        # Store the generated audio data
        shared["audio_data"] = exec_res
        return "default"  # Go to the next node

class SaveAudioNode(Node):
    def prep(self, shared):
        # Read audio data and output filename from shared
        return {
            "audio_data": shared["audio_data"],
            "output_file": shared["output_file"]
        }
    
    def exec(self, params):
        # Save audio to file
        return save_audio(
            audio_data=params["audio_data"],
            output_file=params["output_file"]
        )
    
    def post(self, shared, prep_res, exec_res):
        # Update output file path if it changed
        if exec_res:
            shared["output_file"] = exec_res
        return "default"  # Go to the next node

class PlayAudioNode(Node):
    def prep(self, shared):
        # Read output file path from shared
        return shared["output_file"]
    
    def exec(self, output_file):
        # Play the generated audio
        user_choice = input(f"\nPlay the generated audio? (y/n): ")
        
        if user_choice.lower() == 'y':
            print(f"Playing audio from {output_file}...")
            play_audio(output_file)
            return True
        else:
            print(f"Audio playback skipped.")
            return False
    
    def post(self, shared, prep_res, exec_res):
        # Nothing to update in shared
        return "default"