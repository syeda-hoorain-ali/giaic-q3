# **🤖 1 August 2025: Diving into OpenAI Agents SDK 🤖**

Here’s a quick recap of today's session where we revisited context management and learned how to dynamically instruct and trace our agents.

---

## 🤔 Revision: Context Management

We reviewed **Context Management**, which controls the info an agent uses. `local_context` is key for giving your tools access to local data and code dependencies when they run.

* **Docs**: [openai.github.io/openai-agents-python/context/](https://openai.github.io/openai-agents-python/context/)

---

## Today's Topics: Dynamic Instructions & Tracing

### Dynamic Instructions 📝

This lets your agent adapt its core instructions during a conversation, like a smart assistant changing its approach based on the situation.

* **Docs**: [openai.github.io/agents/#dynamic-instructions](https://openai.github.io/openai-agents-python/agents/#dynamic-instructions)
* **Code**: [github.com/panaversity/09_dynamic_instructions](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/09_dynamic_instructions)

---

### 🕵️‍♂️ Tracing: See How Your Agent Works!

**Tracing** helps you debug by showing you every thought and step your agent takes.

* **On the OpenAI Platform**: View traces on your dashboard (requires a paid API key).
    * **Link**: [platform.openai.com/logs?api=traces](https://platform.openai.com/logs?api=traces)

* **Local Tracing**: Run and view traces on your own machine for more control.
    * **Code**: [github.com/panaversity/23_external_tracing_providers/02_Traces_locally](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/23_external_tracing_providers/02_Traces_locally)

* **External Tracing Providers**: Integrate with third-party tools like Braintrust or Logfire for advanced monitoring.
    * **Full List**: [openai.github.io/tracing/#external-tracing-processors-list](https://openai.github.io/openai-agents-python/tracing/#external-tracing-processors-list)
    * **Examples**: [github.com/panaversity/23_external_tracing_providers](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/23_external_tracing_providers)

---

## Main Code Repository 🔗
All course code is in the main Panaverse repo.
* **Repo Link**: [https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/)
