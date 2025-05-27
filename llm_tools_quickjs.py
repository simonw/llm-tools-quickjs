import llm
from quickjs import Context, Function
from typing import Optional


class QuickJS(llm.Toolbox):
    _context: Optional[Context] = None

    def _get_context(self) -> Context:
        if not self._context:
            self._context = Context()
            # Set resource limits
            self._context.set_time_limit(0.1)
            self._context.set_memory_limit(4 * 1024 * 1024)
        return self._context

    def execute_javascript(self, javascript: str) -> str:
        """
        Execute JavaScript code using a persistent QuickJS context.
        State is maintained between calls, allowing you to define variables,
        functions, and objects that persist across executions.

        Example code:

        // First call - define a variable
        var counter = 0;
        function increment() { return ++counter; }
        increment();

        // Second call - the variable persists
        increment(); // returns 2

        You can return values directly or define and then run an execute() function.
        """
        context = self._get_context()
        try:
            result = context.eval(javascript)
            if hasattr(result, "json"):
                return result.json()
            return str(result) if result is not None else ""
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_context(self):
        """Reset the QuickJS context."""
        self._context = None


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
    register(QuickJS)
    register(quickjs)
