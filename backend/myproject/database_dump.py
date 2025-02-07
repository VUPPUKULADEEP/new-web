# import sqldumper
# from sqldumper import MySQLDumper 

# # Set the necessary parameters for your MySQL connection
# def generate_sql_dump(db_name, user, password, host='localhost', output_file='data.sql'):
#     dumper = MySQLDumper(
#         db_name=db_name,
#         user=user,
#         password=password,
#         host=host
#     )
    
#     # Generate SQL dump file
#     dumper.dump(output_file)
#     print(f"SQL dump generated at {output_file}")

# # Call the function to generate the dump
# generate_sql_dump('test', 'kuladeep', 'vsrk')
import subprocess

db_name = 'test' 
user = 'kuladeep'
password = 'vsrk'
host = 'localhost'
output_file = 'data.sql'

# Properly format the MySQL command
command = f"mysql -h {host} -u {user} -p{password} {db_name} < {output_file}"

try:
    # Execute the command
    subprocess.run(command, shell=True, check=True)
    print("Database import successful.")
except subprocess.CalledProcessError as e:
    print(f"Error during database import: {e}")
