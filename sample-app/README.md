# Allscreenshots Demo

A simple Flask web application demonstrating the Allscreenshots Python SDK.

## Features

- URL input field
- Device selector (Desktop HD, iPhone 14, iPad)
- Full page capture toggle
- Real-time screenshot preview
- Error handling with user-friendly messages

## Prerequisites

- Python 3.10 or higher
- An Allscreenshots API key

## Setup

### 1. Install dependencies

Using uv (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 2. Set your API key

```bash
export ALLSCREENSHOTS_API_KEY="your-api-key"
```

### 3. Run the application

Using uv:

```bash
uv run python app.py
```

Or directly with Python:

```bash
python app.py
```

The application will be available at http://localhost:5000

## Configuration

Environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `ALLSCREENSHOTS_API_KEY` | Your Allscreenshots API key | Required |
| `PORT` | Server port | 5000 |
| `FLASK_DEBUG` | Enable debug mode | false |

## Development

To run in development mode with auto-reload:

```bash
FLASK_DEBUG=true uv run python app.py
```

## Usage

1. Open http://localhost:5000 in your browser
2. Enter a URL to capture
3. Select a device preset
4. Toggle "Full page" if you want to capture the entire page
5. Click "Take Screenshot"
6. The screenshot will appear in the result area

## License

Apache License 2.0
