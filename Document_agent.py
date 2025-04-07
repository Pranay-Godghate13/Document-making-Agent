from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()


web_search_agent=Agent(
    name="Oracle document making agent",
    role="Search the Oracle documentation for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources",
        "Check oracle documentation for all the information",
        "Document should contain commands and what does command does"],
    show_tool_calls=True,
    markdown=True,
)

web_search_agent.print_response("""Make a documentation for Restore point creation and drop, which have commands and what does 
                                that command does""",stream=True)







































# web_search_agent=Agent(
#     name="Web search agent",
#     role="Search the web for the information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources"],
#     show_tool_calls=True,
#     markdown=True,
# )

# finance_agent = Agent(
#     name="Finance Agent",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True)],
#     instructions=["Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# research_team=Agent(
#     name="Research Team",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     team=[web_search_agent,finance_agent],
#     instructions=["Always include sources","Use tables to display data"],
#     show_tools_calls=True,
#     markdown=True,
# )

# research_team.print_response("Summarize analyst recommendation and share the latest news for TATA",stream=True)