# 🧠 Full AI Coding Assistant Workflow

This guide outlines a repeatable, structured process for working with AI coding assistants to build production-quality software. We'll use the example of building a Supabase MCP server with Python, but the same process applies to any AI coding workflow.

## 1. 🔑 Golden Rules

These are the high-level principles that guide how to work with AI tools efficiently and effectively. We’ll be implementing these through global rules and our prompting throughout the process:

*   Use markdown files to manage the project (`README.md`, `PLANNING.md`, `TASK.md`).
*   Keep files under 500 lines. Split into modules when needed.
*   Start fresh conversations often. Long threads degrade response quality.
*   Don’t overload the model. One task per message is ideal.
*   Test early, test often. Every new function should have unit tests.
*   Be specific in your requests. The more context, the better. Examples help a lot.
*   Write docs and comments as you go. Don’t delay documentation.
*   Implement environment variables yourself. Don’t trust the LLM with API keys.
*   [!WARNING] Don’t be "that guy" (implied: the one who ignores best practices).

## 2. 🧠 Planning & Task Management

Before writing any code, it’s important to have a conversation with the LLM to plan the initial scope and tasks for the project. Scope goes into `PLANNING.md`, and specific tasks go into `TASK.md`. These should be updated by the AI coding assistant as the project progresses.

### `PLANNING.md`

*   **Purpose**: High-level vision, architecture, constraints, tech stack, tools, etc.
*   **Prompt to AI**:
    > "Use the structure and decisions outlined in `PLANNING.md`."
*   Have the LLM reference this file at the beginning of any new conversation.

### `TASK.md`

*   **Purpose**: Tracks current tasks, backlog, and sub-tasks.
*   **Includes**: Bullet list of active work, milestones, and anything discovered mid-process.
*   **Prompt to AI**:
    > "Update `TASK.md` to mark XYZ as done and add ABC as a new task."
*   Can prompt the LLM to automatically update and create tasks as well (through global rules).

## 3. ⚙️ Global Rules (For AI IDEs)

Global (or project level) rules are the best way to enforce the use of the golden rules for your AI coding assistants.
Global rules apply to all projects. Project rules apply to your current workspace. All AI IDEs support both.

*   Cursor Rules: [Cursor Rules](https://docs.cursor.com/context/rules-for-ai)
*   Windsurf Rules: [Windsurf Rules](https://docs.codeium.com/windsurf/memories#windsurfrules)
*   Cline Rules: [Cline Rules](https://docs.cline.bot/improving-your-prompting-skills/prompting)
*   Roo Code Rules: Works the same way as Cline

Use the below example (for our Supabase MCP server) as a starting point to add global rules to your AI IDE system prompt to enforce consistency:

``````text
### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).

### 🧪 Testing & Reliability
- **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case

### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.

### 📎 Style & Conventions
- **Use Python** as the primary language.
- **Follow PEP8**, use type hints, and format with `black`.
- **Use `pydantic` for data validation**.
- Use `FastAPI` for APIs and `SQLAlchemy` or `SQLModel` for ORM if applicable.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.
``````

## 4. 🧰 Configuring MCP

MCP enables your AI assistant to interact with services to do things like:

*   Use the file system (read/write, refactor, multi-file edits) - *[Link to server/docs needed]*
*   Search the web (great for pulling documentation) with Brave - *[Link to server/docs needed]*
*   Use Git (branching, diffing, committing) - *[Link to server/docs needed]*
*   Access memory and other tools (e.g., connecting Qdrant)

Want more MCP servers?
*View a large list of MCP servers with installation instructions here.* - *[Link to list needed]*

**How to Configure MCP**

*   Cursor MCP: [Cursor MCP](https://docs.cursor.com/context/model-context-protocol)
*   Windsurf MCP: [Windsurf MCP](https://docs.codeium.com/windsurf/mcp)
*   Cline MCP: [Cline MCP](https://docs.cline.bot/mcp-servers/mcp)
*   Roo Code MCP: [Roo Code MCP](https://docs.roocode.com/features/mcp/using-mcp-in-roo)

**Example prompt made possible with the Git MCP server:**
> Okay great, I like the current state of the application. Please make a git commit to save the current state.

## 5. 💬 Initial Prompt to Start the Project

[!TIP] The first prompt is crucial!
Even with comprehensive planning docs and rules, provide detailed context, examples, and documentation links for the initial code generation.

**Ways to provide examples and documentation:**

1.  Use the built-in documentation feature of your AI IDE (e.g., `@docs:feature-name` in Cursor/Windsurf).
2.  Have the LLM use an MCP server (like Brave search) to find documentation online.
3.  Manually provide examples/documentation snippets in your prompt.

**Example prompt to create our initial Supabase MCP server with Python:**
```
Use `@docs:model-context-protocol-docs` and `@docs:supabase-docs` to create an MCP server written in Python (using FastMCP) to interact with a Supabase database. The server should use the Stdio transport and have the following tools:

*   Read rows in a table
*   Create a record (or multiple) in a table
*   Update a record (or multiple) in a table
*   Delete a record (or multiple) in a table

Be sure to give comprehensive descriptions for each tool so the MCP server can effectively communicate to the LLM when and how to use each capability.
The environment variables for this MCP server need to be the Supabase project URL and service role key.

Read this GitHub README to understand best how to create MCP servers with Python:
[https://github.com/modelcontextprotocol/python-sdk/tree/main](https://github.com/modelcontextprotocol/python-sdk/tree/main)

After creating the MCP server with FastMCP, update `README.md` and `TASK.md` since you now have the initial implementation for the server.
```

[!NOTE] Remember to restart conversations once they get long. You’ll know when it’s time when the LLM starts to frustrate you.

## 6. 🧩 Modular Prompting Process after Initial Prompt

For follow-up fixes or changes, focus on **one task per prompt** unless tasks are trivial. This yields more consistent results. Aim for the LLM to update a single file when possible.

*   **Good example:**
    > “Now update the `list_records` function to add a parameter for filtering the records.”
*   **Bad example:**
    > “Update list records to add filtering. Then I’m getting an error for the create row function that says API key not found. Plus I need to add better documentation to the main function and in `README.md` for how to use this server.”

[!IMPORTANT] Remember to always have the LLM update `README.md`, `PLANNING.md`, and `TASK.md` after making any changes!

## 7. ✅ Test After Every Feature

[!IMPORTANT] Catching bugs early prevents compounding problems!
Ensure the AI writes unit tests after each feature, or do it yourself as a follow-up.

**Best practices for testing (enforce via global rules or prompts):**

*   Create tests in a `tests/` directory mirroring the app structure.
*   Always **mock** external service calls (DB, APIs, LLMs) to avoid real interactions during tests.
*   For each function/feature, test at least:
    *   One successful scenario (happy path).
    *   One intentional failure (e.g., invalid input) to ensure proper error handling.
    *   One edge case (e.g., empty list, boundary values).

You can ask the AI to skip tests for a specific feature if it gets stuck, but aim for comprehensive test coverage.

## 8. 🐳 Docker Deployment (Supabase MCP Example)

Containerizing applications with Docker (or similar) is a reliable way to deploy and share projects. LLMs are generally proficient with Docker tasks.

**Dockerfile Example:**

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the MCP server files
COPY . .

CMD ["python", "server.py"]
```

**Build Command:**

```bash
docker build -t mcp/supabase .
```

**Example prompt to get this from the LLM:**

```
Write a Dockerfile for this MCP server using `requirements.txt`. Give me the commands to build the container after.
```

