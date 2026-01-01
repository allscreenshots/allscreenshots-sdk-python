"""
Allscreenshots Demo Application.

A simple Flask web application demonstrating the Allscreenshots SDK.
"""

import base64
import os

from flask import Flask, jsonify, render_template, request

from allscreenshots_sdk import AllscreenshotsClient, AllscreenshotsError

app = Flask(__name__)

# Device presets
DEVICES = [
    {"value": "Desktop HD", "label": "Desktop HD"},
    {"value": "iPhone 14", "label": "iPhone 14"},
    {"value": "iPad", "label": "iPad"},
]


def get_client() -> AllscreenshotsClient:
    """Create an Allscreenshots client."""
    api_key = os.environ.get("ALLSCREENSHOTS_API_KEY")
    if not api_key:
        raise ValueError("ALLSCREENSHOTS_API_KEY environment variable is not set")
    return AllscreenshotsClient.builder().with_api_key(api_key).with_timeout(120.0).build()


@app.route("/")
def index() -> str:
    """Render the main page."""
    return render_template("index.html", devices=DEVICES)


@app.route("/api/screenshot", methods=["POST"])
def capture_screenshot() -> tuple[dict, int]:
    """Capture a screenshot and return it as base64."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    url = data.get("url", "").strip()
    device = data.get("device", "Desktop HD")
    full_page = data.get("fullPage", False)

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Basic URL validation
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        client = get_client()
        try:
            image_bytes = client.screenshots.capture(
                url=url,
                device=device,
                full_page=full_page,
            )

            # Convert to base64 for embedding in HTML
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            return jsonify({
                "success": True,
                "image": f"data:image/png;base64,{image_base64}",
                "size": len(image_bytes),
            })
        finally:
            client.close()

    except ValueError as e:
        return jsonify({"error": str(e)}), 500
    except AllscreenshotsError as e:
        return jsonify({"error": e.message}), 400
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


@app.route("/health")
def health() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
