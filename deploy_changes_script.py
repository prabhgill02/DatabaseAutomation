# Import zipfile to handle zip files and pymysql to interact with MySQL database
import zipfile
import pymysql  

# Path to the zip file containing SQL scripts
package_file = 'deployment_package.zip'

# Establish the database connection using pymysql
connection = pymysql.connect(
    host='localhost',  
    user='root',
    password='yourpassword',  
    database='changes_database'
)

# Open the zip file and process each SQL script inside
with zipfile.ZipFile(package_file, 'r') as zf:
    
    # Loop through each file in the zip
    for script in zf.namelist():
        # Open the SQL script inside the zip
        with zf.open(script) as file:
            # Read and decode the SQL script to a string
            sql_script = file.read().decode('utf-8')
            
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            
            # Split the SQL script by semicolon to separate statements
            statements = sql_script.split(';')
            
            # Execute each SQL statement
            for statement in statements:
                if statement.strip():  # Only execute non-empty statements
                    cursor.execute(statement)  # Execute the SQL statement
                    connection.commit()  # Commit the changes after each statement

# Commit any remaining changes and close the connection

connection.commit()  
cursor.close()  
connection.close()  

# Print a message to indicate successful execution
print("Successfully deployed the SQL scripts from the package.")
