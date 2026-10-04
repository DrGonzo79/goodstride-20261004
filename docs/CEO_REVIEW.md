# CEO Review

**Mode:** Scope reduction. A two-sided all-marathon marketplace is premature; ship the smallest trust-bearing vertical slice.

## Nuclear challenge and alternatives

The actual outcome is a legitimate charity entry with a consciously accepted obligation, not a searchable directory. The minimal concierge board (S/low risk) beats a self-serve marketplace (M/high cold-start risk) and organizer inventory network (XL/high partnership risk). Recommendation: prove verified introductions for one race, while keeping the data model compatible with integrations.

`manual charity outreach → verified NYC board → runner fit + pledge plan → direct handoff → measured placement` is the path to the 12-month ideal of authoritative, multi-race inventory and fundraising workflows.

## Review sections

1. **Architecture:** Static demo and source-only API boundaries are honest. Production needs durable inventory events, identity, and correction workflows before taking payment.
2. **Error/rescue map:** Named cases are invalid budget (422), unknown place (404), overfunded progress (422), empty results (200), stale record (visible freshness warning), and inventory dependency failure (`503 inventory_unavailable`, deferred). No silent fallback to “available.”
3. **Security/threat model:** Main threats are fake charities, malicious links, tampered minimums, scraping, and PII leakage. Require charity verification, scoped editors, allowlisted links, audit logs, and minimal runner data.
4. **Data/interaction edge cases:** Nil filters broaden; empty search shows recovery; long names wrap; double-click is disabled during simulated matching; back navigation loses only demo state; zero/negative/over-limit inputs are rejected; stale availability must never look current.
5. **Code quality:** Deterministic rules are testable and model-free. Shared fixture intent is explicit, though production must generate typed contracts from the API rather than duplicate schemas.
6. **Tests:** Python covers success, empty, invalid, 404, and overfunded paths. Playwright covers filter, save, plan, invalid input, empty state, and mobile overflow. Missing until production: auth, persistence, race/charity imports, and link safety integration tests.
7. **Observability:** Track freshness SLA, corrections, API errors, searches with no results, contact conversion, and filled-place confirmation. Runbook: hide disputed inventory first, investigate source second.
8. **Database/state:** Use normalized race/charity/place records plus append-only inventory events. Enforce nonnegative quantity/minimum, unique active charity-race offer, and indexed `(race_id,status,deadline)`.
9. **API contract:** Explicit request bounds and empty semantics are good. Before external use add versioning, stable error codes, pagination, ETags, and rate limits.
10. **Performance/scalability:** Fixture filtering is trivial. At 100x, cache race queries and precompute availability; freshness ingestion and partner rate limits—not reads—become the bottleneck.
11. **Design/UX:** Hierarchy starts with commitment fit, not promotion. Loading/error/empty states and focus rings exist. Production must add comparison, source timestamps per listing, correction reporting, and a no-JS fallback.

## Decisions

- **Accepted:** one-race-first marketplace wedge, transparent pledge planner, verified freshness as core promise.
- **Deferred:** payments, AI copy generation, live availability, charity auth, organizer integrations, runner accounts.
- **Not in scope:** bib resale, guaranteed entry claims, automated eligibility decisions, paid hosting, handling donations.
- **Strongest challenges:** no direct demand proof; stale inventory can destroy trust; $75–$150 placement alone has weak ceiling.
- **Recommended next move:** manually validate supply and observe runner searches before building self-service.
