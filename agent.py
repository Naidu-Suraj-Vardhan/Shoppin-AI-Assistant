from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from tools import *
import os
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI API key from the environment variables
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Define a list of tools that the agent can use
tools = [
    ecommerce_search, 
    shipping_estimator, 
    discount_checker, 
    competitor_price_comparison, 
    return_policy_checker,
    get_today_date_and_day
]

# Initialize a language model with specific parameters
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

# Create a reactive agent using the language model and tools
graph = create_react_agent(llm, tools=tools)

def agent_output(query):
    """
    Processes a user query through the react agent and returns the agent's response.

    Args:
        query (str): The user's query to be processed by the agent.

    Returns:
        str: The content of the agent's response.
    """
    # Prepare the input for the agent
    inputs = {"messages": [("user", query)]}
    
    # Stream the output from the agent with a recursion limit
    for output in graph.stream(inputs, {"recursion_limit": 150}):
        # Print the agent's message if available
        if 'agent' in output:
            pprint(output['agent']['messages'][-1])
        # Print the tool's message if available
        elif 'tools' in output:
            pprint(output['tools']['messages'][-1])
    
    # Return the first message content from the agent's response
    return output['agent']['messages'][0].content