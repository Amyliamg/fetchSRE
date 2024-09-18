# fetchSRE

This project creates a system to regularly check the status of given URLs.


## Basic Logic
The code is divided into three parts:

1) Reading information from the given YAML file and storing it as instances of endpoints
2) Checking the health of the given URLs and recording the results in the checkStatus package
3) Calculating the total number of UP and DOWN endpoints after all the API calls in one term and then printing them out in the format required in the PDF

## How to run
1. Clone the project from the repository to your local device by copying the link below:
`https://github.com/Amyliamg/fetchSRE.git`
2. Install all the required dependencies
`pip install -r requirements.txt`
3. Navigate to the main class folder
`cd src`
4. Run the main method
`python main.py`

> **Note:** The code will continue to run. To stop it, manually interrupt the process with Ctrl + C.

## How to run other yml files?
If you want to use different YAML files:

1. Place the YAML file in the src/data folder and ensure it ends with ".yml".
2. The YAML file should follow the YAML format rules. Incorrect formatting may cause failures in reading the file.
