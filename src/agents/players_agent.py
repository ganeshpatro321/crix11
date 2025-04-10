from crewai import Agent, Task
from src.tools.search_tools import get_search_tool
import os
from langchain_openai import ChatOpenAI


def create_players_agent():
    """Creates the Player Analyst Agent"""
    # Get the search function
    search_tool = get_search_tool(
        description="Search for IPL 2025 player stats and playing 11",
        n_results=30
    )

    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("GPT_MODEL", "gpt-3.5-turbo"),
        temperature=0.7,
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    players = Agent(
        role="Player Analyst",
        goal="Provide names of players playing in the teams selected by the user in IPL 2025.",
        backstory="Expert in searching the web and providing current team players with stats.",
        llm=llm,
        tools=[search_tool],
        verbose=True
    )
    
    return players


def create_players_task(agent, user_team_selector_task, player_stats_url):
    """Creates the Players Analysis Task"""
    return Task(
        name="Player Selector",
        description=f"Search this website {player_stats_url} to get the current IPL players for the teams selected by user_team_selector agent and give the names of the players that are playing in 2025 for the teams selected by user.",
        expected_output="""Names of the players (playing 11 players for that match) selected by each team with their IPL stats starting from their IPL carrier up to IPL 2024 record and their recent stats within last 1 year:
        name of team 1:
            For Batsmen: Stats like:
            Matches, Runs, Average, Strike-Rate, 50's, 100's, HighScore and Career Highlights.
            For Bowlers: Stats like:
            Matches, Wickets, Economy, Average, Best Bowling and Career Highlights
            For All Rounders: Stats Like:
            Batting Stats: Matches, Runs, Average, Strike-Rate, 50's, 100's, HighScore and Career Highlights.
            Bowling Stats: Matches, Wickets, Economy, Average, Best Bowling and Career Highlights
        name of team 2:
            For Batsmen: Stats like:
            Matches, Runs, Average, Strike-Rate, 50's, 100's, HighScore and Career Highlights.
            For Bowlers: Stats like:
            Matches, Wickets, Economy, Average, Best Bowling and Career Highlights
            For All Rounders: Stats Like:
            Batting Stats: Matches, Runs, Average, Strike-Rate, 50's, 100's, HighScore and Career Highlights.
            Bowling Stats: Matches, Wickets, Economy, Average, Best Bowling and Career Highlights
        """,
        agent=agent,
        context=[user_team_selector_task]
    )