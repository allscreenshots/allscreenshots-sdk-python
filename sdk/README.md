# Allscreenshots Python SDK

A Python SDK for the [Allscreenshots](https://allscreenshots.com) API, enabling you to capture screenshots of web pages programmatically.

## Installation

### Using pip

```bash
pip install allscreenshots-sdk
```

### Using uv

```bash
uv add allscreenshots-sdk
```

## Quick start

```python
from allscreenshots_sdk import AllscreenshotsClient

# Create a client (reads API key from ALLSCREENSHOTS_API_KEY env var)
client = AllscreenshotsClient.builder().build()

# Or explicitly provide the API key
client = AllscreenshotsClient.builder().with_api_key("your-api-key").build()

# Capture a screenshot
image_bytes = client.screenshots.capture("https://example.com")

# Save to file
with open("screenshot.png", "wb") as f:
    f.write(image_bytes)

# Clean up
client.close()
```

### Using context manager

```python
from allscreenshots_sdk import AllscreenshotsClient

with AllscreenshotsClient.builder().with_api_key("your-api-key").build() as client:
    image = client.screenshots.capture("https://example.com", device="Desktop HD")
    with open("screenshot.png", "wb") as f:
        f.write(image)
```

### Async usage

```python
import asyncio
from allscreenshots_sdk import AllscreenshotsClient

async def main():
    async with AllscreenshotsClient.builder().with_api_key("your-api-key").build_async() as client:
        image = await client.screenshots.capture("https://example.com")
        with open("screenshot.png", "wb") as f:
            f.write(image)

asyncio.run(main())
```

## Configuration options

```python
client = (
    AllscreenshotsClient.builder()
    .with_api_key("your-api-key")          # Required (or set ALLSCREENSHOTS_API_KEY env var)
    .with_base_url("https://custom.api")   # Optional: Custom API endpoint
    .with_timeout(120.0)                   # Optional: Request timeout in seconds (default: 60)
    .with_max_retries(5)                   # Optional: Max retry attempts (default: 3)
    .with_retry_delay(2.0)                 # Optional: Initial retry delay (default: 1.0)
    .with_max_retry_delay(60.0)            # Optional: Max retry delay (default: 30.0)
    .build()
)
```

## API reference

### Screenshots API

#### Capture a screenshot (sync)

```python
image_bytes = client.screenshots.capture(
    url="https://example.com",
    device="Desktop HD",           # Device preset: "Desktop HD", "iPhone 14", "iPad", etc.
    full_page=True,                # Capture entire page
    format="png",                  # Output format: "png", "jpeg", "webp", "pdf"
    quality=80,                    # Image quality (1-100, for jpeg/webp)
    delay=1000,                    # Delay before capture in ms
    wait_for=".main-content",      # CSS selector to wait for
    wait_until="networkidle",      # "load", "domcontentloaded", "networkidle"
    timeout=30000,                 # Request timeout in ms
    dark_mode=True,                # Enable dark mode
    custom_css="body { background: red; }",
    hide_selectors=[".ad", ".popup"],
    selector=".main-content",      # Capture specific element
    block_ads=True,                # Block advertisements
    block_cookie_banners=True,     # Block cookie consent banners
    block_level="pro",             # Blocking level: "none", "light", "normal", "pro", "ultimate"
    viewport_width=1920,           # Custom viewport width
    viewport_height=1080,          # Custom viewport height
    device_scale_factor=2,         # Device scale factor (1-3)
)
```

#### Async screenshot capture

```python
# Start an async job
job = client.screenshots.capture_async(
    url="https://example.com",
    device="Desktop HD",
    webhook_url="https://your-server.com/webhook",  # Optional webhook
)
print(f"Job ID: {job.id}")

# Check job status
status = client.screenshots.get_job(job.id)
print(f"Status: {status.status}")

# Download result when complete
if status.status == "COMPLETED":
    image = client.screenshots.get_job_result(job.id)

# List all jobs
jobs = client.screenshots.list_jobs()

# Cancel a job
client.screenshots.cancel_job(job.id)
```

### Bulk API

```python
from allscreenshots_sdk import BulkUrlRequest, BulkUrlOptions, BulkDefaults

# Simple bulk capture
job = client.bulk.create([
    "https://example.com",
    "https://github.com",
])

# With per-URL options
job = client.bulk.create([
    BulkUrlRequest(url="https://example.com"),
    BulkUrlRequest(
        url="https://github.com",
        options=BulkUrlOptions(full_page=True, device="iPhone 14")
    ),
], defaults=BulkDefaults(format="jpeg", quality=80))

# Check status
status = client.bulk.get_status(job.id)
print(f"Progress: {status.progress}%")

# List all bulk jobs
jobs = client.bulk.list_jobs()

# Cancel
client.bulk.cancel(job.id)
```

### Compose API

Combine multiple screenshots into a single image:

```python
from allscreenshots_sdk import CaptureItem, ComposeOutputConfig, VariantConfig

# Multiple URLs
result = client.compose.create([
    CaptureItem(url="https://example.com", label="Example"),
    CaptureItem(url="https://github.com", label="GitHub"),
], output=ComposeOutputConfig(
    layout="GRID",  # "GRID", "HORIZONTAL", "VERTICAL", "MASONRY", "MONDRIAN"
    columns=2,
    spacing=10,
    padding=20,
    background="#ffffff",
))

# Single URL with variants (different devices)
result = client.compose.create(
    url="https://example.com",
    variants=[
        VariantConfig(device="Desktop HD", label="Desktop"),
        VariantConfig(device="iPhone 14", label="Mobile"),
        VariantConfig(device="iPad", label="Tablet"),
    ],
)

print(f"Result URL: {result.url}")

# Preview layout
preview = client.compose.preview_layout(
    layout="GRID",
    image_count=4,
    canvas_width=1920,
)
```

### Schedules API

```python
from allscreenshots_sdk import ScheduleScreenshotOptions

# Create a schedule
schedule = client.schedules.create(
    name="Daily homepage",
    url="https://example.com",
    schedule="0 9 * * *",  # Cron: daily at 9 AM
    timezone="America/New_York",
    options=ScheduleScreenshotOptions(
        device="Desktop HD",
        full_page=True,
    ),
    retention_days=30,
)

# List schedules
result = client.schedules.list()
for s in result.schedules:
    print(f"{s.name}: {s.status}")

# Update
client.schedules.update(schedule.id, name="New name")

# Pause/resume
client.schedules.pause(schedule.id)
client.schedules.resume(schedule.id)

# Manually trigger
client.schedules.trigger(schedule.id)

# Get execution history
history = client.schedules.get_history(schedule.id, limit=10)

# Delete
client.schedules.delete(schedule.id)
```

### Usage API

```python
# Get usage statistics
usage = client.usage.get()
print(f"Tier: {usage.tier}")
print(f"Screenshots this period: {usage.current_period.screenshots_count}")
print(f"Bandwidth: {usage.current_period.bandwidth_formatted}")

# Get quota status
quota = client.usage.get_quota()
print(f"Screenshots: {quota.screenshots.used}/{quota.screenshots.limit}")
print(f"Bandwidth: {quota.bandwidth.used_formatted}/{quota.bandwidth.limit_formatted}")

if quota.screenshots.percent_used > 80:
    print("Warning: Approaching screenshot limit!")
```

## Error handling

The SDK provides typed exceptions for different error scenarios:

```python
from allscreenshots_sdk import (
    AllscreenshotsClient,
    AllscreenshotsError,
    ValidationError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TimeoutError,
)

try:
    client.screenshots.capture("https://example.com")
except ValidationError as e:
    print(f"Invalid request: {e.message}")
    print(f"Error code: {e.error_code}")
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Resource not found")
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after} seconds")
except ServerError as e:
    print(f"Server error ({e.status_code}): {e.message}")
except TimeoutError as e:
    print(f"Request timed out after {e.timeout} seconds")
except AllscreenshotsError as e:
    print(f"SDK error: {e.message}")
```

## License

Apache License 2.0
