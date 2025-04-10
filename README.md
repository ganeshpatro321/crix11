# Crix11 - Dream11 AI Agent for IPL 2025

An AI-powered Dream11 team selection system for IPL 2025 using the CrewAI framework.

## Overview

This system uses four specialized agents to create an optimized fantasy cricket team:

1. **Today's Teams Agent**: Identifies matches, analyzes pitch conditions and team records
2. **User Team Selector Agent**: Helps users choose specific teams for team creation
3. **Players Agent**: Analyzes player statistics, performance, and playing 11 details
4. **Team Selector Agent**: Optimizes team selection following Dream11 rules

## Features

- Data-driven player selection - Consideration of match conditions
- Flexible captain/vice-captain choices
- User customization options

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crix11.git
cd crix11
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
- Create a `.env` file with your API keys and URLs
- Example:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
MATCH_URL=https://www.iplt20.com/matches
PLAYER_STATS_URL=https://www.iplt20.com/stats/2025
```

## Usage

Run the main script:
```bash
python main.py
```

The system will:
1. Find today's IPL matches
2. Ask you to select teams for Dream11
3. Analyze player stats and match conditions
4. Generate an optimized Dream11 team
