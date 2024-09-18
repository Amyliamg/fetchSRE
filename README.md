# fetchSRE
This project creates a system to regularly check the status of given URLs

## Basic Logic
The code is divided into three parts:

1. Read Information: Parsing the provided YAML file and creating endpoint instances.
2. Health Checks: Monitoring the health of the URLs and recording the results in the checkStatus package.
3. Result Calculation: Aggregating the number of UP and DOWN endpoints after all API calls within a term, then printing them in the format specified in the PDF.

The code is organized into different classes, following Agile methodologies. This approach allows for isolated fixes in different segments if issues arise in any of the three components.
> **Others:** add error handlers and unit tests for debugging and checking the health of the project.

## How to run

### Step1. Check Python Installation
If Python is not yet installed, follow these steps:
1. **Download Python:**
   - Visit [Python official website](https://www.python.org/downloads) and download the appropriate version for your operating system
2. **Verify Installation:**
   - Open terminal or command prompt and run the following command to check the Python version:
     `python --version`
   - If a version number is returned, then Python is successfully installed on your device!

### Step2. Clone the Project and Install All Dependencies
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
To use different YAML files:

1. Place the YAML file in the src/data folder and ensure it ends with ".yml".
2. The YAML file should follow the YAML format rules. Incorrect formatting may cause failures in reading the file.
3. Change Line 52 in main.py file with `app = Main('Your YamlFileName.yml', 15)`  Then it will be running!

## Assumptions:
This code makes the following assumptions to complete the tasks:
1. Since the method is optional, if the user does not specify a method, the default method is GET.
2. Since this code is a demo, asynchronous scenarios are not considered.
3. Users will place their input files in the src/data directory.


