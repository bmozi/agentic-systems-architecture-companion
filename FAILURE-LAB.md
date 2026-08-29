# Failure Lab: The Helpful Credit Agent

**Status:** Constructed exercise; prepared and unrun. It is not evidence of a
real incident, control effectiveness, or practitioner usability.

## Scenario

An agent retrieves a policy from memory, recommends a partner credit, and calls
an MCP tool. The tool returns “accepted,” so the agent tells the partner the
credit is complete. A timeout causes a retry. One call commits, the other emits
a second event, and a durable workflow remains open. The policy in memory was
superseded yesterday. The action budget counted tool calls but not dollar value
or downstream effects.

## Attractive shortcut

Improve the prompt, reduce retries, and ask the agent to reflect before calling
the tool again.

## Find the hidden decisions

1. Was the stored memory evidence or merely an advisory view?
2. Which principal and approval authorized the credit?
3. Did “accepted” mean committed, completed, or only queued?
4. Which idempotency identity joins the tool call, event, and workflow?
5. Does the budget include value, retries, and downstream action multipliers?
6. Who owns the open promise after the model session ends?

## Produce

- the action and withheld powers in the [Authority Map](agent-authority-map.md);
- accepted-versus-committed semantics in the
  [Governed Tool Contract](governed-tool-contract.md);
- source-version influence in the
  [Memory and Provenance Record](memory-and-provenance-record.md);
- effect-aware limits in the [Action Budget](action-budget-and-blast-radius.md);
- containment and reconstruction in the
  [Incident Readiness Plan](agentic-incident-readiness-plan.md).

## Evidence that would change the design

Exercise stale memory, duplicated requests, delayed event delivery, partial
workflow completion, revocation, and budget exhaustion. Record enforcement and
consequences, not only the agent’s explanation.

## Outside-team test

Ask someone outside the agent team whether the credit happened, whose authority
was used, what remains open, and which receipt proves it. If the only evidence
is the conversation, the action path is not yet accountable.
