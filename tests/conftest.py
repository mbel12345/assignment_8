import pytest
import requests
import subprocess
import time

from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def fastapi_server():

    '''
    Start the FastAPI server before any tests
    '''

    # Start FastAPI app
    fastapi_process = subprocess.Popen(['python3', 'main.py'])

    # Define server URL (localhost)
    server_url = 'http://127.0.0.1:8000/'

    # Give the server 30 seconds to come up before failing
    timeout = 30
    start_time = time.time()
    server_up = False
    print('Starting FastAPI server...')
    while time.time() - start_time < timeout:
        try:
            response = requests.get(server_url) # Query the home page (index.html)
            if response.status_code == 200:
                server_up = True
                print('FastAPI server is up and running.')
                break
        except requests.exceptions.ConnectionError:
            pass # Try again after waiting for a second if there is an error
        time.sleep(1)

    if not server_up:
        fastapi_process.terminate()
        raise RuntimeError('FastAPI server failed to start within timeout period.')

    yield # Separate setup from teardown

    # Terminate FastAPI server
    print('Shutting down FastAPI server...')
    fastapi_process.terminate()
    fastapi_process.wait()
    print('FastAPI server has been terminated')

@pytest.fixture(scope='session')
def playwright_instance_fixture():

    # Manage Playwright's lifecycle

    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='session')
def browser(playwright_instance_fixture):

    # Launch a browser instance

    browser = playwright_instance_fixture.chromium.launch(headless=True)
    yield browser # Separate setup from teardown
    browser.close()

@pytest.fixture(scope='function')
def page(browser):

    # Create a new page for each test

    page = browser.new_page()
    yield page # Separate setup from teardown
    page.close()
