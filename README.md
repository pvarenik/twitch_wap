# WAP Testing with Selenium
This repository contains automated tests for the Twitch Web Application (WAP) using Selenium and the Page Object pattern.

## Prerequisites

- Python 3.x
- Selenium
- Google Chrome Driver

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages by running:
```pip install -r requirements.txt```

## Running the WAP Test

1. Navigate to the WAP test directory.
2. Run the test using the following command:
```pytest test_wap.py```

## Expected Result

The test should open the Twitch website in mobile emulation mode, perform a search for "StarCraft II", scroll down twice, select a streamer, wait for the stream to load, and take a screenshot of the streamer's page.

## Test Results

The test results will be displayed in the terminal after running the tests. If all tests pass, you will see a success message. If any test fails, you will see an error message with details about the failure.

## Notes

- The tests are designed to be run in a headless browser for CI/CD integration. If you want to see the browser while running the tests, you can modify the `headless` option in the `webdriver.Chrome()` method.
- The screenshot will be saved as `streamer_page_mobile.png` in the same directory as the test script.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
