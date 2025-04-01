from pocketflow import Flow
from nodes import GetTextNode, SelectVoiceNode, GenerateSpeechNode, SaveAudioNode, PlayAudioNode

def create_tts_flow():
    """Create and return a text-to-speech flow."""
    # Create nodes
    get_text_node = GetTextNode()
    select_voice_node = SelectVoiceNode()
    generate_speech_node = GenerateSpeechNode()
    save_audio_node = SaveAudioNode()
    play_audio_node = PlayAudioNode()
    
    # Connect nodes in sequence
    get_text_node >> select_voice_node >> generate_speech_node >> save_audio_node >> play_audio_node
    
    # Create flow starting with input node
    return Flow(start=get_text_node)

# Create a flow instance
tts_flow = create_tts_flow()