import time
from utils import read_yaml
from checkStatus import checkStatus   
from endpoints import Endpoint

class Main:
    def __init__(self, config_file, interval):
        self.check_status = checkStatus()
        self.interval = interval
        self.config_file = config_file
 
    # Read yaml file and map it as lists of endpoint instances
    def load_endpoints(self):
        try:
            endpoints = read_yaml(self.config_file)
            if endpoints is None:
                raise Exception("No endpoints found in configuration file.")
            
            return [Endpoint(name=ep.get('name'),
                             url=ep.get('url'),
                             method=ep.get('method'),
                             headers=ep.get('headers'),
                             body=ep.get('body'))
                    for ep in endpoints]
        
        except Exception as e:
            print(f"An unexpected error occurred in load_endpoints: {e}")
            return []
        
    
        
    # Store the information inside the self.check_status to keep security
    def check_endpoints(self, endpoint): 
        status = self.check_status.check_endpoint(endpoint)
        self.check_status.record(endpoint.url, status)

    # Print the result out
    def print_logs(self):
        self.check_status.print_logs()

    def run(self):
        while True:
            endpoints = self.load_endpoints()
            for endpoint in endpoints:
                self.check_endpoints(endpoint)
            self.print_logs()
            time.sleep(self.interval)
    


if __name__ == '__main__':
    app = Main('httpSample.yml', 15)   # <------ change the yaml file name
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nKey stop")
