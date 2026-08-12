from core.gemini import client
from core.registry import GEMINI_TOOLS
from core.executor import execute_tool


# ============================================================
# 1. HUMAN MESSAGE
# ============================================================

user_message = "What is 25 multiplied by 20?"

print("\n👤 HUMAN")
print(user_message)


# ============================================================
# 2. SEND MESSAGE TO GEMINI
# ============================================================

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=user_message,
    config={
        "tools": GEMINI_TOOLS
    }
)


# ============================================================
# 3. READ AI TOOL CALL
# ============================================================

if response.function_calls:

    for call in response.function_calls:

        print("\n🤖 AI TOOL CALL")

        print("Tool name:")
        print(call.name)

        print("\nArguments:")
        print(call.args)


        # ====================================================
        # 4. EXECUTE TOOL
        # ====================================================

        result = execute_tool(
            call.name,
            call.args
        )


        print("\n🔧 TOOL EXECUTION")

        print("Tool:")
        print(call.name)

        print("Result:")
        print(result)


else:

    print("\n🤖 AI")
    print(response.text)