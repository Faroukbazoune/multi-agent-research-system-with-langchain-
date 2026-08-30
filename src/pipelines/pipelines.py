from src.agents.agents import create_search_agent , create_scraping_agent , writer_chain, citicker_chain

def run_search_pipeline(topic:str) -> dict:

    state = {}
    print("="*50)
    print("Search Agent is working . . . ")
    print("="*50)

    search_agent  = create_search_agent()
    result = search_agent.invoke({
        'messages':[
            ("human",f"find the best reliablel informations about {topic}")
        ]
    })
    state["search_result"] = result['messages'][-1].text

    print(f"\n Search Result: {state['search_result']}")


    print("="*50)
    print("Scraping Agent is working . . . ")
    print("="*52)

    search_agent  = create_scraping_agent()
    result = search_agent.invoke({
        'messages':[
            ("human",f""" based on this topic: {topic}.
            pcik the most reliable URLs and scrape them.
            Search result : {state['search_result']}

            """)
        ]
    })
    state["scrape_result"] = result['messages'][-1].text

    print(f"\n Scrape Result: {state['scrape_result']}")

##Writer chain 

    print("="*50)
    print("writer Agent is working . . . ")
    print("="*50)

    state['report'] = writer_chain.invoke({
        'topic':topic,
        'research_info':f"""Search result:{state["search_result"]}\n\n\n\n
        Scrape result:{state['scrape_result']}"""
    })

    print(f"Final Report :\n{state['report']}")

##CRITICKER agent
    print("="*50)
    print("writer Agent is working . . . ")
    print("="*50)

    state['critic'] = citicker_chain.invoke({
        'report':state['report']
    })
    print(f"Report Critic:\n{state['critic']}")


    return state