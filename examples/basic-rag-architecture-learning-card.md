# Basic RAG Architecture Learning Card

**Status:** Provider example verified 2026-09-01; architecture exercise
`PLANNED/UNRUN`

## The operational problem

An AI assistant must answer from an approved document collection without
treating model memory, an irrelevant search hit, or an old file as sufficient
evidence. If the assistant cannot retrieve fit evidence, it must say so rather
than fill the gap with a plausible answer.

## Plain-language analogy

A vector store is like a fast library catalog. It can point toward passages
that resemble the question. The catalog does not decide who may read a record,
whether the edition is current, whether the passage governs this situation, or
whether anyone may act on the answer.

## Technical structure

```text
INGEST
approved source -> upload -> searchable collection -> chunk/embed -> ready index

ANSWER
question -> tenant/purpose filter -> retrieve -> assemble context
         -> generate with source evidence -> answer or abstain

ACT
proposed action -> identity + authority + policy + budget + approval gate
                -> act, hold, or refuse -> durable evidence
```

The provider-neutral steps are:

1. Accept a source only through an owned ingestion boundary.
2. record its identity, version, authority scope, classification, effective
   time, tenant, purpose, and correction owner;
3. chunk and embed it into a versioned searchable collection;
4. wait until processing succeeds before making the collection eligible;
5. retrieve with tenant, purpose, source, and time filters;
6. assemble bounded context and instruct the model to answer from supplied
   evidence, cite it, and abstain when support is missing;
7. record the query, index version, returned items, answer, and actual-use
   evidence; and
8. send any consequential action through a separate governed capability.

## OpenAI implementation mapping

As verified in the official OpenAI documentation on 2026-09-01, one basic
managed path is:

1. upload a file for retrieval or `file_search` ingestion;
2. create a vector store and attach the uploaded file, then wait for processing
   status to become complete; and
3. create a model response with the `file_search` tool restricted to the
   intended vector-store identifier.

The managed service can perform file processing, search, context augmentation,
and response generation. The architect still owns source admission, metadata,
tenant and purpose isolation, freshness, deletion and correction, evaluation,
abstention, retention, evidence, cost limits, and action authority.

Official references, recheck before implementation:

- [Upload file](https://developers.openai.com/api/reference/typescript/resources/files/methods/create)
- [Attach a file to a vector store](https://developers.openai.com/api/reference/cli/resources/vector_stores/subresources/files/methods/create)
- [Create a response with file search](https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create)

## What goes wrong

| Failure | Consequence | Required response |
| --- | --- | --- |
| Cross-tenant or overbroad retrieval | One user's material influences another user's answer | Enforce tenant and purpose filters outside the model; refuse ambiguous scope |
| Stale or superseded source remains eligible | A fluent answer repeats an obsolete rule | Version sources and indexes; invalidate descendants and affected work |
| Relevance score is treated as truth | The highest-ranked passage becomes false authority | Record what the score means; verify source authority and effective time |
| Retrieved text is treated as instruction | Poisoned content redirects reasoning, tools, or egress | Classify retrieved text as untrusted data; enforce tool and egress policy separately |
| No evidence or abstention path | The model fills retrieval gaps with plausible language | Require source evidence, unsupported-claim tests, and an explicit no-answer state |
| Retrieval success authorizes action | An answer triggers a refund, shipment, or disclosure without delegation | Put identity, authority, approval, policy, budget, and reversal gates at the action boundary |

## Transfer artifact

| Decision | Your system |
| --- | --- |
| Recognizable user question and consequence | |
| Corpus owner and authoritative questions | |
| Admitted source types, versions, classifications, tenants, and purposes | |
| Chunking, embedding, index version, and readiness rule | |
| Retrieval query, filters, ranking meaning, and maximum evidence | |
| Citation, unsupported-claim, conflict, and abstention behavior | |
| Correction, deletion, reindexing, and in-flight revalidation path | |
| Prompt, model, retriever, and corpus evaluation set | |
| Cost, latency, retention, and exposure budgets | |
| Actions withheld from the answer path | |
| Separate action authority, approval, evidence, and reversal owner | |

## AI amplification

AI tools can quickly generate ingestion code, SDK calls, chunking experiments,
evaluation questions, retrieval tests, diagrams, and candidate prompts. They
cannot decide which source governs a business question, whose data may enter
the corpus, what a ranking score permits, when the system must abstain, or who
is accountable for an external action. Generated RAG machinery accelerates the
need for those decisions; it does not replace them.

This card is a design exercise, not evidence that a RAG system was executed,
secured, evaluated, or approved for production.
