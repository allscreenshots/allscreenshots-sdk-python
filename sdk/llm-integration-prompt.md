# Allscreenshots Python SDK - LLM integration prompt

Use this prompt to help LLMs understand and work with the Allscreenshots Python SDK.

---

## SDK overview

The Allscreenshots Python SDK (`allscreenshots-sdk`) provides a client for capturing screenshots of web pages. It supports synchronous and asynchronous operations.

## Installation

```bash
pip install allscreenshots-sdk
```

## Basic usage

```python
from allscreenshots_sdk import AllscreenshotsClient

# Create client (API key from env var ALLSCREENSHOTS_API_KEY or explicit)
client = AllscreenshotsClient.builder().with_api_key("your-key").build()

# Capture screenshot
image_bytes = client.screenshots.capture("https://example.com")

# Save to file
with open("screenshot.png", "wb") as f:
    f.write(image_bytes)

client.close()
```

## Client configuration

```python
client = (
    AllscreenshotsClient.builder()
    .with_api_key("key")           # Required
    .with_timeout(120.0)           # Seconds (default: 60)
    .with_max_retries(5)           # Default: 3
    .build()
)
```

## Screenshot options

```python
image = client.screenshots.capture(
    url="https://example.com",     # Required
    device="Desktop HD",           # "Desktop HD", "iPhone 14", "iPad"
    full_page=True,                # Capture full page
    format="png",                  # "png", "jpeg", "webp", "pdf"
    quality=80,                    # 1-100 for jpeg/webp
    delay=1000,                    # Wait before capture (ms)
    wait_for=".selector",          # Wait for CSS selector
    wait_until="networkidle",      # "load", "domcontentloaded", "networkidle"
    dark_mode=True,                # Enable dark mode
    block_ads=True,                # Block ads
    block_cookie_banners=True,     # Block cookie banners
    viewport_width=1920,           # Custom width
    viewport_height=1080,          # Custom height
)
```

## Available APIs

- `client.screenshots` - Capture screenshots (sync and async jobs)
- `client.bulk` - Bulk screenshot operations
- `client.compose` - Combine multiple screenshots
- `client.schedules` - Scheduled captures
- `client.usage` - Usage and quota info

## Error handling

```python
from allscreenshots_sdk import (
    AllscreenshotsError,    # Base exception
    ValidationError,         # 400 - Bad request
    AuthenticationError,     # 401 - Invalid API key
    NotFoundError,           # 404 - Resource not found
    RateLimitError,          # 429 - Rate limited
    ServerError,             # 5xx - Server error
    TimeoutError,            # Request timeout
)

try:
    client.screenshots.capture(url)
except RateLimitError as e:
    print(f"Retry after: {e.retry_after}s")
except AllscreenshotsError as e:
    print(f"Error: {e.message}")
```

## Async usage

```python
async with AllscreenshotsClient.builder().with_api_key("key").build_async() as client:
    image = await client.screenshots.capture("https://example.com")
```

## Common tasks

### Capture with specific device
```python
image = client.screenshots.capture("https://example.com", device="iPhone 14")
```

### Full page screenshot
```python
image = client.screenshots.capture("https://example.com", full_page=True)
```

### Wait for dynamic content
```python
image = client.screenshots.capture(
    "https://example.com",
    wait_for=".content-loaded",
    wait_until="networkidle"
)
```

### Check quota
```python
quota = client.usage.get_quota()
print(f"Used: {quota.screenshots.used}/{quota.screenshots.limit}")
```
