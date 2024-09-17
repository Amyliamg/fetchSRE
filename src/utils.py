# Step 1 Parsing the program input
import yaml
from os.path import join, dirname, abspath

def read_yaml(filename):
    dir = dirname(abspath(__file__))
    yaml_path = join(dir, 'data',filename)
    try:
        with open(yaml_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.SafeLoader)
        return data
    except FileNotFoundError:
        print(f"File not found: {yaml_path}")
        return None
    
 
file_name = 'httpSample.yml'  
data = read_yaml(file_name)
if data is not None:
    print(data)