<h1 align="center">AI Agent Text-to-Speech Framework</h1>

<p align="center">
  <em>A flexible Text-to-Speech agent built with PocketFlow</em>
</p>

## Overview

This project implements a Text-to-Speech (TTS) agent using the PocketFlow framework. It allows users to convert text to speech with different voice options and save/play the generated audio.

## Features

- Convert text to speech with multiple voice options
- Save generated audio to file
- Play audio directly from the application
- Extensible node-based architecture

## Installation

```bash
# Clone the repository
git clone https://github.com/aixiasang/ai-agent-tts.git
cd ai-agent-tts

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Follow the interactive prompts to:
1. Enter the text you want to convert to speech
2. Select a voice option
3. Generate and save the audio
4. Play the generated audio

## Extending the Framework

You can extend this framework by:

1. Adding new voice options in `utils/tts_engine.py`
2. Creating new nodes in `nodes.py`
3. Modifying the flow in `flow.py`

## License

MIT