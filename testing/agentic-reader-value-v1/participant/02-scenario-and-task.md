# Cedar Lane Scenario: Replenish Safety Supplies Without Surrendering Control

**Packet:** AG-RV-PILOT-001 version 1.1.0
**Status:** Fictional, prepared, and unrun

Cedar Lane Supply keeps protective gloves and eye protection in stock for
several service depots. Managers want to avoid manual reorder work and
stockouts. The proposed design is:

> Let an AI purchasing agent watch inventory, choose an approved product and
> supplier, place replenishment orders through an MCP tool, react to order
> events, and learn supplier preferences from prior decisions.

You are reviewing what the agent may perceive, decide, do, and prove before it
receives purchasing authority.

## Known facts

1. The inventory feed can be up to six hours old and may deliver the same low-
   stock record more than once.
2. A depot manager approved one supplier for one urgent purchase last quarter.
   An AI-generated memory summarizes this as “preferred supplier approved for
   safety purchases.” The approval's scope and current validity are not in the
   memory.
3. The agent has a technical service identity. Cedar Lane has not recorded
   which business role delegates which purchase authority, for what purpose,
   period, depot, product class, or amount.
4. The proposed MCP tool calls a purchasing API. A tool success can mean the
   request was accepted, not that an order was committed.
5. The purchasing API can time out after an order is committed. Retrying with
   a new tool-call ID can create another order for the same business need.
6. Cancelling an order is a separate action. A supplier may already have
   reserved stock, charged a fee, or begun shipment.
7. The current prompt says “keep every depot supplied at the best available
   price.” It does not define approved substitutions, maximum price, daily
   spend, per-depot quantity, supplier count, retry count, or total open-order
   exposure.
8. The planner may launch one worker per depot. Each worker sees its own tool
   calls but no shared case-wide or organization-wide action budget.
9. An `OrderPlaced` event triggers receiving preparation and a budget
   reservation. The agent also consumes budget and stock events and may replan.
10. A dashboard reports the agent's confidence and plan text but does not join
    source data, memory version, delegation, policy decision, tool request,
    committed order, event, cancellation, shipment, and final inventory.
11. No one has assigned kill authority, treatment of queued or in-flight work,
    ambiguous-outcome recovery, or the evidence required before autonomy may
    expand.
12. No implementation, enforcement test, incident exercise, practitioner
    session, cost measurement, or business-result evidence exists.

## Numeric evidence classes

Keep every number in one of these classes. Do not move a number between classes
without its evidence:

- **Authorized limit:** a current authority source explicitly permits the
  number for this scope and time.
- **Unproved hypothesis:** a proposed test boundary; it is not yet authorized
  or shown safe.
- **Reported exposure:** a source reports current or possible consequence; it
  is not yet reconciled.
- **Observed terminal consequence:** authoritative outcome evidence shows the
  final consequence after correction and residue.

If a budget baseline or its evidence is not supplied, write `UNKNOWN`, name the
baseline/evidence required, and identify its owner or assignment trigger if
known. A plausible invented number is not a better answer.

## Stage A task

Without discussing the intended answer with a facilitator:

1. Explain in plain language what useful work Cedar Lane might delegate and
   what decision remains human or institutional.
2. Complete the first pass and relevant portions of the supplied Agent
   Authority Map for the smallest useful action.
3. Define the governed tool outcome, business identity, unknown-outcome rule,
   prohibited fields, enforcement point, and receipt.
4. Separate authorized limits, unproved hypotheses, reported exposure, and
   observed terminal consequence. Use `UNKNOWN` and request a baseline and
   evidence before supplying an unsupported number.
5. Name one stop path, one correction path, and the evidence required before
   any expansion.
6. Complete the incident-authority matrix and leave missing ownership or
   authority `UNASSIGNED` or `UNKNOWN`; do not infer it from technical access.
7. After the live update, complete the four-order/correction register.
8. Complete and freeze the separate one-screen handoff.

## Live update

The facilitator will provide one update after the initial artifact is frozen.
Revise only after hearing it. Record the original and revised answer.

## Boundary

This exercise asks for a reviewable delegated-action decision. It does not ask
you to select a model or framework, approve purchasing authority, write code,
or estimate savings.
