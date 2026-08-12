from tools import (
    calculator,
    get_weather,
    get_student,
    search_product
)


# ============================================================
# PYTHON TOOL REGISTRY
# ============================================================

TOOL_REGISTRY = {

    "calculator": calculator,

    "get_weather": get_weather,

    "get_student": get_student,

    "search_product": search_product
}


# ============================================================
# TOOLS GIVEN TO GEMINI
# ============================================================

GEMINI_TOOLS = [

    calculator,

    get_weather,

    get_student,

    search_product
]