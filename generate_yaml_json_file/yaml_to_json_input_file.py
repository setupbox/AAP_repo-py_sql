import yaml
import json

# Function to convert YAML to JSON
def yaml_to_json(yaml_file):
    try:
        # Open YAML file and load YAML content
        with open(yaml_file, 'r') as f:
            yaml_data = yaml.safe_load(f)
        
        # Convert YAML to JSON
        json_data = json.dumps(yaml_data, indent=2)
        
        return json_data
    except Exception as e:
        print(f"Error converting YAML to JSON: {e}")

# Example usage:
if __name__ == "__main__":
    # Assuming YAML file is named 'input.yaml'
    yaml_file = 'output.yaml'
    
    # Convert YAML to JSON
    json_data = yaml_to_json(yaml_file)
    
    if json_data:
        # Print or save the JSON data
        print(json_data)
        
        # Optionally, save JSON data to a file
        with open('output.json', 'w') as json_file:
            json_file.write(json_data)
            print("Converted YAML to JSON and saved to output.json")