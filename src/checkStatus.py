# Part 2 + 3 check status and print a log 
from urllib.parse import urlparse
import requests
import time
class checkStatus:
    def __init__(self):
        self.storage = {}

    def get_domain(self, url):
        return urlparse(url).netloc

    def record(self, url, status):
        domain = self.get_domain(url)
        if domain not in self.storage:
            self.storage[domain] = {'up_times': 0, 'down_times': 0}
        if status == "UP":
            self.storage[domain]['up_times'] += 1
        else:
            self.storage[domain]['down_times'] += 1

    def calculate_avail(self, domain):
        if domain not in self.storage:
            return 0
        up_times = self.storage[domain]['up_times']
        down_times = self.storage[domain]['down_times']
        if up_times+ down_times == 0: #denominator can't be zero
            return 0
        return round((up_times / (up_times+ down_times)) * 100)

    def print_logs(self):
        for domain in self.storage.keys():
            availability = self.calculate_avail(domain)
            print(f"{domain} has {availability}% availability")
 

    # Call the api and see the performance
    def check_endpoint(self, endpoint):
        method_map = {
        'GET': requests.get,
        'POST': requests.post,
        'PUT': requests.put,
        'DELETE': requests.delete
        }
        method = endpoint.method  
        request_func = method_map.get(method)
        try: 
            kwargs = {
                'headers': endpoint.headers
            }

            if endpoint.method in ['POST', 'PUT'] and endpoint.body:
                try:
                    kwargs['json'] = endpoint.body
                except ValueError:
                    kwargs['data'] = endpoint.body

            start_time = time.time()
            response = request_func(endpoint.url, **kwargs)

            # latency < 500ms
            latency = (time.time() - start_time) * 1000
            if 200 <= response.status_code <= 299 and latency < 500:
                return 'UP'
            else:
                return 'DOWN'
        except Exception as e:
            print(f"An unexpected error occurred in check_endpoint: {e}")
            return 'DOWN'  
 