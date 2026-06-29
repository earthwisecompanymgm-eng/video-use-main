
video-use
Introducing video-use — edit videos with Claude Code. 100% open source.

Drop raw footage in a folder, chat with Claude Code, get final.mp4 back. Works for any content — talking heads, montages, tutorials, travel, interviews — without presets or menus.

What it does
Cuts out filler words (umm, uh, false starts) and dead space between takes
Auto color grades every segment (warm cinematic, neutral punch, or any custom ffmpeg chain)
30ms audio fades at every cut so you never hear a pop
Burns subtitles in your style — 2-word UPPERCASE chunks by default, fully customizable
Generates animation overlays via HyperFrames, Remotion, Manim, or PIL — spawned in parallel sub-agents, one per animation
Self-evaluates the rendered output at every cut boundary before showing you anything
Persists session memory in project.md so next week's session picks up where you left off
# Installation

## Prerequisites

- **Python** 3.10 or later
- **pip** (included with Python)
- **Git** for cloning the repository
- **ffmpeg** — required for all video processing
- **Node.js** 18+ (optional, needed only for Remotion-based animations)

## Quick Start


### Windows

```powershell
# 1. Clone the repository
git clone https://github.com/browser-use/video-use.git
cd video-use

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate

# 3. Install the package and its dependencies
pip install -e .

# 4. Install ffmpeg
# Download from https://ffmpeg.org/download.html and add the bin
# directory to your PATH, or use:
choco install ffmpeg

# 5. (Optional) Install yt-dlp for downloading online sources
choco install yt-dlp
```

### Linux

```bash
# Dependencies
sudo apt install ffmpeg python3-pip python3-venv yt-dlp

# Install
git clone 
cd video-use
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Optional Dependencies

### Manim (Animation Support)

For math equation animations and data visualizations:

```bash
pip install -e ".[animations]"
```

Requires a LaTeX distribution (e.g., [MiKTeX](https://miktex.org/) on Windows, `brew install latex` on macOS).

### Remotion (Programmatic Animations)

For React-based animation overlays:

```bash
cd skills/remotion
npm install
cd ../..
```

## Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Add your [ElevenLabs API key](https://elevenlabs.io/app/settings/api-keys):

```env
ELEVENLABS_API_KEY=your_key_here
```

## Verifying the Installation

```bash
python -c "import video_use; video_use.main()"
```

If everything is configured correctly, you will see:

```
video-use ready.
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ffmpeg not found` | Ensure ffmpeg is installed and in your PATH: `ffmpeg -version` |
| `manim not found` | Install with `pip install manim` and a LaTeX distribution |
| `ModuleNotFoundError` | Verify you are in the project directory with an active virtual environment |
| `yt-dlp` download failures | Update to the latest version: `pip install -U yt-dlp` |

## Agent Integration

### Claude Code

```powershell
New-Item -ItemType SymbolicLink `
  -Path "$HOME\.claude\skills\video-use" `
  -Target "$(Resolve-Path .)"
```

### Codex

```bash
ln -sfn "$(pwd)" ~/.codex/skills/video-use
```

### Other Agents

Register the project root as a skill or plugin directory for your agent. The agent-specific instructions are documented in `SKILL.md`.

## Next Steps

1. Read [`SKILL.md`](./SKILL.md) for daily usage and editing commands
2. Drop raw footage into a folder
3. Start your agent and point it at the folder

The agent will handle transcription, editing, and rendering from there.
