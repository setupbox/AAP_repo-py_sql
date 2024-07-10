import json
import yaml

# Function to convert JSON to YAML
def json_to_yaml(json_data):
    try:
        # Parse the JSON data
        parsed_json = json.loads(json_data)
        
        # Convert JSON to YAML
        yaml_data = yaml.dump(parsed_json, default_flow_style=False)
        
        return yaml_data
    except Exception as e:
        print(f"Error converting JSON to YAML: {e}")

# Main Starts here.
if __name__ == "__main__":
    # Assuming JSON data is in a file named 'input.json'
    with open('sample_data.json', 'r') as json_file:
        json_data = json_file.read()
    
    yaml_data = json_to_yaml(json_data)
    
    # Print or save the YAML data
    print(yaml_data)
    with open('manifest.yml', 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False)

