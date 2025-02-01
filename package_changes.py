import zipfile  

# Function to package multiple SQL scripts into a single zip file
def package_changes(scripts, output_file):
    
    # Create a new zip file at the specified output path ('w' means write mode)
    with zipfile.ZipFile(output_file, 'w') as zf:
        
        # Loop through each script file in the 'scripts' list
        for script in scripts:
            
            # Add the script file to the zip file
            zf.write(script)

# Main function that defines script paths and output zip file path
def main():
    # Path to the first SQL script
    script1 = 'schema_changes.sql'

    # Path where the zip file will be created
    output_path = 'deployment_package.zip'
    
    # List containing all scripts to be packaged
    scripts = [script1]
    
    # Call the package_changes function to zip the scripts into the output file
    package_changes(scripts, output_path)
    
    # Print a message to indicate the process is successful
    print("Successfully packaged")

# Call the main function to start the process
main()