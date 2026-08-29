# Team Workshop: Delegate One Action Defensibly

Use this 90-minute session before giving an agent a consequential tool.

## Participants

Bring the work owner, agent developer, API or tool owner, security/governance,
operations, and a person accountable for the affected outcome.

## Agenda

### 0–15 minutes — Choose one useful action

Name the subject, affected object, consequence, and why delegation is valuable.
Do not scope the session as “approve the agent.”

### 15–30 minutes — Establish authority

Complete the first pass in the [Agent Authority Map](agent-authority-map.md).
Identify the principal, authority source, purpose, withheld powers, and
revocation path.

### 30–45 minutes — Govern the path

Map the model decision to the actual API or MCP capability. Define identity,
input constraints, idempotency, confirmation, and accepted-versus-committed
evidence in the [Governed Tool Contract](governed-tool-contract.md).

### 45–60 minutes — Bound accumulated consequence

Set action, value, time, resource, and retry budgets. Include downstream events
and workflow effects, not only tool-call count.

### 60–75 minutes — Disturb the design

Use the [Failure Lab](FAILURE-LAB.md). Introduce stale memory, timeout,
duplicated effect, expired approval, or a feedback loop. Name the owner after
the model session ends.

### 75–90 minutes — Define evidence and release

Complete one [Value and Evidence Ledger](VALUE-AND-EVIDENCE-LEDGER.md) row.
Choose a supervised release stage, evidence threshold, stop condition, and
reconsideration date.

## Read-back test

Ask an outside-role participant to explain the delegated action, withheld
power, budget, stop path, and proof. Record confusion as a design finding.
