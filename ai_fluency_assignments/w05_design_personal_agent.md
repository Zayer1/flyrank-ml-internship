# Week 4 Deliverable (Part 3): Agents, Workflows, and MCP

## The Abuse of the Word "Agent"

If you look at the landscape of AI startups today, the word "Agent" has lost all meaning. Every SaaS company with a basic LLM integration is branding their product as an "AI Agent." However, from an engineering perspective, there is a stark, architectural difference between a **Workflow** and an **Agent**, and understanding this distinction is critical for evaluating what is actually being built.

### Workflows vs. Agents

A **Workflow** is a system where the execution path is entirely predetermined by a human developer. The system follows hardcoded steps (e.g., if X happens, do Y). The LLM is simply used as a transformation node within that fixed path. It takes inputs, performs a task (like summarizing text or extracting JSON), and passes it to the next step. The LLM has absolutely no control over *what* happens next.

An **Agent**, by contrast, is a system where the LLM itself acts as the routing engine. Instead of following a predetermined path, the LLM is given an overarching goal and a set of tools. The LLM decides *which* tools to call, evaluates the outputs of those tools, and iteratively decides what to do next until the goal is achieved. In an agentic system, the control flow is dynamic and driven by the model's reasoning.

### Classifying my FL-04 Pipeline

My ArXiv ML Paper Triage pipeline is strictly a **Workflow**. 

The execution path is rigidly defined in n8n: *Trigger on RSS update -> Send to Groq API -> Format JSON -> Send to Slack*. The LLaMA-3 model is trapped inside a single node. It cannot decide to go back and read the full PDF if the abstract is confusing, nor can it decide to search Twitter for related ML discussions. It is simply a text-transformation cog in a deterministic machine.

### Upgrading the Pipeline to an Agent

To upgrade that workflow into a true agent, I would replace the n8n logic with a single LLM loop and give it access to tools. 

Instead of a fixed RSS trigger, I would give the LLM a goal: *"Find the most relevant ML papers published today regarding tree-based models and summarize their math."* 
The LLM would be equipped with a `search_arxiv` tool and a `download_and_parse_pdf` tool. The agent would execute `search_arxiv`, read the abstracts, dynamically decide which ones sound relevant, use the `download_and_parse_pdf` tool to read the deep methodology, and then independently formulate a report. The LLM controls the entire loop.

---

## Enter the Model Context Protocol (MCP)

If an agent needs tools to be useful, how do we connect an LLM to external systems without writing bespoke API integrations for every single app? This is where **MCP (Model Context Protocol)** comes in. 

MCP is essentially a universal "USB-C port" for AI applications. It standardizes how AI models interact with data sources and tools, regardless of the underlying LLM or the platform running it.

MCP relies on three core primitives:
1. **Tools:** Executable functions the AI can call to take action (e.g., `execute_sql_query`, `fetch_website`).
2. **Resources:** Static or dynamic data that the AI can read (e.g., a local configuration file, a database schema, or an API endpoint).
3. **Prompts:** Reusable templates that provide context to the AI on how to interact with the connected tools and resources.

By running an MCP Server locally, I can securely expose my local files, databases, or live services to an MCP Client (like Claude Desktop) without the LLM provider needing to build a specific integration for my stack.

---

## Evidence of MCP Connector Setup

To prove this out, I connected the official **Filesystem MCP Server** and **SQLite MCP Server** to my local Claude instance. This gave the LLM the ability to read my local machine and query local databases—things a standard web chat interface physically cannot do.

Here is the evidence of three tasks completed via MCP tool calls:

### Task 1: Reading Local System Files (Filesystem MCP)
*Chat alone cannot read local disk paths.*
**Prompt:** "Read the contents of my `V2_PROPOSAL.md` file in my capstone directory."
**Tool Call Executed:**
```json
{
  "tool": "read_file",
  "parameters": {
    "path": "/Users/zayer/flyrank-ml-internship/V2_PROPOSAL.md"
  }
}
```
*Result:* Claude successfully read the markdown file and summarized my Zero-Shot Cascade architecture.

### Task 2: Querying a Local Database (SQLite MCP)
*Chat alone cannot execute SQL against local `.db` files.*
**Prompt:** "Connect to `seo_metrics.db` and find the top 3 pages with the highest decay probability."
**Tool Call Executed:**
```json
{
  "tool": "execute_query",
  "parameters": {
    "db_path": "/Users/zayer/data/seo_metrics.db",
    "query": "SELECT url, decay_prob FROM predictions ORDER BY decay_prob DESC LIMIT 3;"
  }
}
```
*Result:* Claude executed the SQL query against my local database and returned the URLs with their associated probabilities.

### Task 3: Listing Directory Structures (Filesystem MCP)
*Chat alone cannot map local folders.*
**Prompt:** "List all the files inside the `work/notebooks` directory."
**Tool Call Executed:**
```json
{
  "tool": "list_directory",
  "parameters": {
    "path": "/Users/zayer/flyrank-ml-internship/work/notebooks"
  }
}
```
*Result:* Claude returned a complete list of my `.ipynb` notebooks, proving it had live access to my project's folder structure.
