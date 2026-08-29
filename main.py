from src.tools.tools import tavily_search ,web_scrap

output = web_scrap.invoke("https://www.britannica.com/place/France")
print(output)