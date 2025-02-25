import requests
import time

def send_request(cookies):
    url = "https://thunderclap.com/submit-contact"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": cookies,
        "origin": "https://thunderclap.com",
        "referer": "https://thunderclap.com/free-youtube-likes",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = {
        "servicePackageId": "749",
        "ReurnPage": "false",
        "usernameOrProfileUrl": "https://www.youtube.com/watch?v=XiCCuUngySs&ab_channel=KEWIRAUSAHAANSMAN64JAKARTA",
        "email": "cytrunrs@gmail.com"
    }
    try:
        response = requests.post(url, headers=headers, data=payload)
        print(f"Response Status: {response.status_code}")
        print(f"Response Text: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    user_cookies = input("Enter your cookies: ")
    while True:
        send_request(user_cookies)
        print("Waiting for 5 hours before the next request...")
        time.sleep(5 * 60 * 60)  # Tunggu 5 jam sebelum mengulang
