import os
import datetime
import warnings
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.todays_teams_agent import create_todays_teams_agent, create_todays_teams_task
from src.agents.user_team_selector_agent import create_user_team_selector_agent, create_user_team_selector_task
from src.agents.players_agent import create_players_agent, create_players_task
from src.agents.team_selector_agent import create_team_selector_agent, create_team_selector_task

# Suppress warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

def main():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Get environment variables
    match_url = os.getenv("MATCH_URL")
    player_stats_url = os.getenv("PLAYER_STATS_URL")
    
    # Check if API keys are set
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("SERPER_API_KEY"):
        print("Error: API keys are not set. Please check your .env file.")
        return
    
    print(f"🏏 Starting Dream11 AI Agent for IPL 2025 - {current_date}, {match_url}, {player_stats_url}")
    
    # Create agents
    todays_teams_agent = create_todays_teams_agent()
    user_team_selector_agent = create_user_team_selector_agent()
    players_agent = create_players_agent()
    team_selector_agent = create_team_selector_agent()
    
    # Create tasks
    todays_teams_task = create_todays_teams_task(todays_teams_agent, current_date, match_url)
    user_team_selector_task = create_user_team_selector_task(user_team_selector_agent, todays_teams_task)
    players_task = create_players_task(players_agent, user_team_selector_task, player_stats_url)
    select_players_task = create_team_selector_task(team_selector_agent, players_task)
    
    # Create crew
    team_crew = Crew(
        agents=[todays_teams_agent, user_team_selector_agent, players_agent, team_selector_agent],
        tasks=[todays_teams_task, user_team_selector_task, players_task, select_players_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Run the crew
    result = team_crew.kickoff()
    
    # Display results
    print("\n\n🏆 Dream11 AI Agent Results:")
    print(result)
    
    return result

if __name__ == "__main__":
    main()