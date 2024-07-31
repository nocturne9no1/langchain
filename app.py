import requests

def check_service_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Service is up and running")
        else:
            print(f"Service is down with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Service is down with error: {e}")

def send_generate_request(url, data):
    try:
        with requests.post(url, json=data) as response:
            if response.status_code == 200:
                print("Request from service:")
                for line in response.iter_lines():
                    if line:
                        try:
                            json_line = line.decode('utf-8')
                            print(json_line)
                        except ValueError as e:
                            print(f"Failed to parse JSON response: {line}")

            else:
                print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send request to the service: {e}")

check_service_status("http://127.0.0.1:11434")

url = "http://127.0.0.1:11434/api/generate"
data = {
    "model": "llama3:8b",
    "prompt": "Why is the sky blue?",
}

send_generate_request(url, data)