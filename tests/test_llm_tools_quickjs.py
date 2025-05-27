import llm
import json
from llm_tools_quickjs import QuickJS, quickjs


def test_toolbox_tool():
    model = llm.get_model("echo")
    code = """
    function execute() {
        return "hello: " + (45 * 16);
    }
    execute()
    """
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {
                        "name": "QuickJS_execute_javascript",
                        "arguments": {"javascript": code},
                    }
                ]
            }
        ),
        tools=[QuickJS()],
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {
            "name": "QuickJS_execute_javascript",
            "output": "hello: 720",
            "tool_call_id": None,
        }
    ]


def test_function_tool():
    model = llm.get_model("echo")
    code = """
    function execute() {
        return "hello: " + (45 * 16);
    }
    """
    chain_response = model.chain(
        json.dumps(
            {"tool_calls": [{"name": "quickjs", "arguments": {"javascript": code}}]}
        ),
        tools=[quickjs],
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {"name": "quickjs", "output": "hello: 720", "tool_call_id": None}
    ]
