from core.gemini import client
from core.registry import GEMINI_TOOLS
from core.executor import execute_tool


# ============================================================
# USER MESSAGE
# ============================================================

user_message = input("\n👤 You: ")


# ============================================================
# SEND TO GEMINI
# ============================================================

response = client.models.generate_content(

    model="gemini-3.5-flash",

    contents=user_message,

    config={
        "tools": GEMINI_TOOLS
    }
)


# ============================================================
# CHECK TOOL CALL
# ============================================================

if response.function_calls:

    for call in response.function_calls:

        print("\n🤖 AI TOOL CALL")

        print("Tool:")
        print(call.name)

        print("Arguments:")
        print(call.args)


        # ====================================================
        # EXECUTE TOOL
        # ====================================================

        result = execute_tool(
            call.name,
            call.args
        )


        print("\n🔧 TOOL RESULT")

        print(result)


else:

    print("\n🤖 AI")

    print(response.text)