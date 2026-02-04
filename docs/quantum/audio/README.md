# Whitepaper AI Voiceover Audio Files

This directory holds audio files for the interactive whitepaper's AI voiceover feature. When a visitor enables the voiceover toggle, audio narration plays section-by-section as they scroll through the whitepaper.

## How It Works

The whitepaper JS contains an `AUDIO_MANIFEST` mapping each section ID to an audio file path. Dropping MP3 files here with the correct filenames makes them work automatically — no code changes needed.

If a file is missing, the voiceover bar shows "audio coming soon" with no error.

## File Naming Convention

| File | Section | Whitepaper Section ID |
|------|---------|----------------------|
| `01-introduction.mp3` | 1. Introduction | `intro` |
| `02-problem.mp3` | 2. The Problem | `problem` |
| `03-hourglass.mp3` | 3. The Hourglass Architecture | `hourglass` |
| `04-coherence-metric.mp3` | 4. The Coherence Metric | `coherence-metric` |
| `05-scale-frequency.mp3` | 5. Scale-Frequency Invariance | `scale-frequency` |
| `06-qi-equation.mp3` | 6. The Quantum Integer | `qi-equation` |
| `07-decoherence.mp3` | 7. Decoherence & Threat Modeling | `decoherence` |
| `08-neural-firewall.mp3` | 8. The Neural Firewall | `neural-firewall` |
| `09-falsifiability.mp3` | 9. Falsifiability & Testable Predictions | `falsifiability` |
| `10-related-work.mp3` | 10. Related Work | `related-work` |
| `11-conclusion.mp3` | 11. Conclusion | `conclusion` |
| `12-references.mp3` | 12. References | `references` |

## Audio Generation

**Recommended approach:** Use an AI text-to-speech service to generate narration from each section's content.

**Services:**
- ElevenLabs (high quality, natural voice)
- OpenAI TTS API (`tts-1-hd` model)
- Google Cloud Text-to-Speech

**Specifications:**
- Format: MP3
- Bitrate: 128kbps
- Channels: Mono
- Each file should narrate the full text content of its corresponding section
- Keep individual files under 5 MB (~5 minutes at 128kbps mono)

## Workflow

1. Copy the text content of a whitepaper section
2. Generate audio via your preferred TTS service
3. Save as the corresponding filename (e.g., `01-introduction.mp3`)
4. Drop into this directory
5. Push to GitHub — the voiceover toggle will pick it up automatically
