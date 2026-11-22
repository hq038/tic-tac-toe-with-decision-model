# tic-tac-toe-with-ai

Tic-tac-toe game with an AI opponent.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

## Usage

```bash
uv run tic-tac-toe
# or
uv run python -m src
```

## Decision model

`src/decision.py` provides a client for OpenRouter's Jev decision model via the
TypeSafe SDK. It is not wired into the game yet.

Set an OpenRouter API key before using it:

```bash
export OPENROUTER_API_KEY="your-api-key"
```

On PowerShell:

```powershell
$env:OPENROUTER_API_KEY = "your-api-key"
```

## Development

```bash
uv run ruff check .
uv run mypy
```
