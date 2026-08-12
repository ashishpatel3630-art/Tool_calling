import os

from dotenv import load_dotenv
from google import genai

from tools import calculate


# ============================================================
# 1. GEMINI SETUP
# ============================================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ============================================================
# 2. TOOL REGISTRY
# ============================================================

tools = {
    "calculate": calculate
}


# ============================================================
# 3. HUMAN MESSAGE
# ============================================================

human_message = "What is 25 + 35?"


# ============================================================
# 4. SEND MESSAGE + TOOLS TO GEMINI
# ============================================================

response = client.models.generate_content(
    model="gemini-3.5-flash",

    contents=human_message,

    config={
        "tools": [calculate]
    }
)


# ============================================================
# 5. CHECK AI TOOL CALL
# ============================================================

if response.function_calls:

    for call in response.function_calls:

        tool_name = call.name

        tool_args = call.args

        print("\n==============================")
        print("AI TOOL CALL")
        print("==============================")

        print("Tool:", tool_name)

        print("Arguments:", tool_args)


        # ====================================================
        # 6. FIND TOOL
        # ====================================================

        tool_function = tools.get(tool_name)


        if tool_function is None:

            print("Tool not found!")

            continue


        # ====================================================
        # 7. EXECUTE TOOL
        # ====================================================

        result = tool_function(**tool_args)


        # ====================================================
        # 8. TOOL RESULT
        # ====================================================

        print("\n==============================")
        print("TOOL RESULT")
        print("==============================")

        print(result)

else:

    print("\nAI:", response.text)