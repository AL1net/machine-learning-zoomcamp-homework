import sys
import requests


def main() -> int:
    """Send a sample client payload to the prediction endpoint and print the JSON response.

    Returns 0 on success, 1 on failure.
    """
    url = "http://localhost:8000/predict"
    client = {
        "lead_source": "organic_search",
        "number_of_courses_viewed": 4,
        "annual_income": 80304.0,
    }

    try:
        resp = requests.post(url, json=client, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 1

    try:
        data = resp.json()
    except ValueError:
        print("Response is not valid JSON:")
        print(resp.text)
        return 1

    print("Response JSON:", data)
    return 0


if __name__ == "__main__":
    sys.exit(main())