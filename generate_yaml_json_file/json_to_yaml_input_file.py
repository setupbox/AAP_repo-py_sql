import json
import yaml

# Function to convert JSON to YAML and write to file
def json_to_yaml_and_write(json_data, output_file):
    try:
        # Parse the JSON data
        parsed_json = json.loads(json_data)
        
        # Convert JSON to YAML
        yaml_data = yaml.dump(parsed_json, default_flow_style=False)
        
        # Write YAML data to file
        with open(output_file, 'w') as yaml_file:
            yaml_file.write(yaml_data)
        
        print(f"Converted JSON to YAML and saved to {output_file}")
    except Exception as e:
        print(f"Error converting JSON to YAML: {e}")

# Example usage:
if __name__ == "__main__":
    # Assuming JSON data is in a file named 'input.json'
    with open('sample_data.json', 'r') as json_file:
        json_data = json_file.read()
    
    # Define output file path
    output_file = 'output.yaml'
    
    json_to_yaml_and_write(json_data, output_file)