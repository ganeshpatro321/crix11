from crewai import Agent, Task
import os
from langchain_openai import ChatOpenAI


def create_user_team_selector_agent():
    """Creates the User Team Selector Agent"""
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("GPT_MODEL", "gpt-3.5-turbo"),
        temperature=0.7,
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    user_team_selector = Agent(
        role="User Team Selector",
        goal="Ask the user about the teams for which they want to make a Dream11 team.",
        backstory="A helpful assistant that asks users about the team names for which they want to make a team",
        llm=llm,
        verbose=True,
    )
    
    return user_team_selector


def create_user_team_selector_task(agent, todays_teams_task):
    """Creates the User Team Selector Task"""
    return Task(
        name='Team Selector for Dream11',
        description="Ask the user about the teams they want to choose for making a Dream11 team",
        expected_output="Returns the name of teams in this specific format: team_1 vs team_2",
        human_input=True,
        agent=agent,
        context=[todays_teams_task]
    )