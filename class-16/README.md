# **🤖 29 August 2025: Diving into OpenAI Agents SDK 🤖**

Today, we explored advanced tool customization to gain precise control over agent behavior and clarified the difference between **stateless** and **stateful** APIs.

---

## 🛠️ Advanced Tool Customization

We learned how to precisely manage our agent's tools:

* **`tool_use_behavior`**: This pattern controls the agent's execution flow around tool calls.
    * **`"run_llm_again"` (The Default Thinker)**: This is the standard behavior. After a tool runs, its output is sent back to the LLM. The LLM then analyzes the result and decides what to do next.
    * **`"stop_on_first_tool"` (The Direct Responder)**: This mode stops execution immediately after the first tool call. The raw output of that tool becomes the agent's final answer. The LLM does not see the tool's result.
  * **`StopAtTools` (The Workflow Finisher)**: This mode gives you surgical control. You provide a list of "finalizing" tool names. The agent will run its workflow but stop immediately after one of those specific tools is called.


* **`name_override` & `description_override`**: If provided, use this name/description for the tool instead of the function's name/function's docstring.

* **`is_enabled`**: The `is_enabled` flag on a `@function_tool` lets you make tools available only when conditions are right.

* **Dynamic `is_enabled`**: This is where it gets powerful. You can pass a function to `is_enabled` that checks the current context. The tool will only be available if the function returns `True`.

* **`failure_error_function`**: This allows you to define a custom callback function that executes when a tool's code throws an error. It gives you full control over error handling, logging, and retry logic.

---

## 🧠 Completions vs. Responses: Stateless vs. Stateful 

We also clarified the two main ways to interact with the API:

* **Completions API (Stateless)**: Think of this like a single function call. It has no memory of past interactions. You must send the entire context (like previous messages) with every single request.

* **Responses API (Stateful)**: This is like an ongoing conversation. The API manages the chat history and state for you. You can simply send the next message, and it remembers the context of what was said before.

---

## 📗 Class Resources 

* **Panaverse Repo (Advanced Tools)**: [https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/15_advanced_tools](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/15_advanced_tools)
* **Today's Class Code**: [https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-16](https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-16)
