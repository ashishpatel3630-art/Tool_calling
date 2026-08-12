from core.registry import TOOL_REGISTRY


def execute_tool(
    tool_name: str,
    tool_args: dict
):

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:

        return {
            "error": f"Tool '{tool_name}' not found"
        }

    try:

        result = tool(**tool_args)

        return result

    except Exception as e:

        return {
            "error": str(e)
        }