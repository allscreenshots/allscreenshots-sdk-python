import os, sys, time, uuid
from pathlib import Path
from allscreenshots_sdk import ApiClient, Configuration, ScreenshotRequest, ScreenshotJsonResponse
from allscreenshots_sdk.api.screenshot_api import ScreenshotApi
from allscreenshots_sdk.api.job_api import JobApi
from allscreenshots_sdk.api.usage_api import UsageApi
import json
from urllib.parse import urlparse

def main():
    config = Configuration(host=os.getenv('ALLSCREENSHOTS_BASE_URL', 'https://api.allscreenshots.com'), api_key={'ApiKey': os.environ['ALLSCREENSHOTS_API_KEY']})
    with ApiClient(config) as client:
        screenshots, jobs = ScreenshotApi(client), JobApi(client)
        mode = sys.argv[1] if len(sys.argv)>1 else 'quota'
        if mode == 'quota':
            print(UsageApi(client).get_quota().to_json()); return
        request = ScreenshotRequest(url=os.getenv('ALLSCREENSHOTS_URL', 'https://example.com'), response_type='URL', format='png')
        key = os.getenv('ALLSCREENSHOTS_IDEMPOTENCY_KEY', str(uuid.uuid4()))
        if mode == 'sync':
            raw = screenshots.capture_sync(request, idempotency_key=key, _request_timeout=180)
            metadata = ScreenshotJsonResponse.from_json(raw.decode('utf-8'))
            capture_id = urlparse(metadata.result_url).path.split('/')[-2]
            file = screenshots.get_sync_capture_result(capture_id)
        elif mode == 'async':
            job = jobs.create_async_job(request, idempotency_key=key)
            deadline = time.monotonic()+180
            while True:
                status = jobs.get_job_status(job.id)
                if status.status == 'COMPLETED': break
                if status.status in ['FAILED','CANCELLED']: raise RuntimeError(status.error_message or status.status)
                if time.monotonic()>deadline: raise TimeoutError('Capture polling timed out')
                time.sleep(2)
            file = jobs.get_job_result(job.id)
        else: raise ValueError('Expected quota, sync, or async')
        output = Path(os.getenv('ALLSCREENSHOTS_OUTPUT','capture.png'))
        output.write_bytes(file)
        print(json.dumps({'output':str(output)}))
if __name__ == '__main__':
    try: main()
    except Exception:
        print('SDK request failed. Check authentication, quota, and the API response.', file=sys.stderr); sys.exit(1)
