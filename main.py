from flow import tts_flow

def main():
    shared = {
        "text": "Welcome to the AI agent Text-to-Speech system.",
        "voice": "default",
        "speed": 1.0,
        "output_file": "output.mp3",
        "audio_data": None
    }

    tts_flow.run(shared)
    print(f"Text: {shared['text']}")
    print(f"Voice: {shared['voice']}")
    print(f"Generated audio saved to: {shared['output_file']}")

if __name__ == "__main__":
    main()