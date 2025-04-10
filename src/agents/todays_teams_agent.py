from crewai import Agent, Task
from src.tools.search_tools import get_search_tool
import os
from langchain_openai import ChatOpenAI


def create_todays_teams_agent():
    """Creates the Today's Match Details Agent"""
    # Get the search function
    search_tool = get_search_tool(
        description="Search for the IPL 2025 matches and details",
        n_results=30
    )

    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("GPT_MODEL", "gpt-3.5-turbo"),
        temperature=0.7,
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    todays_teams = Agent(
        role="Todays Match Details Agent",
        goal="Find IPL teams that are playing on the specified date",
        backstory="You are an expert in finding cricket news across the web.",
        tools=[search_tool],
        llm=llm,
        verbose=True
    )
    
    return todays_teams


def create_todays_teams_task(agent, date, url):
    """Creates the Today's Match Details Task"""
    return Task(
        name="Todays Match Details",
        description=f"""You have to find the teams that are going to play on {date} from the url: {url}.
        If there is Sunday on date then 2 matches on a same day than give the details of both matches.
        If there is no match on date then just say: "There is no match for {date}".""",
        expected_output="""Give the names of the teams, where they are playing and at what time(in PM) the match will start.
        Also give the information about the pitch condition and the past records like numbers of losses and wins of the teams on that ground.
        If there is Sunday on date then 2 matches on a same day than give the details of both matches.
        If there isn't any match on date then say: "There is no match for [date]".""",
        agent=agent
    )