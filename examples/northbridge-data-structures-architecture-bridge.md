# Northbridge Data-Structures Architecture Bridge

**Status:** Constructed teaching example; `PLANNED/UNRUN`

**Disclosure:** Northbridge Exchange, its warehouse, records, quantities,
workload, and outcomes are fictional composite teaching material. They are not
production measurements or John Briggs project history.

## Efficient selection is not delegated authority

An agent may use a hash index to retrieve inventory, a heap to rank urgent
orders, or a graph to propose a route. These structures support perception and
planning. They do not authorize reservation, shipment, worker assignment, or
relocation.

The delegated action must name the principal, subject, purpose, scope,
authority, action budget, stop condition, evidence, and reversal path. A stale
index, changed route, or reordered priority must cause revalidation or
abstention rather than an invisible expansion of power.

## Plain-language model: the map and the travel authorization

A map can show the shortest road. It does not grant permission to drive the
vehicle, enter a restricted site, spend company money, or ignore a closed road.
The agent needs both planning machinery and a travel authorization: who
delegated what, under which conditions, for how long, with what limits, and
with which stop and reversal paths.

```text
retrieve + rank + route -> recommendation with provenance
                        -> authority, approval, policy, and budget gate
                        -> act or abstain -> evidence -> reverse/escalate
```

If the heap's first item is treated as permission, stale priority can bypass a
human hold. If the shortest route is treated as authority, the agent can move
goods outside its scope. Missing authority or exhausted budget should produce
abstention, not a better guess.

| Agent-supported structure | Authority boundary |
| --- | --- |
| Hash lookup | Retrieval is not permission to act on the record. |
| Priority heap | Ranking is not permission to override policy or fairness. |
| Route graph | A proposed path is not authorization to execute it. |
| Analytical aggregate | A reported pattern is not proof of a causal decision. |

## Transfer artifact: bounded-delegation and reversal card

| Decision | Your answer |
| --- | --- |
| Recommendation and structures used | |
| Source, graph, priority, and policy versions | |
| Principal, subject, purpose, and authority | |
| Allowed, withheld, and approval-bound actions | |
| Value, rate, cost, time, and blast-radius budgets | |
| Revalidation and abstention triggers | |
| Stop authority, reversal owner, and correction path | |

## AI-amplified transfer to other systems

AI tools can generate candidate structures, implementation code, tests, and
diagrams for many domains. The architect supplies the governing decisions the
generated machinery must preserve.

| Transfer case | AI can accelerate | Decision the structure cannot settle |
| --- | --- | --- |
| Search-engine indexing | Crawlers, inverted indexes, ranking code, query tests | Content authority, freshness, deletion, ranking policy, and evidence |
| Social-media platforms | Social graphs, feeds, queues, moderation classifiers | Consent, identity, amplification limits, appeal, and causal responsibility |
| Blockchain systems | Transaction parsing, Merkle proofs, graph analysis, contract tests | Signing authority, finality assumptions, off-chain governance, and reversal limits |
| Recommendation systems | Feature pipelines, candidate retrieval, ranking, evaluation | Permitted inputs, objective, fairness, explanation, and user control |
| Online food delivery | Route graphs, order queues, dispatch heaps, ETA models | Order and payment authority, worker custody, retry safety, refunds, and recovery |

The lesson is not that AI removes architecture work. It moves practitioners up
a level: generated machinery arrives sooner, so meaning, authority, failure,
and evidence must become explicit sooner.

> **Why we did not choose every structure**
>
> Autocomplete systems help predict partial search terms, but they are not
> needed for core inventory and order work. Huffman coding compresses data, but
> it does not solve ranking, routing, delegated authority, abstention, budgets,
> or reversal. Choose a structure because the problem requires it.
