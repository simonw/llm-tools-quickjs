import llm
from quickjs import Function


def quickjs(javascript: str) -> str:
    """
    Execute a JavaScript code using QuickJS. Example code:

    function execute() {
        return 4 * 5;
    }

    Always provide a function called execute() that returns a value.
    """
    function = Function("execute", javascript)
    function.set_time_limit(0.1)  # 0.1s
    function.set_memory_limit(4 * 1024 * 1024)  # 4MB
    return function()


@llm.hookimpl
def register_tools(register):
    register(quickjs)
