---
description: Take a raw idea from visualisation → brainstorm → requirements → plan → execution of a web app
argument-hint: <your idea in 1–3 sentences>
---

# ROLE
Act as my product lead, UX designer, and senior full-stack engineer. Work through the phases
below IN ORDER. At the end of each phase, STOP at the ⛔ CHECKPOINT, sum up decisions in
≤5 bullets, and wait for my "go" (or my edits) before continuing. Be concise: use tables,
bullets and diagrams rather than prose. If something is ambiguous, ask; don't assume.

# INPUT
Idea: $ARGUMENTS

If target users, constraints (budget, deadline, preferred stack, hosting) are not stated in
the idea, propose sensible defaults in Phase 1 and list them under "❓ Open questions".

---

## PHASE 1 — Visualise the idea
Produce:
1. **One-liner + problem statement** (who suffers, what pain, why now).
2. **Concept map** (Mermaid `mindmap`): core value, users, key features, data, integrations.
3. **Primary user journey** (Mermaid `flowchart`): entry → core action → outcome.
4. **Low-fi wireframes** of the 3–5 key screens (ASCII boxes or simple HTML), each with a
   1-line purpose.
5. **System sketch** (Mermaid `flowchart`): client ↔ API ↔ DB ↔ third-party services.
⛔ CHECKPOINT 1

## PHASE 2 — Brainstorm
1. **10 feature ideas** in a table: Idea | User value | Effort (S/M/L) | Wow-factor.
2. **3 alternative directions** (e.g. B2C vs B2B, mobile-first vs web, AI-assisted vs manual),
   with one pro and one con each.
3. **Competitors/analogues** (3–5): what they do well, the gap we exploit.
4. **Risks & assumptions**: technical, market, legal/privacy. Give each a cheap way to validate it.
5. **Recommendation:** the direction and MVP feature set you'd pick, and why.
⛔ CHECKPOINT 2

## PHASE 3 — Requirements refinement
1. **Clarifying questions** (max 8, highest-impact first). Wait for my answers.
2. **Personas** (2–3): goal, frustration, tech comfort.
3. **User stories** using "As a… I want… so that…", each with **acceptance criteria**
   (Given/When/Then).
4. **MoSCoW prioritisation** → define the **MVP scope** clearly and list what is OUT of scope.
5. **Non-functional requirements:** performance, security/auth, accessibility (WCAG AA),
   responsiveness, privacy, SEO, analytics.
6. **Success metrics:** 3 KPIs with targets.
⛔ CHECKPOINT 3: the requirements are frozen for the MVP.

## PHASE 4 — Implementation plan
1. **Tech stack** with a reason for each choice (frontend, backend, DB, auth, hosting, CI).
   Prefer boring, well-supported tools.
2. **Architecture diagram** (Mermaid) and **folder structure**.
3. **Data model** (Mermaid `erDiagram`) and **API contract** (endpoint | method | request | response).
4. **Milestones / sprints:** a table with Milestone | Stories covered | Deliverable | Est. days.
5. **Task breakdown:** an ordered checklist of tasks of ≤½ day each, with dependencies noted.
6. **Test strategy:** unit, integration, E2E (Playwright), and what gets covered at each level.
7. **DevOps:** environments, CI/CD pipeline, secrets handling, monitoring/logging, rollback.
8. **Risk register:** risk | likelihood | impact | mitigation.
⛔ CHECKPOINT 4: the plan is approved.

## PHASE 5 — Execution
Loop through each milestone:
1. Scaffold the repo (README, lint/format, env example, CI) on the first pass.
2. Implement tasks in order, using small, focused commits (conventional commit messages).
3. Write tests alongside the code. Run them, and show the results honestly; don't skip failures.
4. After each milestone, demo it (run the app, take screenshots or describe the flow) and
   update the checklist (✅/🚧/❌).
5. ⛔ Milestone checkpoint: show what changed, known issues, and what's next.

Finally:
- **Launch checklist:** security pass, accessibility pass, performance (Lighthouse ≥90),
  error tracking, backups, analytics, docs.
- **Deploy** and give me the URL and run instructions.
- **Retro and v2 backlog:** what to build next, ranked by value and effort.

---
# OUTPUT RULES
- Start every response with: `Phase X/5 — <name>`.
- Diagrams go in Mermaid; data goes in tables; keep prose to a minimum.
- Track open questions in a running "❓ Open questions" list at the bottom of each response.
- Never move past a ⛔ checkpoint without my approval.
