from langchain.tools import tool
from dotenv import load_dotenv , find_dotenv
from rich import print
import os 
import requests
from tavily import TavilyClient

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