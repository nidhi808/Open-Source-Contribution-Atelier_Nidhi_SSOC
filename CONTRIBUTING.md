# Contributing

Thanks for contributing to Open Source Contribution Atelier.

## Principles

- Keep contributions beginner-friendly and well-documented
- Prefer safe defaults and avoid introducing secrets into code
- Add tests for backend and frontend changes when practical
- Discuss large architectural changes before implementation

## Getting Started for SSoC

Welcome, Social Summer of Code (SSoC) Season 5 contributors! We are thrilled to have you here. To help you make high-quality, impactful contributions, follow this structured path:

### 1. Suggested First Tasks
If you are new to the codebase, look for issues with the following labels:
*   `good first issue` or `ssoc:good-first-issue`: Small, self-contained tasks (like typos, documentation, or minor UI tweaks).
*   `SSOC`: Standard issues curated specifically for the SSOC timeline.
*   **View all beginner-friendly issues here**: [Good First Issues](https://github.com/nidhi808/Open-Source-Contribution-Atelier_Nidhi_SSOC/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

### 2. Mentorship & Guidelines
*   **Ask to be assigned**: Comment on the issue you wish to work on. Please wait for a maintainer/mentor to assign the issue to you before writing code.
*   **One issue at a time**: To keep the contribution process fair, we only assign one issue per contributor at a time.
*   **Timeline**: Once assigned, you have **3 days** to open a draft PR or submit your changes. If there is no activity, the issue may be reassigned to keep the project moving forward.

### 3. Communication Channels
*   Use the **SSOC Discord server** inside the dedicated project channel to ask quick questions or discuss implementation details with mentors.
*   For technical discussions related to a specific issue, use that **GitHub Issue comments** so all project maintainers can view the context.

---

## Setup

Use the instructions in [README.md](README.md) to run the project locally.

## Branching

- Never commit directly to `main`
- Start every change by creating a new branch from `main`
- Use branch names such as `feature/terminal-feedback`, `fix/auth-tests`, or `docs/setup-guide`
- Use clear commit messages
- Open focused pull requests

Recommended commands:

```bash
git pull origin main
git switch -c feature/short-description
```

## Pull Requests

- Describe the problem and the chosen approach
- Include screenshots for UI changes
- Mention any schema or environment updates
- Confirm tests run locally
- Push your branch and open the PR from that branch into `main`

## Code Style

- Python: Black-compatible formatting, modular Django apps
- TypeScript: ESLint + Prettier, accessible React components
- Avoid large unrelated refactors in feature PRs

## Security

- Never commit `.env` files or tokens
- Do not add code that executes untrusted shell input
- Route exercise validation through the sandbox verifier service
- Do not commit generated artifacts such as `node_modules/`, `dist/`, or local virtual environments

## Lesson Contributions & Issues

- To propose a new lesson or exercise, open an issue titled `lesson: <short title>` and include:
	- a short summary, learning objectives, and the expected exercise command(s)
	- suggested order/placement in the track
	- any files or assets required
- If you want to work on the lesson yourself, comment on the issue and open a branch prefixed with `lesson/`.
- Use `python manage.py seed_lessons` to load the example lessons locally; maintainers will review and promote community-submitted lessons.

## Issue Hygiene For Maintainers

- Keep issue labels consistent: `bug`, `enhancement`, `curriculum`, `good first issue`, `needs-triage`, `blocked`.
- Close duplicate/outdated issues with a short reason and a pointer to the active issue.
- Convert vague issues into actionable tasks by adding scope and acceptance criteria.
- If an issue is stale for >30 days with no owner, either re-scope or close it with a reopen note.
