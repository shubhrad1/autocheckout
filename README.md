# AutoCheckout

AutoCheckout is a Python automation tool designed to streamline the process of logging in and purchasing items from e-commerce websites like Amazon and Flipkart. It leverages Playwright for browser automation, with stealth and AI-powered element extraction to bypass bot detection and interact with dynamic web pages.

## Features

-   Automated login and checkout for supported e-commerce sites
-   Stealth mode to avoid bot detection
-   AI-based element extraction for robust button and form detection using MISTRAL-MEDIUM-2505 API

## Requirements

-   Python 3.8+
-   [Playwright](https://playwright.dev/python/)
-   [playwright-stealth](https://github.com/AtuboDad/playwright-stealth)
-   Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd autocheckout
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Usage

1. Set your environment variables for credentials:
    ```bash
    export EMAIL=your_email@example.com
    export PASSWORD=your_password
    export MISTRAL_API_KEY=MISTRAL_LLM_api_key
    export MISTRAL_API_ENDPOINT=MISTRAL_API_endpoint
    ```
2. Run the main script:
    ```bash
    python main.py
    ```
    Or use the provided `run.sh` script.

## Project Structure

-   `main.py` - Entry point for the automation
-   `authenticator.py` - Handles login automation
-   `buynow.py` - Handles the buy now process
-   `element_extractor.py` - Extracts actionable elements from pages
-   `ai.py` - AI service for element selection

## Test Results

-   Amazon.in - 23s
-   Flipkart.com - 18s
