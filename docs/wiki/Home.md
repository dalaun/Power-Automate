# Trust Domain Ontology

**Version 4.0** | [View Ontology File](https://github.com/dalaun/Finch-Dagen-Foundation/blob/claude/owl-ontology-trust-domain-2FLJj/trust-domain-ontology.ttl) | [Estate Planning Extension](https://github.com/dalaun/Finch-Dagen-Foundation/blob/claude/owl-ontology-trust-domain-2FLJj/trust-domain-estate-planning.ttl)

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

### 4. **Temporal Dimension** (v4.0)

All operations occur in time:

- **Fiscal Years**: 12-month accounting periods for DNI computation
- **Temporal Tracking**: Expenditures linked to quarters, months
- **Distribution Requirements**: IRC §4942 minimum distributions tracked annually
- **Compliance Queries**: Time-series analysis of qualifying distributions

### 5. **Grantmaking** (v4.0)

Grantmaking is modeled as **distinct from operations**:

- **GrantmakingActivity**: Separate authorized activity class
- **Grants to Public Charities**: Count as qualifying distributions
- **Program-Related Investments (PRIs)**: Grants for charitable purpose
- **Expenditure Responsibility**: Required for non-exempt grantees

### 6. **IRC §§4941-4945 Safeguards** (v4.0)

Fully axiomatized private foundation rules:

- **§4941 Self-Dealing**: Transactions with disqualified persons prohibited
- **§4942 Distributions**: Minimum distribution requirements enforced
- **§4943 Excess Holdings**: Business ownership limits (>20% triggers violation)
- **§4944 Jeopardizing Investments**: Investments endangering mission prohibited
- **§4945 Taxable Expenditures**: Lobbying, political, irresponsible grants prohibited

All violations are subclasses of `AuthorityCollapse` with disjoint classes preventing violations.

## Extensions

### Estate Planning Extension (v3.0) 🆕 DUAL-ONTOLOGY ARCHITECTURE

**[Estate Planning Extension](Estate-Planning-Extension.md)** - **Dual-layer ontology** separating semantic commitments from authority commitments

The base ontology focuses on **private foundations** (IRC §§4941-4945, grantmaking, temporal compliance). The estate planning extension (v3.0) implements a **clean architectural separation**:

#### v3.0 Dual-Ontology Architecture:
- **📚 Vocabulary Layer** (trust-domain-vocabulary.ttl): Defines what things MEAN - 1,628 triples
  - All class/property definitions, taxonomy, labels, domain/range, inverse properties
  - Use for: Data modeling, interoperability, shared semantics WITHOUT enforcement

- **⚖️ Compliance Layer** (trust-domain-compliance.ttl): Enforces what is ALLOWED - 263 triples
  - Disjointness, cardinality, state machine, outcome determination rules
  - Use for: Legal compliance, tax outcomes, automated reasoning

- **Design Principle**: "Meaning can tolerate ambiguity. Authority cannot."
  - Every axiom categorized: semantic (understanding) vs authority (enforcement)
  - Vocabulary + Compliance = Complete system (1,891 triples)

#### v2.0 Closed System Features:
- **🔄 Trust State Machine**: 6 lifecycle states (Created → Funded → Active → Irrevocable → Terminated)
- **⚖️ Outcome Determination**: Automatic inference of IRC §4941 self-dealing, validity outcomes, recognition
- **🔒 Complete Disjointness**: Transaction space partitioned (Relationship × Pricing = 2D classification)
- **🎯 Closure Axioms**: Every trust MUST be in exactly one state, every transaction classified
- **🤖 Automated Reasoning**: OWL reasoner determines legal consequences from trust configurations

#### Traditional Features (v1.0-1.2):
- **Participant roles** with disjointness: Grantor, Settlor, Trustee variants, Income/Remainder Beneficiaries
- **Document hierarchy**: Trust Indentures, Deeds, Amendments, Restatements
- **Property tenure**: Fee Simple, Life Estate, Remainder, Joint Tenancy
- **Legal actions** (all disjoint): Trust Contests, Reformation, Accounting Proceedings
- **Common law doctrines**: Rule Against Perpetuities, Cy Pres, Spendthrift Clauses, Arm's Length
- **Hague Trusts Convention**: Two-step validity model, choice of law, mandatory rules
- **160+ properties** with inverse relationships and cardinality constraints

**Key Innovation (v3.0)**: Clean separation enables vocabulary reuse without enforcement burden, while compliance layer adds authority when needed.

**Key Innovation (v2.0)**: Given transaction between grantor and trust at below-market price, reasoner **automatically infers** IRC §4941 self-dealing tax liability.

Use **vocabulary alone** for data modeling, **compliance** for enforcement, or **together** for complete system.

## Quick Start

1. **[Architecture Overview](Architecture.md)** - Understand the control-plane framework
2. **[Keystone Constraint](Keystone-Constraint.md)** - The fundamental rule governing private enablement
3. **[Authority Cascade](Authority-Cascade.md)** - How every dollar traces back to mission
4. **[Examples](Examples.md)** - See concrete instances of permissible vs improper enablement
5. **[Usage Guide](Usage-Guide.md)** - Query the ontology and validate compliance
6. **[Estate Planning Extension](Estate-Planning-Extension.md)** - Traditional trust vocabulary (optional)

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
