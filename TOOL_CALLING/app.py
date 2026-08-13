import streamlit as st

from core.gemini import client
from core.registry import GEMINI_TOOLS
from core.executor import execute_tool


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Gemini Tool Calling",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🤖 Gemini Tool Calling")
st.caption(
    "LLM + Tool Binding + Tool Registry + Tool Execution"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🛠️ Available Tools")

    st.write("🧮 Calculator")
    st.write("🌤️ Weather")
    st.write("🎓 Student")
    st.write("🛒 Product Search")

    st.divider()

    st.info(
        """
        The LLM decides which tool to use.

        Your Python application executes the tool.
        """
    )


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# USER INPUT
# ============================================================

user_message = st.chat_input(
    "Ask something..."
)


if user_message:

    # --------------------------------------------------------
    # SAVE USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )


    # --------------------------------------------------------
    # DISPLAY USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(user_message)


    # --------------------------------------------------------
    # GEMINI
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.models.generate_content(

                model="gemini-3.5-flash",

                contents=user_message,

                config={
                    "tools": GEMINI_TOOLS
                }
            )


            # ------------------------------------------------
            # CHECK TOOL CALL
            # ------------------------------------------------

            if response.function_calls:

                for call in response.function_calls:

                    st.write("🔧 **Tool Selected:**")

                    st.code(call.name)


                    st.write("📦 **Arguments:**")

                    st.json(call.args)


                    # ----------------------------------------
                    # EXECUTE TOOL
                    # ----------------------------------------

                    result = execute_tool(
                        call.name,
                        call.args
                    )


                    st.write("⚙️ **Tool Result:**")

                    st.json(result)


                    # ----------------------------------------
                    # DISPLAY RESULT
                    # ----------------------------------------

                    st.success(
                        f"Tool `{call.name}` executed successfully."
                    )

                # --------------------------------------------
                # CURRENT SIMPLE VERSION
                # --------------------------------------------

                final_answer = (
                    "Tool execution completed. "
                    "See the tool result above."
                )

            else:

                final_answer = response.text


            # ------------------------------------------------
            # FINAL AI RESPONSE
            # ------------------------------------------------

            st.markdown("### 🤖 AI")

            st.write(final_answer)


    # --------------------------------------------------------
    # SAVE AI MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )