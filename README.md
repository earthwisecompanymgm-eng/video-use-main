<p align="center">
  <img src="static/video-use-banner.png" alt="video-use" width="100%">
</p>

# video-use

Introducing **video-use** — edit videos with Claude Code. 100% open source.

Drop raw footage in a folder, chat with Claude Code, get `final.mp4` back. Works for any content — talking heads, montages, tutorials, travel, interviews — without presets or menus.

## What it does

- **Cuts out filler words** (`umm`, `uh`, false starts) and dead space between takes
- **Auto color grades** every segment (warm cinematic, neutral punch, or any custom ffmpeg chain)
- **30ms audio fades** at every cut so you never hear a pop
- **Burns subtitles** in your style — 2-word UPPERCASE chunks by default, fully customizable
- **Generates animation overlays** via [HyperFrames](https://github.com/heygen-com/hyperframes), [Remotion](https://www.remotion.dev/), [Manim](https://www.manim.community/), or PIL — spawned in parallel sub-agents, one per animation
- **Self-evaluates the rendered output** at every cut boundary before showing you anything
- **Persists session memory** in `project.md` so next week's session picks up where you left off

Installation
Prerequisites
Python 3.10 or later
pip (included with Python)
Git for cloning the repository
ffmpeg — required for all video processing
Node.js 18+ (optional, needed only for Remotion-based animations)
Quick Start
git clone 
cd video-use
pip install -e .
Platform-Specific Setup
Install
git clone cd video-use-main pip install -e .



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
Create a .env file in the project root:

cp .env.example .env
Add your ElevenLabs API key:

ELEVENLABS_API_KEY=your_key_here
Verifying the Installation
python -c "import video_use; video_use.main()"
If everything is configured correctly, you will see:

video-use ready.
Troubleshooting
Issue	Solution
ffmpeg not found	Ensure ffmpeg is installed and in your PATH: ffmpeg -version
manim not found	Install with pip install manim and a LaTeX distribution
ModuleNotFoundError	Verify you are in the project directory with an active virtual environment
yt-dlp download failures	Update to the latest version: pip install -U yt-dlp
Agent Integration
Claude Code
New-Item -ItemType SymbolicLink `
  -Path "$HOME\.claude\skills\video-use" `
  -Target "$(Resolve-Path .)"
Codex
ln -sfn "$(pwd)" ~/.codex/skills/video-use
Other Agents
Register the project root as a skill or plugin directory for your agent. The agent-specific instructions are documented in SKILL.md.

Next Steps
Read SKILL.md for daily usage and editing commands
Drop raw footage into a folder
Start your agent and point it at the folder
The agent will handle transcription, editing, and rendering from there.

## How it works

The LLM never watches the video. It **reads** it — through two layers that together give it everything it needs to cut with word-boundary precision.

<p align="center">
  <img src="static/timeline-view.svg" alt="timeline_view composite — filmstrip + speaker track + waveform + word labels + silence-gap cut candidates" width="100%">
</p>

**Layer 1 — Audio transcript (always loaded).** One ElevenLabs Scribe call per source gives word-level timestamps, speaker diarization, and audio events (`(laughter)`, `(applause)`, `(sigh)`). All takes pack into a single ~12KB `takes_packed.md` — the LLM's primary reading view.

```
## C0103  (duration: 43.0s, 8 phrases)
  [002.52-005.36] S0 Ninety percent of what a web agent does is completely wasted.
  [006.08-006.74] S0 We fixed this.
```

**Layer 2 — Visual composite (on demand).** `timeline_view` produces a filmstrip + waveform + word labels PNG for any time range. Called only at decision points — ambiguous pauses, retake comparisons, cut-point sanity checks.

> Naive approach: 30,000 frames × 1,500 tokens = **45M tokens of noise**.
> Video Use: **12KB text + a handful of PNGs**.

Same idea as browser-use giving an LLM a structured DOM instead of a screenshot — but for video.

## Pipeline

```
Transcribe ──> Pack ──> LLM Reasons ──> EDL ──> Render ──> Self-Eval
                                                              │
                                                              └─ issue? fix + re-render (max 3)
```

The self-eval loop runs `timeline_view` on the _rendered output_ at every cut boundary — catches visual jumps, audio pops, hidden subtitles. You see the preview only after it passes.

## Design principles

1. **Text + on-demand visuals.** No frame-dumping. The transcript is the surface.
2. **Audio is primary, visuals follow.** Cuts come from speech boundaries and silence gaps.
3. **Ask → confirm → execute → self-eval → persist.** Never touch the cut without strategy approval.
4. **Zero assumptions about content type.** Look, ask, then edit.
5. **12 hard rules, artistic freedom elsewhere.** Production-correctness is non-negotiable. Taste isn't.

See [`SKILL.md`](./SKILL.md) for the full production rules and editing craft.
