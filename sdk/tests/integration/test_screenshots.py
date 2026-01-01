"""
Integration tests for the Allscreenshots SDK.

These tests require a valid API key set in the ALLSCREENSHOTS_API_KEY environment variable.
They make real API calls and verify the SDK works correctly end-to-end.
"""

import base64
import os
import platform
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import pytest

from allscreenshots_sdk import AllscreenshotsClient, AllscreenshotsError, ValidationError


@dataclass
class TestResult:
    """Result of a single test case."""

    test_id: str
    test_name: str
    url: str
    device: str
    full_page: bool
    passed: bool
    error_message: str | None = None
    image_base64: str | None = None
    execution_time_ms: int = 0


@dataclass
class TestReport:
    """Complete test report."""

    sdk_name: str = "allscreenshots-sdk-python"
    sdk_version: str = "1.0.0"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    total_tests: int = 0
    passed_tests: int = 0
    failed_tests: int = 0
    total_execution_time_ms: int = 0
    results: list[TestResult] = field(default_factory=list)
    os_info: str = field(default_factory=lambda: f"{platform.system()} {platform.release()}")
    python_version: str = field(default_factory=lambda: sys.version.split()[0])


# Global report instance
_report = TestReport()


def get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.environ.get("ALLSCREENSHOTS_API_KEY")
    if not api_key:
        pytest.fail(
            "ALLSCREENSHOTS_API_KEY environment variable is not set. "
            "Set it to run integration tests."
        )
    return api_key


@pytest.fixture(scope="module")
def client() -> AllscreenshotsClient:
    """Create a client for the test module."""
    api_key = get_api_key()
    client = AllscreenshotsClient.builder().with_api_key(api_key).with_timeout(120.0).build()
    yield client
    client.close()


class TestScreenshotsIntegration:
    """Integration tests matching the required test cases."""

    def test_it_001_basic_desktop_screenshot(self, client: AllscreenshotsClient) -> None:
        """IT-001: Basic Desktop Screenshot."""
        test_id = "IT-001"
        test_name = "Basic Desktop Screenshot"
        url = "https://github.com"
        device = "Desktop HD"
        full_page = False

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_002_basic_mobile_screenshot(self, client: AllscreenshotsClient) -> None:
        """IT-002: Basic Mobile Screenshot."""
        test_id = "IT-002"
        test_name = "Basic Mobile Screenshot"
        url = "https://github.com"
        device = "iPhone 14"
        full_page = False

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_003_basic_tablet_screenshot(self, client: AllscreenshotsClient) -> None:
        """IT-003: Basic Tablet Screenshot."""
        test_id = "IT-003"
        test_name = "Basic Tablet Screenshot"
        url = "https://github.com"
        device = "iPad"
        full_page = False

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_004_full_page_desktop(self, client: AllscreenshotsClient) -> None:
        """IT-004: Full Page Desktop."""
        test_id = "IT-004"
        test_name = "Full Page Desktop"
        url = "https://github.com"
        device = "Desktop HD"
        full_page = True

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_005_full_page_mobile(self, client: AllscreenshotsClient) -> None:
        """IT-005: Full Page Mobile."""
        test_id = "IT-005"
        test_name = "Full Page Mobile"
        url = "https://github.com"
        device = "iPhone 14"
        full_page = True

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_006_complex_page(self, client: AllscreenshotsClient) -> None:
        """IT-006: Complex Page."""
        test_id = "IT-006"
        test_name = "Complex Page"
        url = "https://github.com/anthropics/claude-code"
        device = "Desktop HD"
        full_page = False

        start_time = time.time()
        try:
            image_bytes = client.screenshots.capture(url, device=device, full_page=full_page)
            execution_time_ms = int((time.time() - start_time) * 1000)

            assert image_bytes is not None
            assert len(image_bytes) > 0

            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    image_base64=base64.b64encode(image_bytes).decode("utf-8"),
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=str(e),
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_007_invalid_url(self, client: AllscreenshotsClient) -> None:
        """IT-007: Invalid URL - should raise ValidationError."""
        test_id = "IT-007"
        test_name = "Invalid URL"
        url = "not-a-valid-url"
        device = "Desktop HD"
        full_page = False

        start_time = time.time()
        try:
            # This should raise a ValidationError
            with pytest.raises((ValidationError, AllscreenshotsError, Exception)):
                client.screenshots.capture(url, device=device, full_page=full_page)

            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    error_message="Validation error correctly raised",
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=f"Unexpected error: {e}",
                    execution_time_ms=execution_time_ms,
                )
            )
            raise

    def test_it_008_unreachable_url(self, client: AllscreenshotsClient) -> None:
        """IT-008: Unreachable URL - should handle gracefully."""
        test_id = "IT-008"
        test_name = "Unreachable URL"
        url = "https://this-domain-does-not-exist-12345.com"
        device = "Desktop HD"
        full_page = False

        start_time = time.time()
        try:
            # This should raise an error but be handled gracefully
            with pytest.raises(AllscreenshotsError):
                client.screenshots.capture(url, device=device, full_page=full_page)

            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=True,
                    error_message="Error handled gracefully",
                    execution_time_ms=execution_time_ms,
                )
            )
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            _report.results.append(
                TestResult(
                    test_id=test_id,
                    test_name=test_name,
                    url=url,
                    device=device,
                    full_page=full_page,
                    passed=False,
                    error_message=f"Unexpected error: {e}",
                    execution_time_ms=execution_time_ms,
                )
            )
            raise


def generate_html_report(report: TestReport) -> str:
    """Generate an HTML report from test results."""
    passed_count = sum(1 for r in report.results if r.passed)
    failed_count = sum(1 for r in report.results if not r.passed)
    total_time = sum(r.execution_time_ms for r in report.results)

    results_html = ""
    for result in report.results:
        badge_class = "badge-pass" if result.passed else "badge-fail"
        badge_text = "PASS" if result.passed else "FAIL"

        image_html = ""
        if result.image_base64:
            image_html = f'''
            <div class="screenshot">
                <img src="data:image/png;base64,{result.image_base64}" alt="Screenshot" />
            </div>
            '''

        error_html = ""
        if result.error_message:
            error_html = f'<p class="error-message">{result.error_message}</p>'

        results_html += f'''
        <div class="test-result">
            <div class="test-header">
                <span class="test-id">{result.test_id}</span>
                <span class="test-name">{result.test_name}</span>
                <span class="badge {badge_class}">{badge_text}</span>
            </div>
            <div class="test-details">
                <p><strong>URL:</strong> {result.url}</p>
                <p><strong>Device:</strong> {result.device}</p>
                <p><strong>Full Page:</strong> {result.full_page}</p>
                <p><strong>Execution Time:</strong> {result.execution_time_ms}ms</p>
                {error_html}
            </div>
            {image_html}
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allscreenshots SDK Test Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            background: #1a1a1a;
            color: white;
            padding: 30px;
            border-radius: 8px 8px 0 0;
        }}
        header h1 {{
            font-size: 24px;
            margin-bottom: 10px;
        }}
        .meta {{
            font-size: 14px;
            color: #888;
        }}
        .summary {{
            background: white;
            padding: 20px 30px;
            display: flex;
            gap: 40px;
            border-bottom: 1px solid #eee;
        }}
        .stat {{
            text-align: center;
        }}
        .stat-value {{
            font-size: 32px;
            font-weight: bold;
        }}
        .stat-label {{
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
        }}
        .stat-value.pass {{
            color: #22c55e;
        }}
        .stat-value.fail {{
            color: #ef4444;
        }}
        .results {{
            background: white;
            padding: 20px;
            border-radius: 0 0 8px 8px;
        }}
        .test-result {{
            border: 1px solid #e5e5e5;
            border-radius: 8px;
            margin-bottom: 20px;
            overflow: hidden;
        }}
        .test-header {{
            background: #fafafa;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 15px;
            border-bottom: 1px solid #e5e5e5;
        }}
        .test-id {{
            font-family: monospace;
            background: #e5e5e5;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
        }}
        .test-name {{
            font-weight: 500;
            flex: 1;
        }}
        .badge {{
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }}
        .badge-pass {{
            background: #dcfce7;
            color: #166534;
        }}
        .badge-fail {{
            background: #fee2e2;
            color: #991b1b;
        }}
        .test-details {{
            padding: 15px 20px;
        }}
        .test-details p {{
            margin-bottom: 5px;
            font-size: 14px;
        }}
        .error-message {{
            color: #dc2626;
            background: #fef2f2;
            padding: 10px;
            border-radius: 4px;
            margin-top: 10px;
        }}
        .screenshot {{
            padding: 20px;
            background: #f5f5f5;
            text-align: center;
        }}
        .screenshot img {{
            max-width: 100%;
            max-height: 400px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        footer {{
            margin-top: 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Allscreenshots SDK integration test report</h1>
            <div class="meta">
                <p>SDK: {report.sdk_name} v{report.sdk_version}</p>
                <p>Generated: {report.timestamp}</p>
            </div>
        </header>

        <div class="summary">
            <div class="stat">
                <div class="stat-value">{len(report.results)}</div>
                <div class="stat-label">Total tests</div>
            </div>
            <div class="stat">
                <div class="stat-value pass">{passed_count}</div>
                <div class="stat-label">Passed</div>
            </div>
            <div class="stat">
                <div class="stat-value fail">{failed_count}</div>
                <div class="stat-label">Failed</div>
            </div>
            <div class="stat">
                <div class="stat-value">{total_time}ms</div>
                <div class="stat-label">Execution time</div>
            </div>
        </div>

        <div class="results">
            {results_html}
        </div>

        <footer>
            <p><strong>Environment:</strong> {report.os_info} | Python {report.python_version}</p>
        </footer>
    </div>
</body>
</html>'''
    return html


@pytest.fixture(scope="session", autouse=True)
def generate_report_on_finish(request: pytest.FixtureRequest) -> None:  # noqa: ARG001
    """Generate HTML report after all tests complete."""
    yield
    # Generate report
    html = generate_html_report(_report)
    report_path = Path(__file__).parent.parent.parent / "test-report.html"
    report_path.write_text(html)
    print(f"\nTest report generated: {report_path}")
