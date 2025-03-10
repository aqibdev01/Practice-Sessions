import threading
import requests
from bs4 import BeautifulSoup

urls = ["https://python.langchain.com/docs/introduction/",
        "https://python.langchain.com/docs/tutorials/",
        "https://python.langchain.com/docs/concepts/"]


def fetch_content(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {urls}")

if __name__=="__main__":
    Threads = []

    for url in urls:
        thread = threading.Thread(target=fetch_content,args=(url,))
        Threads.append(thread)
        thread.start()

    for thred in Threads:
        thread.join()

    print("All webpages fetched")