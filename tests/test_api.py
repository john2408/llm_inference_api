import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to the API.")
    parser.add_argument("prompt", type=str, help="The prompt to send to the API")
    args = parser.parse_args()

    response = requests.post(
        "http://localhost:8000/generate",
        json={
            "prompt": args.prompt,
            "config": {
                "model": "llama3.2:latest",#"deepseek-r1:14b",
                "max_tokens": 1000,
                "temperature": 0.8
            }
        }
    )
    
    response_data = response.json()
    parsed_response = response_data['response'].split('</think>\n\n')[-1]
    print(parsed_response)

if __name__ == "__main__":
    main()