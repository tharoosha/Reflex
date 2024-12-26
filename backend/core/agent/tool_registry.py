from db.aiven_connection import get_db_url
from phi.tools.sql import SQLTools
# Import other tools as needed, e.g., SearchTool, CalculatorTool



class ToolRegistry:
    """
    Centralized registry for initializing tools dynamically.
    """

    @staticmethod
    def get_tools(tool_names: list):
        """
        Initialize tools based on their names.

        :param tool_names: List of tool names to initialize.
        :return: List of initialized tools.
        """
        tools = []
        for tool_name in tool_names:
            if tool_name == "SQLTool":

                db_url = get_db_url()
                tools.append(SQLTools(db_url=db_url))

            # Add more tools here as needed
            # elif tool_name == "SearchTool":
            #     tools.append(SearchTool())
            # elif tool_name == "CalculatorTool":
            #     tools.append(CalculatorTool())
            else:
                raise ValueError(f"Tool '{tool_name}' is not recognized.")
        return tools
