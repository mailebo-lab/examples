# Email Processing Automation

This repository contains Python scripts aimed at automating email processing tasks related to order cancellation requests.

## Files

- `detection.py`: Contains a function `detection` that checks for specific keywords in email content to identify cancellation requests.

- `extraction.py`: Includes a function `parsing` to extract relevant order details based on email content and sender information using SQL queries.

- `actions.py`: Implements a function `processing` that processes cancellation requests, sends appropriate responses, and updates the database based on extracted information.


## Requirements

- Python 3.x
- Required Python packages: `typing`, `fuzzywuzzy`
- External dependencies: `processing_modules.get_data`, `ActionTools`


