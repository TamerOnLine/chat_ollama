from langchain.tools import Tool

def custom_response_tool(query: str) -> str:
    """
    Returns a default response if no other tool matches the query.
    """
    return f"Sorry, I don't have a tool for this request. Here is my best response: {query}"

custom_tool = Tool(
    name="GeneralResponse",
    func=custom_response_tool,
    description="Handles queries that do not match any predefined tool.",
    return_direct=True,
)
