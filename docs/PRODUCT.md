# Product plan

## ICP and JTBD

**Primary ICP:** rejected major-marathon applicants with a fixed target race, credible fundraising capacity, and a deadline. **Supply ICP:** small-to-mid-sized charity event managers with allocations to fill. **JTBD:** “When the lottery rejects me, help me find a legitimate charity place whose cause and commitment fit, so I can act before inventory disappears.”

## MVP

Verified NYC inventory, race/cause/minimum/deadline filters, save/compare, fundraising pressure test, direct charity handoff, freshness timestamp, correction path. This demo ships filtering, saving, empty/error/loading states, and pledge arithmetic against shared fixtures.

## Data model

`Race(id, name, date)`; `Charity(id, legal_name, cause, contact)`; `Place(id, race_id, charity_id, minimum, deadline, quantity, status, verified_at)`; `RunnerIntent(id, race, causes, budget, timeline)`; `Introduction(id, runner_id, place_id, status, attribution)`; `InventoryEvent(place_id, old_status, new_status, source, at)`.

## Architecture and AI strategy

Next.js static frontend for discovery; FastAPI matching service for validated filtering/ranking; Postgres plus append-only inventory events in production; scheduled freshness checks and charity self-service links. No model is needed for core matching. Later, a constrained model may summarize approved charity materials or draft donor outreach, always labeled and never deciding eligibility.

## Economics

Start free to charities to seed inventory. Test $75–$150 qualified placement packages only after proving attribution, or $19 runner concierge support with a refund when no verified match exists. At $100 per filled place, 1,000 annual placements yields $100k—too small alone; attractive economics require fundraising tools, renewal, and organizer workflows. Avoid charging both sides opaquely.

## Validation and moat

North-star: verified introduction-to-accepted-place conversion. Leading metrics: active verified listings, age of inventory, search-to-contact, charity response time, runner completion. Kill if fewer than 20% of contacted charities share inventory or fewer than 10% of qualified runners request an introduction. Moat is not SEO; it is trusted freshness, placement outcomes, integration history, and fundraising performance data.

## Risks

Stale availability, race trademark confusion, charity legitimacy, misleading “guaranteed” language, refunds/chargebacks, cold start, discriminatory eligibility handling, and seasonality. Never sell or imply ownership of bibs; charities and race organizers remain authoritative.

## 30/60/90

- **30 days:** one race, 20 charities, concierge verification, 10 observed runner sessions.
- **60 days:** self-service updates, freshness SLA, introduction tracking, first willingness-to-pay test.
- **90 days:** second race only if NYC conversion clears the threshold; pilot fundraising cockpit and charity renewal.
