import json
import time
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

TIMEOUT = 5  # seconds

def load_apis(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(Fore.RED + "Failed to load API list.")
        return []

def check_api(api):
    url = api["url"]
    name = api["name"]

    try:
        start_time = time.time()
        response = requests.get(url, timeout=TIMEOUT)
        response_time = int((time.time() - start_time) * 1000)

        if 200 <= response.status_code < 300:
            return ("UP", name, response.status_code, response_time)
        else:
            return ("DOWN", name, response.status_code, response_time)

    except requests.exceptions.Timeout:
        return ("DOWN", name, "Timeout", "-")
    except requests.exceptions.RequestException:
        return ("DOWN", name, "Network Error", "-")

def print_report(results):
    print("\nAPI Health Status Report\n" + "-" * 40)

    for status, name, code, time_ms in results:
        if status == "UP":
            print(
                Fore.GREEN
                + f"[UP]   {name:<20} {code}   {time_ms}ms"
            )
        else:
            print(
                Fore.RED
                + f"[DOWN] {name:<20} {code}"
            )

    print("\nHealth check completed.\n")

def main():
    apis = load_apis("apis.json")

    if not apis:
        print(Fore.RED + "No APIs found to check.")
        return

    results = []

    for api in apis:
        result = check_api(api)
        results.append(result)

    print_report(results)

if __name__ == "__main__":
    main()
