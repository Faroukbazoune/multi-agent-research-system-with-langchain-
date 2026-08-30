from langchain.tools import tool
from dotenv import load_dotenv , find_dotenv
from rich import print
import os 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from readability import Document
import trafilatura
import re

load_dotenv(find_dotenv())

taviliy_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))


def tavily_search(query: str) -> str:
    """this tool uses tavily to search for information on the web"""
    try:
        response = taviliy_client.search(query=query, max_results=5)
    except Exception as e:
        return f"An error occurred while searching: {e}"

    else:
        result = [f"title: {item['title']}\nURL: {item['url']}\nSnippet: {item['content'][:300]}" for item in response["results"]]
        return "\n-----------\n".join(result)




@tool
def web_scrap(url:str)->str:
    """
    this function help scrap content from a web page
    INPUTS: URL
      """
    headers = {
        "User-Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)" 
                      "Chrome/120.0.0.0 Safari/537.36"),
        "Accept-Language":"en-US,en;q=0.9",
        "Referer":"https://www.google.com/"
    }

    try:
        response = requests.get(
            url = url,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        html = response.text


        extracted = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=False
        )
        if extracted and len(extracted.strip()) > 200:
            cleaned = re.sub(r"\s+", " ", extracted)
            return cleaned[:5000]
        else:
            doc = Document(html)
            soup = BeautifulSoup(doc.summary(), "html.parser").get_text(separator=" ",strip=True)

            if soup and len(soup)>200:
                cleaned = re.sub(r"\s+", " ", soup)
                return cleaned[:5000]

        return f"ERROR : Could NOT extract content from this url"


    except requests.exceptions.Timeout as e:
        return f"Request timed out :{e}"
    except requests.exceptions.HTTPError as e:
        return f"HTTP error has occured  :{e}"
    except Exception as e:
        return f"Error:{e}"
