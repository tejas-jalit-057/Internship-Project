import json
import time
import argparse
import requests
from colorama import Fore, Style, init

init(autoreset=True)

FAST_LIMIT = 500      # ms
SLOW_LIMIT = 1500     # ms


def load_apis(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        print(Fore.RED + "Error: Unable to read API file.")
        return []


def check_api(api, timeout):
    name = api["name"]
    url = api["url"]

    try:
        start = time.time()
        response = requests.get(url, timeout=timeout)
        latency = int((time.time() - start) * 1000)

        if 200 <= response.status_code < 300:
            if latency <= FAST_LIMIT:
                return ("FAST", name, response.status_code, latency)
            elif latency <= SLOW_LIMIT:
                return ("SLOW", name, response.status_code, latency)
            else:
                return ("CRITICAL", name, response.status_code, latency)

        return ("DOWN", name, response.status_code, latency)

    except requests.exceptions.Timeout:
        return ("DOWN", name, "TIMEOUT", "-")
    except requests.exceptions.RequestException:
        return ("DOWN", name, "NETWORK ERROR", "-")


def print_report(results):
    print("\nAPI Health Report")
    print("-" * 50)

    up = slow = down = 0

    for status, name, code, latency in results:
        if status == "FAST":
            up += 1
            print(Fore.GREEN + f"[FAST]     {name:<20} {code}   {latency}ms")

        elif status == "SLOW":
            slow += 1
            print(Fore.YELLOW + f"[SLOW]     {name:<20} {code}   {latency}ms")

        elif status == "CRITICAL":
            slow += 1
            print(Fore.MAGENTA + f"[CRITICAL] {name:<20} {code}   {latency}ms")

        else:
            down += 1
            print(Fore.RED + f"[DOWN]     {name:<20} {code}")

    print("\nSummary")
    print("-" * 50)
    print(f"Total APIs : {len(results)}")
    print(Fore.GREEN + f"Healthy   : {up}")
    print(Fore.YELLOW + f"Slow      : {slow}")
    print(Fore.RED + f"Down      : {down}")
    print("\nHealth check completed.\n")


def main():
    parser = argparse.ArgumentParser(description="API Health Checker CLI Tool")
    parser.add_argument("--file", default="apis.json", help="API list JSON file")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout (seconds)")
    args = parser.parse_args()

    apis = load_apis(args.file)
    if not apis:
        return

    results = []
    for api in apis:
        results.append(check_api(api, args.timeout))

    print_report(results)


if __name__ == "__main__":
    main()