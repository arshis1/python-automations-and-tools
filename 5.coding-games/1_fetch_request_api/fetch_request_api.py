#################################################################################
#This Application is to parse arguments at run time that will decide 
#whether a request needs to be sent to fetch data from an API
#It also uses logging library to capture the logs of the app with timestamps
#################################################################################


import argparse # For command-line argument parsing 
import logging # For logging 
from datetime import datetime # For timestamping 
import requests # Example external library (requires installation via pip)

CONFIG = { "version": "2.0", "app_name": "Advanced Python App", "log_file": "app.log", }

logging.basicConfig( filename=CONFIG["log_file"], level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s" )

def greet_user(name):
    """ Greet the user by name. """ 
    logging.info(f"Greeting user: {name}") 
    print(f"Hello, {name}! Welcome to {CONFIG['app_name']}.")

def perform_task(task_name):
    """ Perform a specific task based on the task name. """ 
    logging.info(f"Performing task: {task_name}") 
    if task_name == "fetch_data":
        fetch_data()
    else:
        print(f"Task '{task_name}' is not recognized.") 
        logging.warning(f"Unrecognized task: {task_name}")

def fetch_data(): 
    """ Example task: Fetch data from an external API. """ 
    logging.info("Fetching data from an API.") 
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response.raise_for_status()
        data = response.json()
        print(f"Fetched data: {data}")
        logging.info(f"Data fetched successfully: {data}") 
    except requests.RequestException as e: 
        print(f"Error fetching data: {e}") 
        logging.error(f"Error during API call: {e}")

def parse_arguments(): 
    """ Parse command-line arguments. """ 
    parser = argparse.ArgumentParser(description=CONFIG["app_name"])
    parser.add_argument( "--name", type=str, default="User", help="Name of the user." ) 
    parser.add_argument( "--task", type=str, default="fetch_data", help="Task to perform." ) 
    return parser.parse_args()

def main(): 
    """ Main entry point for the application. """ 
    logging.info(f"Starting {CONFIG['app_name']} (v{CONFIG['version']})") 
    print(f"Starting {CONFIG['app_name']} (v{CONFIG['version']})")
    # Parse arguments
    args = parse_arguments()

    # Greet the user
    greet_user(args.name)

    # Perform the requested task
    perform_task(args.task)

    print("Application finished.")
    logging.info("Application finished successfully.")

if __name__ == "__main__": 
    try: 
        main() 
    except KeyboardInterrupt: 
        print("\nApplication interrupted by the user.") 
        logging.warning("Application interrupted by user.") 
        sys.exit(0) 
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
        logging.error(f"Unexpected error: {e}") 
        sys.exit(1)