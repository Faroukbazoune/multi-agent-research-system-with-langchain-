from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import find_dotenv ,load_dotenv
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import tavily_search ,web_scrap
import os
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())
groq_model = ChatGroq(model_name="qwen/qwen3.6-27b")
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.0)

def create_search_agent():

    return create_agent(
        model=gemini_model,
        tools=[tavily_search],
        system_prompt=(
            "you are an expert searcher , with tavily_seacrh tool"
            "tools:tavily_search is a tool that help you search information to answer the user query"
            "your task is to search for information with the help of this tool"
        )
        
    )

def create_scraping_agent():
    return create_agent(
            model=gemini_model,
            tools=[web_scrap],
            system_prompt=(
                "you are an expert web scraper , with web_scrap tool"
                "tools:web_scrap is a tool that help you scrap more content from a url"
                "your task is to scrap the web for more information and content  with the help of this tool"
            )
            
        )


writer_prompt=ChatPromptTemplate.from_messages(
    [
    ("system","""you are an expert research and writer agent, write me a structured thoughtful reports.
    Structured the report as this:
    -Introduction
    -key insights (3 well-explained points)
    -Conclusion
    -List of sources (URLs you used) """),

    ("human", """write me a report about this topic
    topic : {topic}

    research gathered:{research_info}
""")
    ]
)



writer_chain = writer_prompt| gemini_model | StrOutputParser()



critic_prompt = ChatPromptTemplate.from_messages(
    [
    ("system", """you are an expert report Criticker, critic this report.
the critic report should be like this :
-Rating (on 10)
-Weak points:
.....
....
-Strong points
....
....
-One line verdict:
.... """),

    ("""human","citic this report 
    report : {report} """)
    ]
)

citicker_chain = critic_prompt | gemini_model|StrOutputParser()