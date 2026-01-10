# Trust Domain Ontology

**Version 3.0** | [View Ontology File](../../trust-domain-ontology.ttl)

## Overview

The Trust Domain Ontology is a formal OWL 2 DL ontology that models private & foreign irrevocable non-grantor trusts as **systems of authority** rather than tax structures. It treats IRC sections not as "tax rules" but as **recognized instruments, authority boundaries, evidence schemas, and control-plane components**.

## Mission

**"Empowering lives through health, education, innovation, and opportunity"**

This ontology formalizes how this mission statement becomes the authorizing document that legitimizes every operational instrument and expenditure.

## Core Innovation

Traditional approach: "Is this expense deductible?"

**This ontology asks**: "Can you trace this spend back to mission through authorized activities?"

## Key Concepts

### 1. **The Control-Plane Architecture**

The ontology models the doctrinal stack that transforms trusts into autonomous systems:

```
IRC §§671-679  →  THE GATEWAY (control-of-income boundary)
IRC §§641-685  →  THE OPERATING SYSTEM (autonomous accounting)
IRC §7701      →  THE JURISDICTION (domestic vs foreign)
IRC §162/§212/§67(e) → THE EXPENSE INSTRUMENTS
```

### 2. **The Keystone Constraint**

> **Private enablement is permissible when and only when it is BOTH:**
> 1. **Incidental to** purpose-driven execution (not the primary purpose), AND
> 2. **Inseparable from** purpose-driven execution (necessarily coupled with mission)

This is the formal boundary between legitimate operations and private inurement.

### 3. **The Authority Cascade**

Every dollar spent must trace through this chain:

```
Mission
  ↓ legitimizes
Authority
  ↓ has purpose
Purpose Domains
  ↓ authorize
Authorized Activities
  ↓ require
Operators in Role
  ↓ necessitate
Expense Domains
  ↓ manifest as
Actual Spend
  ↓ traces back to
Purpose ✓
```

**If the cascade completes, spend is permissible. If it breaks, it's private inurement.**

## Quick Start

1. **[Architecture Overview](Architecture.md)** - Understand the control-plane framework
2. **[Keystone Constraint](Keystone-Constraint.md)** - The fundamental rule governing private enablement
3. **[Authority Cascade](Authority-Cascade.md)** - How every dollar traces back to mission
4. **[Examples](Examples.md)** - See concrete instances of permissible vs improper enablement
5. **[Usage Guide](Usage-Guide.md)** - Query the ontology and validate compliance

## What This Enables

### Automated Compliance
```sparql
# Find all spending that fails to trace back to purpose
SELECT ?spend WHERE {
  ?spend rdf:type :ActualSpend .
  FILTER NOT EXISTS { ?spend :tracesBackTo ?purpose }
}
```

### Audit Trail Generation
For any expenditure, query the complete chain from mission to spend and back.

### Real-Time Validation
Before approving spend, automated systems verify the authority cascade completes.

## Documentation

- **[Classes](Classes.md)** - All ontology classes
- **[Properties](Properties.md)** - Object and data properties
- **[Architecture](Architecture.md)** - The doctrinal framework
- **[Examples](Examples.md)** - Concrete individuals and use cases

## The Paradigm Shift

This ontology transforms tax compliance from a legal opinion into a **graph traversal problem**:

- IRS asks: "Is this private inurement?"
- Traditional answer: Hire lawyers, write memos, hope auditor agrees
- **This ontology**: Run a graph query. Does the path from spend to purpose exist?

If the path exists → permissible. If not → private inurement.

---

**This is tax compliance as a database query.**
