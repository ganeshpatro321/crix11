from crewai import Agent, Task
import os
from langchain_openai import ChatOpenAI


def create_team_selector_agent():
    """Creates the Dream11 Team Selector Agent"""
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("GPT_MODEL", "gpt-3.5-turbo"),
        temperature=0.7,
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    team_selector = Agent(
        role="Dream11 Team Selector",
        goal="Create the optimal Dream11 team based on match conditions, player stats, and team composition rules",
        backstory="You are a Dream11 expert who knows how to balance team selection, captaincy choices, and credit allocation to maximize points potential.",
        llm=llm,
        verbose=True
    )
    
    return team_selector


def create_team_selector_task(agent, players_task):
    """Creates the Team Selector Task"""
    return Task(
        name="Select Dream11 Players",
        description="""Select the best 11 players for a Dream11 team based on the match analysis and player statistics. Make sure you don't exceed team with more than 100 points. So choose the players accordingly:
        Follow Dream11 rules:
        - Total of 11 players (including Captain and Vice-Captain)
        - 1-4 Wicket-keepers
        - 3-6 Batsmen
        - 1-4 All-rounders
        - 3-6 Bowlers
        - Maximum 7 players from any one team
        
    Select the players so that they can help in maximizing the T20 Fantasy Cricket Points System

    Batting Points
    Run                                       +1
    Boundary Bonus                            +4
    Six Bonus                                 +6
    25 Run Bonus                              +4
    Half-Century Bonus                        +8
    75 Run Bonus                             +12
    Century Bonus                            +16
    Dismissal for a duck                     -2
    (Batter, Wicket-Keeper, & All-Rounder)   

    Important points
    Any player scoring a century will only get points for the century. No points such as 30 run Bonus or Half-century Bonus will be awarded here. Additionally, no points are awarded for centuries in T10 matches.
    If any runs are scored on an overthrow, points for those runs will be credited to the batter on strike for that ball. However, if the overthrow goes for a boundary, the batter will not receive extra Boundary Bonus points.

    Bowling Points
    Dot Ball                                +1
    Wicket (Excluding Run Out)              +25
    Bonus (LBW/Bowled)                      +8
    3 Wicket Bonus                          +4
    4 Wicket Bonus                          +8
    5 Wicket Bonus                         +12
    Maiden Over                            +12


    Fielding Points
    Catch                                   +8
    3 Catch Bonus                           +4
    Stumping                                +12
    Run out (Direct hit)                    +12
    Run out (Not a direct hit)              +6
    Important points
    A direct hit is inflicted by the fielder, who is the only one to touch the ball after the batter faces the delivery. In all other cases, points will be awarded only to the last 2 fielders who touch the ball.
    Players taking more than 3 catches will also get 4 points as 3 Catch Bonus. For example, if a player takes 6 catches, they will not get 8 points.

    Other Points
    Captain                                  2X
    Vice Captain                             1.5x
    In announced lineups                     +4

    Economy Rate Points (Min 2 Overs To Be Bowled)
    Below 5 runs per over                    +6
    Between 5-5.99 runs per over             +4
    Between 6-7 runs per over                +2
    Between 10-11 runs per over              -2
    Between 11.01-12 runs per over           -4
    Above 12 runs per over                   -6


    Strike Rate (Except Bowler) Points (Min 10 Balls To Be Played)
    Above 170 runs per 100 bowls             +6
    Between 150.01-170 runs per 100 balls    +4
    Between 130-150 runs per 100 balls       +2
    Between 60-70 runs per 100 balls         -2
    Between 50-59.99 runs per 100 balls      -4
    Below 50 runs per 100 balls              -6
    Important points
    Negative points for low batting Strike Rates are only applicable for individual Strike Rates of 70 runs per 100 balls or below.

    Playing Substitute
    Concussion, X-Factor, or Impact Player   +4
       
    Use the match information and the match analysis from the previous (players_task) task to select players.
    For each selected player, provide rationale based on their statistics, current form, pitch conditions, and matchup specifics.
        """,
        expected_output="""A complete Dream11 team with:
        - List of all 11 players with their roles (WK/BAT/AR/BOWL) + 2 additional players total 13 players
        - Captain and Vice-Captain selections with reasoning
        - Team breakdown (how many players from each team)
        - Rationale for key selections based on match conditions and player statistics
        If user want to add it's own choice player from both teams change that to the player he want to remove
        """,
        agent=agent,
        context=[players_task],
        human_input=True
    )