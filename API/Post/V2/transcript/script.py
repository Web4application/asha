# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your chosen API key, this is the "default" account api key
aai.settings.api_key = "3c0dbe4a8a61430d8430582e3f95aa4c"

# URL of the file to transcribe
FILE_URL = "https://cdn.assemblyai.com/upload/4328dc28473b30511b51eaf2edef7b88a59182ee593fdb84e559f31d151631f8/5a5df6c7-8c80-471c-b1ec-a2bd4b47799a"

# You can set additional parameters for the transcription
config = aai.TranscriptionConfig(
  summarization=True,
  iab_categories=True,
  content_safety=True,
  sentiment_analysis=True,
  redact_pii=True,
  speaker_labels=True,
  filter_profanity=True,
  format_text=True,
  punctuate=True,
  disfluencies=True,
  language_detection=True
)
config.language_detection_options = {
  "code_switching": true
}
config.speech_understanding = {
  "request": {
    "custom_formatting": {
      "date": "dd/mm/yyyy",
      "phone_number": "+x(xxx)xxx-xxxx",
      "email": "firstname.lastname@domain.com",
      "format_utterances": true
    },
    "translation": {
      "target_languages": [
        "en"
      ],
      "formal": true,
      "match_original_utterance": true
    },
    "speaker_identification": {
      "speaker_type": "role",
      "known_values": [
        "Asha",
        "Lola",
        "Aura",
        "Roda",
        "Kubu",
        "Host"
      ]
    }
  }
}
config.speech_models = [
  "universal"
]
config.redact_pii_policies = [
  "medical_condition",
  "banking_information",
  "credit_card_number",
  "credit_card_cvv",
  "person_name"
]
config.keyterms_prompt = [
  "Speech",
  "Voice",
  "Encoder",
  "Decoder",
  "Latent",
  "Spectrogram",
  "Mel",
  "MFCC",
  "Phoneme",
  "Prosody",
  "Attention",
  "Vocoder",
  "Translation",
  "Embedding",
  "Real-time"
]

transcriber = aai.Transcriber(config=config)
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: ", transcript.error)
    exit(1)
else:
    print(f"Transcript Text: ", transcript.text)
  
