# Estate Planning Extension

[← Back to Home](Home.md)

## Overview

The **Trust Domain Estate Planning Extension** is a **closed, outcome-determining decision system** for trust legal compliance. Based on the Passbuckdefs legal glossary, this extension transforms the descriptive ontology into an executable decision framework following the principle:

> **"Define minimal classifications that determine outcomes, assign roles as non-overlapping constraint bundles, specify all admissible state transitions, and close the system such that from any valid state exactly one compliant outcome is reachable."**

### Key Features (v3.0) 🆕 DUAL-ONTOLOGY ARCHITECTURE

**Breaking Change**: The ontology now exists as **TWO separate files** instead of one, implementing clean separation of semantic commitments from authority commitments following the principle:

> **"Meaning can tolerate ambiguity. Authority cannot."**

**Architecture**:
- **trust-domain-vocabulary.ttl** (1,628 triples) - **SEMANTIC LAYER** - Defines what things MEAN
- **trust-domain-compliance.ttl** (263 triples) - **AUTHORITY LAYER** - Enforces what is ALLOWED

**Design Principle**: Every axiom passes this litmus test:
- *"If I remove this rule, do I lose understanding?"* → VOCABULARY (semantic)
- *"If I remove this rule, do I lose authority?"* → COMPLIANCE (operational)

**Benefits**:
- ✅ Clear distinction between what exists and what is allowed
- ✅ Vocabulary can be used for data modeling without enforcement
- ✅ Compliance adds authority layer when needed
- ✅ No conflation of meaning rules with enforcement rules
- ✅ Audit trail: every rule is explicitly categorized

### Previous Features (v2.0)

- **🔒 Complete Disjointness** - All major class hierarchies partitioned (transactions, roles, documents, legal actions)
- **🔄 Trust State Machine** - 6 lifecycle states with admissible transitions and triggers
- **⚖️ Outcome Determination** - Automatic inference of legal consequences (IRC §4941, validity, recognition)
- **🎯 Closure Axioms** - Every entity must be completely classified
- **🤖 Automated Reasoning** - OWL reasoner determines compliance outcomes from trust configurations

### Traditional Features (v1.0-1.2)

- **Participant roles** (Grantor, Settlor, Trustee, Beneficiary variants) with disjointness constraints
- **Document hierarchy** (Trust Indentures, Deeds, Amendments) - mutually exclusive types
- **Property tenure** (Fee Simple, Life Estate, Remainder)
- **Legal actions** (Trust Contests, Reformation, Accounting) - all disjoint
- **Common law doctrines** (Rule Against Perpetuities, Cy Pres, Spendthrift Clauses)
- **Arm's length transaction framework** (Related Party vs Arms Length with outcome determination)
- **Hague Trusts Convention** (Two-step validity model, choice of law, mandatory rules)
- **Comprehensive relationships** with inverse properties
- **Cardinality constraints** ensuring ontological integrity

## File Structure (v3.0)

```
trust-domain-ontology.ttl          # Base ontology (v4.0)
trust-domain-vocabulary.ttl        # Semantic layer (v3.0) - what things MEAN
trust-domain-compliance.ttl        # Authority layer (v3.0) - what is ALLOWED
trust-domain-estate-planning.ttl   # Original (v2.0) - superseded but retained for compatibility
extract_semantic.py                 # Tool to extract semantic commitments
extract_authority.py                # Tool to extract authority commitments
validate_separated.py               # Tool to validate dual-ontology separation
validate_ontology.py                # Original validation tool
```

The vocabulary ontology **imports** the base ontology, and the compliance ontology **imports** the vocabulary:

```turtle
# Vocabulary (semantic layer)
<http://example.org/trust-domain/estate-planning/vocabulary> rdf:type owl:Ontology ;
    owl:imports <http://example.org/trust-domain> ;
    owl:versionInfo "3.0" .

# Compliance (authority layer)
<http://example.org/trust-domain/estate-planning/compliance> rdf:type owl:Ontology ;
    owl:imports <http://example.org/trust-domain/estate-planning/vocabulary> ;
    owl:versionInfo "3.0" .
```

---

## 🆕 Dual-Ontology Architecture (v3.0)

### The Separation Principle

The v3.0 architecture separates the ontology into two distinct layers based on a fundamental insight:

> **"Meaning can tolerate ambiguity. Authority cannot."**

Every axiom in the original ontology was evaluated with this litmus test:
- **"If I remove this axiom, do I lose understanding?"** → Belongs in **VOCABULARY** (semantic layer)
- **"If I remove this axiom, do I lose authority?"** → Belongs in **COMPLIANCE** (operational layer)

This clean separation enables:
1. **Vocabulary** to define what concepts mean without enforcing rules
2. **Compliance** to add authority commitments on top of meaning
3. **Clear audit trail** of which axioms serve which purpose

### Vocabulary Ontology (Semantic Layer)

**File**: `trust-domain-vocabulary.ttl`
**Triples**: 1,628 (86.1% of total)
**Purpose**: Define what things MEAN in the trust and estate planning domain

**Contains**:
- ✅ All 131 class definitions (no disjointness)
- ✅ All 160 property definitions (no functional declarations)
- ✅ Taxonomy (rdfs:subClassOf)
- ✅ Domain/range declarations
- ✅ Inverse properties
- ✅ Labels, comments, glossary mappings
- ✅ Property chains (compositional meaning)
- ✅ State definitions (what states mean, not transitions)

**Does NOT contain**:
- ❌ Cardinality constraints
- ❌ Disjointness axioms
- ❌ Functional property declarations
- ❌ State machine transitions
- ❌ Outcome determination rules
- ❌ Closure axioms

**Validation**: ✓ Clean (0 functional properties, 0 disjointness axioms)

**Use Case**: Load vocabulary alone for:
- **Interoperability** across systems
- **Data exchange** without enforcement
- **Understanding** the domain model
- **Shared semantics** without operational constraints

### Compliance Ontology (Authority Layer)

**File**: `trust-domain-compliance.ttl`
**Triples**: 263 (13.9% of total)
**Purpose**: Enforce WHAT IS ALLOWED and determine outcomes

**Imports**: `trust-domain-vocabulary.ttl` (gets all semantic commitments)

**Contains**:
- ✅ 14 functional property declarations
- ✅ 39 disjointness axioms
- ✅ 15 cardinality constraints
- ✅ State machine transitions (canTransitionTo)
- ✅ State enumeration (oneOf - closed world)
- ✅ Outcome determination (equivalentClass with intersection/union)
- ✅ Closure axioms (forcing classification)

**Does NOT contain**:
- ❌ Class definitions (imported from vocabulary)
- ❌ Property definitions (imported from vocabulary)
- ❌ Labels, comments (imported from vocabulary)

**Validation**: ✓ Contains authority axioms as expected

**Use Case**: Load compliance for:
- **Legal compliance** checking
- **Tax determination** (IRC §4941 self-dealing)
- **Outcome inference** via OWL reasoner
- **Enforcement** of what is permissible

### Separation Statistics

| Layer | Triples | Percentage | Purpose |
|-------|---------|------------|---------|
| **Vocabulary** | 1,628 | 86.1% | What things MEAN |
| **Compliance** | 263 | 13.9% | What is ALLOWED |
| **Combined** | 1,891 | 100% | Complete system |
| **Original** | 1,887 | - | v2.0 monolithic |
| **Difference** | +4 | - | Metadata only |

### Examples of Separation

#### Example 1: Trust State (Vocabulary vs Compliance)

**Vocabulary Layer** (what states MEAN):
```turtle
ep:TrustCreated a owl:NamedIndividual ;
    rdfs:label "Trust Created"@en ;
    rdfs:comment "Trust instrument executed but not yet funded"@en ;
    rdf:type ep:TrustState .

ep:TrustFunded a owl:NamedIndividual ;
    rdfs:label "Trust Funded"@en ;
    rdfs:comment "Assets transferred to trustee"@en ;
    rdf:type ep:TrustState .
```

**Compliance Layer** (what transitions are ALLOWED):
```turtle
# State enumeration (closed world - exactly these 6 states, no others)
ep:TrustState owl:equivalentClass
    [ owl:oneOf ( ep:TrustCreated ep:TrustFunded ep:TrustActive
                  ep:TrustIrrevocable ep:TrustRevoked ep:TrustTerminated ) ] .

# Admissible transitions
ep:TrustCreated ep:canTransitionTo ep:TrustFunded, ep:TrustRevoked, ep:TrustTerminated .
ep:TrustFunded ep:canTransitionTo ep:TrustActive, ep:TrustRevoked, ep:TrustTerminated .

# Functional constraint (exactly ONE state at a time)
:TrustEntity rdfs:subClassOf
    [ owl:onProperty ep:hasState ;
      owl:cardinality "1"^^xsd:nonNegativeInteger ] .
```

#### Example 2: Transaction Classification (Vocabulary vs Compliance)

**Vocabulary Layer** (what transaction types MEAN):
```turtle
ep:ArmsLengthTransaction a owl:Class ;
    rdfs:label "Arm's Length Transaction"@en ;
    rdfs:comment "Transaction between unrelated parties dealing at arm's length"@en ;
    rdfs:subClassOf ep:Transaction .

ep:RelatedPartyTransaction a owl:Class ;
    rdfs:label "Related Party Transaction"@en ;
    rdfs:comment "Transaction involving related parties or conflicts of interest"@en ;
    rdfs:subClassOf ep:Transaction .

ep:BelowMarketTransaction a owl:Class ;
    rdfs:label "Below Market Transaction"@en ;
    rdfs:comment "Transaction at less than fair market value"@en ;
    rdfs:subClassOf ep:Transaction .
```

**Compliance Layer** (what classifications are REQUIRED):
```turtle
# Mutual exclusion (cannot be both arms-length AND related party)
ep:ArmsLengthTransaction owl:disjointWith ep:RelatedPartyTransaction .

# Pricing partition
ep:FairValueTransaction owl:disjointWith ep:BelowMarketTransaction, ep:AboveMarketTransaction .
ep:AboveMarketTransaction owl:disjointWith ep:BelowMarketTransaction .

# Closure axiom (MUST be classified on relationship dimension)
ep:Transaction rdfs:subClassOf
    [ owl:unionOf ( ep:ArmsLengthTransaction ep:RelatedPartyTransaction ) ] .

# Closure axiom (MUST be classified on pricing dimension)
ep:Transaction rdfs:subClassOf
    [ owl:unionOf ( ep:FairValueTransaction ep:BelowMarketTransaction ep:AboveMarketTransaction ) ] .

# Outcome determination (automatic IRC §4941 inference)
ep:PotentialSelfDealingTransaction owl:equivalentClass
    [ owl:intersectionOf ( ep:RelatedPartyTransaction ep:BelowMarketTransaction ) ] .
```

#### Example 3: Properties (Vocabulary vs Compliance)

**Vocabulary Layer** (what the property MEANS):
```turtle
ep:governedBy a owl:ObjectProperty ;
    rdfs:label "governed by"@en ;
    rdfs:comment "Trust is governed by this document"@en ;
    rdfs:domain :TrustEntity ;
    rdfs:range ep:Document ;
    owl:inverseOf ep:governs .
```

**Compliance Layer** (authority constraint):
```turtle
# Functional property (trust can have ONLY ONE governing document)
ep:governedBy a owl:FunctionalProperty .
```

### Usage Patterns

#### Pattern 1: Load Vocabulary Only (Interoperability)

```python
from rdflib import Graph

# For shared semantics without enforcement
g = Graph()
g.parse("trust-domain-vocabulary.ttl", format="turtle")

# Can model trusts, transactions, participants
# WITHOUT triggering disjointness violations
# Useful for data exchange between systems
```

#### Pattern 2: Load Compliance (Full Enforcement)

```python
from rdflib import Graph

# For legal compliance and outcome determination
g = Graph()
g.parse("trust-domain-compliance.ttl", format="turtle")
# Automatically imports vocabulary.ttl

# OWL reasoner will:
# - Detect inconsistencies (functional property violations)
# - Infer outcomes (IRC §4941 self-dealing)
# - Enforce state machine transitions
```

#### Pattern 3: Incremental Migration

```python
# Start with vocabulary for data modeling
import_vocabulary()

# Add compliance layer when ready for enforcement
if ready_for_compliance:
    import_compliance()
```

### Automation Tools

#### extract_semantic.py

Extracts semantic commitments from original ontology:

```python
python extract_semantic.py
# Creates: trust-domain-vocabulary.ttl
# Includes: Classes, properties, taxonomy, labels, comments
# Excludes: Cardinality, disjointness, functional declarations
```

#### extract_authority.py

Extracts authority commitments from original ontology:

```python
python extract_authority.py
# Creates: trust-domain-compliance.ttl
# Includes: Disjointness, cardinality, state machine, outcome rules
# Excludes: Class/property definitions (imported from vocabulary)
```

#### validate_separated.py

Validates the dual-ontology separation:

```python
python validate_separated.py
# Checks:
# ✓ Vocabulary has no functional properties
# ✓ Vocabulary has no disjointness axioms
# ✓ Compliance contains authority axioms
# ✓ Combined triple count matches original
# ✓ No semantic commitments lost
```

### Migration Guide

**From v2.0 (monolithic) to v3.0 (dual-ontology)**:

1. **For data modeling only**:
   ```python
   # Old (v2.0)
   import trust_domain_estate_planning

   # New (v3.0)
   import trust_domain_vocabulary  # Semantic layer only
   ```

2. **For compliance checking**:
   ```python
   # Old (v2.0)
   import trust_domain_estate_planning

   # New (v3.0)
   import trust_domain_compliance  # Imports vocabulary automatically
   ```

3. **Compatibility mode**:
   ```python
   # v2.0 file remains for backward compatibility
   import trust_domain_estate_planning  # Still works (superseded)
   ```

### Benefits of Dual-Ontology Architecture

| Benefit | Description |
|---------|-------------|
| **Clarity** | Every axiom explicitly categorized: semantic or authority |
| **Modularity** | Use vocabulary without enforcement burden |
| **Flexibility** | Add/remove authority layer as needed |
| **Auditability** | Clear separation makes governance easier |
| **Interoperability** | Vocabulary layer sharable across systems |
| **Evolution** | Semantic and authority layers can evolve independently |

---

## 🆕 Closed System Architecture (v2.0)

### Trust State Machine

Every trust exists in **exactly one state** at any time (enforced via `owl:FunctionalProperty`):

```
┌─────────────┐
│   Created   │ ─── Instrument executed, not funded
└──────┬──────┘
       │ InitialFundingEvent
       ↓
┌─────────────┐
│   Funded    │ ─── Assets transferred to trustee
└──────┬──────┘
       │ ValidityConfirmation
       ↓
┌─────────────┐
│   Active    │ ─── Operating with all validity conditions satisfied
└──────┬──────┘
       │ IrrevocabilityEvent (GrantorDeath | IrrevocableByTerms | ExplicitIrrevocability)
       ↓
┌──────────────┐
│ Irrevocable  │ ─── Cannot be revoked, only terminated
└──────┬───────┘
       │ TerminationEvent
       ↓
┌──────────────┐
│ Terminated   │ ─── Terminal state (merger, RAP, final distribution)
└──────────────┘

Alternative paths:
  Any state → Revoked (if revocable)
  Any state → Terminated (various triggers)
```

**Admissible Transitions** (defined via `canTransitionTo`):

```turtle
ep:TrustCreated ep:canTransitionTo ep:TrustFunded, ep:TrustRevoked, ep:TrustTerminated .
ep:TrustFunded ep:canTransitionTo ep:TrustActive, ep:TrustRevoked, ep:TrustTerminated .
ep:TrustActive ep:canTransitionTo ep:TrustIrrevocable, ep:TrustRevoked, ep:TrustTerminated .
ep:TrustIrrevocable ep:canTransitionTo ep:TrustTerminated .
```

**Termination Triggers**:
- `MergerEvent` - Legal and equitable title merge (Merger Doctrine)
- `PurposeFulfilled` - Trust purpose accomplished
- `RAPViolation` - Rule Against Perpetuities violation
- `FinalDistribution` - All corpus distributed to remaindermen

### Outcome Determination

The system automatically infers **legal consequences** based on trust state and classifications:

#### Tax Consequences

```turtle
# AUTOMATIC INFERENCE:
# IF transaction is RelatedPartyTransaction AND BelowMarketTransaction
# THEN transaction is PotentialSelfDealingTransaction
# THEN transaction hasOutcome IRC4941ExciseTax

ep:PotentialSelfDealingTransaction owl:equivalentClass
    [ owl:intersectionOf (ep:RelatedPartyTransaction ep:BelowMarketTransaction) ] .

ep:PotentialSelfDealingTransaction rdfs:subClassOf
    [ owl:onProperty ep:hasOutcome ;
      owl:someValuesFrom ep:IRC4941ExciseTax ] .
```

**Tax Outcome Classes**:
- `IRC4941ExciseTax` - Self-dealing excise tax (10% initial, 200% additional)
- `IRC4945TaxableExpenditure` - Prohibited expenditure tax (20% initial, 100% additional)
- `ExcessBenefitTransaction` - IRC §4958 excess benefit (supporting organizations)
- `GrantorTrustStatus` ⊥ `NonGrantorTrustStatus` - Income tax classification (disjoint)

#### Validity Outcomes (Hague Two-Step Model)

```turtle
# Step One: Trust Validity (TrustValid ⊥ TrustInvalid)
# Step Two: Asset Transfer Validity (TransferValid ⊥ TransferInvalid)

# CRITICAL: These are INDEPENDENT
# A trust can be TrustValid even if specific assets are TransferInvalid
# Models: "A trust can exist even if a particular transfer fails"

:TrustEntity rdfs:subClassOf
    [ owl:unionOf (
        [ owl:onProperty ep:hasOutcome ; owl:someValuesFrom ep:TrustValid ]
        [ owl:onProperty ep:hasOutcome ; owl:someValuesFrom ep:TrustInvalid ] ) ] .
```

**Validity Outcome Classes**:
- `TrustValid` ⊥ `TrustInvalid` - Step one of Hague two-step
- `TransferValid` ⊥ `TransferInvalid` - Step two (does NOT invalidate trust)

#### Recognition Outcomes

**Recognition Outcome Classes**:
- `TrustRecognized` ⊥ `TrustNotRecognized` - Hague Convention recognition

### Complete Disjointness Declarations

All major class hierarchies are **partitioned** to enable outcome determination:

#### Transaction Space Partitioning

```turtle
# Every transaction MUST be classified by TWO orthogonal dimensions:

# Dimension 1: Relationship
ArmsLengthTransaction ⊥ RelatedPartyTransaction

# Dimension 2: Pricing
FairValueTransaction ⊥ BelowMarketTransaction ⊥ AboveMarketTransaction

# Closure: Every transaction is classified on BOTH dimensions
ep:Transaction rdfs:subClassOf
    [ owl:unionOf (ep:ArmsLengthTransaction ep:RelatedPartyTransaction) ] .

ep:Transaction rdfs:subClassOf
    [ owl:unionOf (ep:FairValueTransaction ep:BelowMarketTransaction ep:AboveMarketTransaction) ] .
```

This 2D classification enables **automatic tax outcome determination**:
- `RelatedPartyTransaction ⊓ BelowMarketTransaction` → IRC §4941 self-dealing
- `RelatedPartyTransaction ⊓ AboveMarketTransaction` → IRC §4958 excess benefit

#### Participant Role Partitioning

```turtle
# Functional roles cannot overlap
Witness ⊥ Grantor, Settlor, Trustee, Beneficiary
NotaryPublic ⊥ Grantor, Settlor, Beneficiary
Judge ⊥ Grantor, Settlor, Trustee, Beneficiary, Attorney

# Estate planning vs inter vivos distinction
Testator ⊥ Grantor

# Beneficiary space partition
IncomeBeneficiary ⊥ RemainderBeneficiary
```

#### Document Type Partitioning

```turtle
TrustAgreement ⊥ Deed          # Trust documents vs property deeds
Will ⊥ TrustAgreement          # Testamentary vs inter vivos
```

#### Legal Action Partitioning

```turtle
# All legal action types are mutually exclusive
TrustContest ⊥ AccountingProceeding ⊥ Reformation ⊥ ConstructionProceeding ⊥ Partition
```

#### Hague Framework Partitioning

```turtle
# Two-step model separation
TrustValidity ⊥ AssetTransferValidity

# Mandatory rules OVERRIDE choice of law
MandatoryRule ⊥ ChoiceOfLaw
```

### Closure Axioms

The system ensures **every entity is completely classified**:

```turtle
# Every trust must be in exactly ONE state
:TrustEntity rdfs:subClassOf
    [ owl:onProperty ep:hasState ;
      owl:cardinality "1"^^xsd:nonNegativeInteger ] .

# Every cross-border trust must have validity outcome
ep:CrossBorderTrust rdfs:subClassOf
    [ owl:onProperty ep:hasOutcome ;
      owl:someValuesFrom ep:ValidityOutcome ] .

# Every cross-border trust must have recognition outcome
ep:CrossBorderTrust rdfs:subClassOf
    [ owl:onProperty ep:hasOutcome ;
      owl:someValuesFrom ep:RecognitionOutcome ] .

# Every trust must be valid or invalid
:TrustEntity rdfs:subClassOf
    [ owl:unionOf (
        [ owl:onProperty ep:hasOutcome ; owl:someValuesFrom ep:TrustValid ]
        [ owl:onProperty ep:hasOutcome ; owl:someValuesFrom ep:TrustInvalid ] ) ] .
```

### Automated Reasoning Examples

With an OWL reasoner (HermiT, Pellet, or ELK), the system provides:

#### 1. Automatic Tax Classification

```turtle
# INPUT (user provides):
:Transaction_2024_001 a ep:Transaction ;
    ep:transactionBy :JohnDoe_Grantor ;
    ep:transactionWith :FamilyTrust ;
    ep:transactionValue "100000.00"^^xsd:decimal ;
    ep:fairMarketValue "200000.00"^^xsd:decimal .

# REASONER INFERS:
:Transaction_2024_001 a ep:RelatedPartyTransaction .   # JohnDoe is related to his trust
:Transaction_2024_001 a ep:BelowMarketTransaction .    # $100k < $200k FMV
:Transaction_2024_001 a ep:PotentialSelfDealingTransaction .  # Intersection
:Transaction_2024_001 ep:hasOutcome :IRC4941_Tax_001 .
:IRC4941_Tax_001 a ep:IRC4941ExciseTax .
```

#### 2. Inconsistency Detection

```turtle
# INVALID INPUT:
:MyTrust ep:hasState ep:TrustCreated ;
         ep:hasState ep:TrustFunded .     # TWO states!

# REASONER DETECTS:
ERROR: Inconsistent ontology
Reason: ep:hasState is owl:FunctionalProperty (max cardinality = 1)
```

#### 3. State Reachability Analysis

```turtle
# INPUT:
:MyTrust ep:hasState ep:TrustIrrevocable .

# USER QUERY:
Can :MyTrust transition to ep:TrustRevoked?

# REASONER DETERMINES:
NO - ep:TrustIrrevocable has no canTransitionTo ep:TrustRevoked assertion
Only valid transition: ep:TrustIrrevocable → ep:TrustTerminated
```

#### 4. Hague Two-Step Independence

```turtle
# INPUT:
:CrossBorderTrust a ep:CrossBorderTrust ;
    ep:hasOutcome :Validity_001 .
:Validity_001 a ep:TrustValid .

:Asset_RealProperty ep:heldBy :CrossBorderTrust ;
    ep:hasOutcome :TransferValidity_001 .
:TransferValidity_001 a ep:TransferInvalid .  # Transfer failed!

# REASONER CONFIRMS:
CONSISTENT - Trust validity and transfer validity are independent
Trust remains valid even though property transfer failed (Hague two-step model)
```

#### 5. Mandatory Rule Override

```turtle
# INPUT:
:NevisTrust ep:choosesGoverningLaw :NevisLaw ;
            ep:subjectToMandatoryRule :FrenchForcedHeirship .

:FrenchForcedHeirship a ep:ForcedHeirship ;
    ep:legitimePortion "0.50"^^xsd:decimal .  # 50% reserved for heirs

# REASONER INFERS:
For questions within scope of ep:ForcedHeirship:
  → Mandatory rule applies (overrides :NevisLaw choice)
For other questions:
  → :NevisLaw applies
```

---

## Traditional Ontology Features (v1.0-1.2)

## Key Additions

### 1. Participant Role Taxonomy

Complete hierarchy of trust participants with specialized roles:

```
Participant
├── Grantor (creates trust)
├── Settlor (settles property into trust)
├── Trustee
│   ├── CoTrustee
│   └── SuccessorTrustee
├── Protector
├── Beneficiary
│   ├── IncomeBeneficiary
│   ├── RemainderBeneficiary
│   └── ContingentBeneficiary
├── Testator (executes will)
├── Heir (inherits via intestacy)
├── Witness
├── NotaryPublic
├── Attorney
└── Judge
```

### 2. Document & Instrument Hierarchy

Comprehensive legal document taxonomy:

```
Document
├── TrustIndenture
├── TrustAgreement
├── DeclarationOfTrust
├── TrustAmendment
├── Restatement
├── TerminationAgreement
├── Deed
│   ├── WarrantyDeed
│   └── QuitclaimDeed
├── BillOfSale
├── Mortgage
├── Petition
├── Complaint
└── Judgment
```

### 3. Property Tenure Forms

Traditional common law property interests:

```
PropertyTenure
├── FeeSimple (absolute ownership)
├── LifeEstate (duration of life)
├── Remainder (future interest)
├── Reversion (grantor's retained interest)
├── JointTenancy (with right of survivorship)
└── TenancyInCommon (co-ownership)
```

### 4. Legal Action Framework

Court proceedings affecting trusts:

```
LegalAction
├── TrustContest
├── AccountingProceeding
├── Reformation
├── ConstructionProceeding
└── Partition
```

## Relationship Properties

All properties include **inverse relationships** for bidirectional navigation.

### Trust-Centered Relationships

| Property | Domain | Range | Inverse | Functional |
|----------|--------|-------|---------|------------|
| **hasGrantor** | Trust | Grantor | creates | No |
| **hasSettlor** | Trust | Settlor | settles | No |
| **hasCoTrustee** | Trust | CoTrustee | servesAs | No |
| **hasSuccessorTrustee** | Trust | SuccessorTrustee | willServe | No |
| **hasIncomeBeneficiary** | Trust | IncomeBeneficiary | receivesIncomeFrom | No |
| **hasRemainderBeneficiary** | Trust | RemainderBeneficiary | receivesCorpusFrom | No |
| **governedBy** | Trust | Document | governs | **Yes** |
| **establishedBy** | Trust | Document | establishes | **Yes** |
| **amendedBy** | Trust | TrustAmendment | amends | No |
| **restatedBy** | Trust | Restatement | restates | **Yes** |
| **terminatedBy** | Trust | TerminationAgreement | terminates | **Yes** |
| **holdsCorpus** | Trust | Corpus | isCorpusOf | **Yes** |
| **operatesUnder** | Trust | Jurisdiction | jurisdictionOver | **Yes** |
| **hasSitus** | Trust | Situs | locationOf | **Yes** |
| **createsInterest** | Trust | BeneficialInterest | createdBy | No |

**Functional properties** (`owl:FunctionalProperty`) ensure trust can only have **one** of that relationship.

### Participant-Centered Relationships

| Property | Domain | Range | Inverse |
|----------|--------|-------|---------|
| **owns** | Participant | Asset | ownedBy |
| **transfers** | Participant | Asset | transferredBy |
| **receives** | Participant | Asset | receivedBy |
| **bequeaths** | Testator | Asset | bequeathedBy |
| **devises** | Testator | RealProperty | devisedBy |
| **inherits** | Heir | Asset | inheritedBy |
| **executes** | Participant | Document | executedBy |
| **witnesses** | Witness | Document | witnessedBy |
| **notarizes** | NotaryPublic | Document | notarizedBy |
| **owes** | Participant | FiduciaryDuty | owedBy |
| **boundBy** | Participant | LegalDoctrine | binds |
| **hasCapacity** | Participant | LegalCapacity | capacityOf |
| **holdsInterest** | Participant | BeneficialInterest | interestHeldBy |
| **initiates** | Participant | LegalAction | initiatedBy |
| **defends** | Participant | LegalAction | defendedBy |

### Asset-Centered Relationships

| Property | Domain | Range | Inverse |
|----------|--------|-------|---------|
| **evidencedBy** | Asset | Document | evidences |
| **conveyedBy** | Asset | Deed | conveys |
| **encumberedByDocument** | Asset | Document | encumbersAsset |
| **describedIn** | Asset | Document | describes |
| **characterizedAs** | Asset | PropertyType | characterizes |
| **heldAs** | Asset | PropertyTenure | formOfHolding |
| **valuedAt** | Asset | Valuation | valuationOf |
| **hasBasis** | Asset | TaxBasis | basisFor |

### Document-Centered Relationships

| Property | Domain | Range | Inverse |
|----------|--------|-------|---------|
| **benefitsParty** | Document | Participant | benefitsFrom |
| **embodies** | Document | LegalPrinciple | embodiedIn |
| **createsRight** | Document | LegalRight | rightCreatedBy |
| **filedIn** | Document | LegalAction | containsDocument |
| **exhibitIn** | Document | LegalAction | hasExhibit |

## Cardinality Constraints

OWL restrictions enforce ontological integrity:

```turtle
###  TRUST MUST have at least one Grantor
:TrustEntity rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:hasGrantor ;
      owl:minCardinality "1"^^xsd:nonNegativeInteger ] .

###  TRUST MUST have at least one Beneficiary
:TrustEntity rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty :hasBeneficiary ;
      owl:minCardinality "1"^^xsd:nonNegativeInteger ] .

###  TRUST can have at most one Protector
:TrustEntity rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty :hasProtector ;
      owl:maxCardinality "1"^^xsd:nonNegativeInteger ] .

###  TRUST established by exactly ONE document
:TrustEntity rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:establishedBy ;
      owl:cardinality "1"^^xsd:nonNegativeInteger ] .

###  TRUSTEE owes at least one Fiduciary Duty
ep:Trustee rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:owes ;
      owl:someValuesFrom ep:FiduciaryDuty ] .
```

## Property Chains

Complex legal patterns expressed through property chain axioms:

### Fiduciary Duty Pattern

```turtle
###  Trust → Trustee → Fiduciary Duty
ep:requiresFiduciaryDuty rdf:type owl:ObjectProperty ;
    owl:propertyChainAxiom ( :hasTrustee ep:owes ) ;
    rdfs:label "requires fiduciary duty"@en .
```

**Inference**: Trust indirectly requires fiduciary duty through trustee.

### Beneficial Interest Pattern

```turtle
###  Beneficiary → Interest → Trust → Corpus
ep:beneficialInterestInCorpus rdf:type owl:ObjectProperty ;
    owl:propertyChainAxiom ( ep:holdsInterest ep:createdBy ep:holdsCorpus ) ;
    rdfs:label "beneficial interest in corpus"@en .
```

**Inference**: Beneficiary's interest traces through trust to corpus.

## Example: Traditional Trust

```turtle
@prefix : <http://example.org/trust-domain#> .
@prefix ep: <http://example.org/trust-domain/estate-planning#> .

###  PARTICIPANTS
:JohnSmith rdf:type ep:Grantor ;
    rdfs:label "John Smith (Grantor)" .

:FidelityTrust rdf:type ep:Trustee ;
    rdfs:label "Fidelity Trust Company (Trustee)" .

:MarySmith rdf:type ep:IncomeBeneficiary ;
    rdfs:label "Mary Smith (Income Beneficiary)" .

:TomSmith rdf:type ep:RemainderBeneficiary ;
    rdfs:label "Tom Smith (Remainderman)" .

###  DOCUMENTS
:SmithTrustIndenture rdf:type ep:TrustIndenture ;
    ep:executedBy :JohnSmith ;
    ep:executionDate "2020-05-15"^^xsd:date ;
    rdfs:label "Smith Family Trust Indenture" .

:Amendment2023 rdf:type ep:TrustAmendment ;
    ep:amends :SmithFamilyTrust ;
    ep:executedBy :JohnSmith ;
    ep:amendmentDate "2023-08-10"^^xsd:date ;
    rdfs:label "First Amendment to Smith Family Trust" .

###  TRUST
:SmithFamilyTrust rdf:type :TrustEntity ;
    ep:hasGrantor :JohnSmith ;
    :hasTrustee :FidelityTrust ;
    ep:hasIncomeBeneficiary :MarySmith ;
    ep:hasRemainderBeneficiary :TomSmith ;
    ep:establishedBy :SmithTrustIndenture ;
    ep:governedBy :SmithTrustIndenture ;
    ep:amendedBy :Amendment2023 ;
    ep:trustDate "2020-05-15"^^xsd:date ;
    ep:operatesUnder :CaliforniaJurisdiction ;
    ep:hasSitus :CaliforniaSitus ;
    rdfs:label "Smith Family Irrevocable Trust" .

###  ASSETS
:FamilyHomeCorpus rdf:type ep:Corpus ;
    ep:isCorpusOf :SmithFamilyTrust ;
    ep:fairMarketValue "2500000.00"^^xsd:decimal ;
    rdfs:label "Family Home and Investment Portfolio (Trust Corpus)" .

:FamilyHome rdf:type ep:RealProperty ;
    ep:heldBy :SmithFamilyTrust ;
    ep:heldAs :LifeEstate ;  # Mary has life estate
    ep:conveyedBy :DeedToTrust ;
    ep:fairMarketValue "1800000.00"^^xsd:decimal ;
    rdfs:label "123 Main Street, Beverly Hills, CA" .

:DeedToTrust rdf:type ep:WarrantyDeed ;
    ep:conveys :FamilyHome ;
    ep:executedBy :JohnSmith ;
    ep:executionDate "2020-05-15"^^xsd:date ;
    rdfs:label "Warranty Deed conveying property to Smith Family Trust" .

###  LEGAL CONCEPTS
:CaliforniaJurisdiction rdf:type ep:Jurisdiction ;
    ep:jurisdictionOver :SmithFamilyTrust ;
    rdfs:label "State of California" .

:CaliforniaSitus rdf:type ep:Situs ;
    ep:locationOf :SmithFamilyTrust ;
    rdfs:label "California (Trust Situs)" .

:MaryLifeInterest rdf:type ep:BeneficialInterest ;
    ep:createdBy :SmithFamilyTrust ;
    ep:interestHeldBy :MarySmith ;
    rdfs:label "Mary's Life Estate Interest" .

:TomRemainderInterest rdf:type ep:BeneficialInterest ;
    ep:createdBy :SmithFamilyTrust ;
    ep:interestHeldBy :TomSmith ;
    rdfs:label "Tom's Remainder Interest" .

:FiduciaryDuty_Fidelity rdf:type ep:FiduciaryDuty ;
    ep:owedBy :FidelityTrust ;
    rdfs:label "Fidelity's Fiduciary Duty to Smith Family Trust" .
```

## SPARQL Queries

### Find All Trusts with Their Grantors and Trustees

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?trust ?grantor ?trustee WHERE {
  ?trust a :TrustEntity ;
         ep:hasGrantor ?grantor ;
         :hasTrustee ?trustee .
}
```

### Find All Income Beneficiaries and Their Trusts

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?beneficiary ?trust WHERE {
  ?trust ep:hasIncomeBeneficiary ?beneficiary .
}
```

### Trace Trust Amendments

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?trust ?amendment ?date WHERE {
  ?trust a :TrustEntity ;
         ep:amendedBy ?amendment .

  ?amendment ep:amendmentDate ?date .
}
ORDER BY ?date
```

### Find Assets Held as Life Estate

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?asset ?trust WHERE {
  ?asset ep:heldBy ?trust ;
         ep:heldAs ep:LifeEstate .
}
```

### Find All Fiduciary Duties (via Property Chain)

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?trust ?duty WHERE {
  ?trust ep:requiresFiduciaryDuty ?duty .
}
```

This query uses the **property chain** `requiresFiduciaryDuty` which infers:
```
:SmithFamilyTrust → hasTrustee → :FidelityTrust → owes → :FiduciaryDuty_Fidelity
```

### Find Legal Actions Involving Trusts

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?action ?trust ?type WHERE {
  ?action ep:involves ?trust ;
          a ?type .

  FILTER(?type IN (ep:TrustContest, ep:AccountingProceeding, ep:Reformation))
}
```

## Integration with Base Ontology

The extension seamlessly integrates with the base Trust Domain Ontology (v4.0):

### Reuses Existing Classes

- `:TrustEntity` - Base trust class
- `:hasBeneficiary` - Beneficiary property (base)
- `:hasTrustee` - Trustee property (base)
- `:hasProtector` - Protector property (base)

### Adds Specialized Variants

- `ep:hasIncomeBeneficiary` - Subproperty of `:hasBeneficiary`
- `ep:hasRemainderBeneficiary` - Subproperty of `:hasBeneficiary`
- `ep:hasCoTrustee` - Variant of trustee relationship
- `ep:hasSuccessorTrustee` - Future trustee designation

### Ontology Statistics (v2.0)

| Metric | Count |
|--------|-------|
| **Total triples** | 1,887 |
| **Total classes** | 131 |
| **Total properties** | 160 |
| **Named individuals** | 6 (trust states) |
| **Disjointness axioms** | 25+ |
| **Cardinality constraints** | 15+ |
| **Property chains** | 3 |
| **Defined classes** | 5+ (e.g., PotentialSelfDealingTransaction) |

**Validation**: ✓ Valid OWL 2 DL syntax (validated with rdflib)

### Compatible with Foundation Model

The estate planning extension focuses on **traditional trusts** while the base ontology focuses on **private foundations**:

| Feature | Base Ontology (v4.0) | Estate Planning Extension (v2.0) |
|---------|----------------------|----------------------------------|
| **Architecture** | Descriptive ontology | **Closed decision system** |
| **Focus** | Private foundations, charitable trusts | Traditional irrevocable trusts, estates |
| **Key Actors** | Foundation managers, grantees, disqualified persons | Grantors, settlors, income/remainder beneficiaries |
| **Documents** | IRS forms (706, 709, 1041) | Trust indentures, deeds, amendments |
| **Compliance** | IRC §§4941-4945 safeguards | **Outcome determination (IRC §4941 auto-inference)** |
| **State Model** | None | **6-state lifecycle machine with transitions** |
| **Temporal** | Fiscal years, qualifying distributions | Life estates, remainder interests, **state triggers** |
| **Operations** | Grantmaking, exempt activities | Asset holding, distributions, conveyances |
| **Reasoning** | Basic classification | **Automated outcome inference, inconsistency detection** |

### Combined Usage

Use both ontologies together for comprehensive trust modeling:

```turtle
@prefix : <http://example.org/trust-domain#> .
@prefix ep: <http://example.org/trust-domain/estate-planning#> .

###  Charitable Trust (uses both ontologies)
:CharitableTrust rdf:type :ForeignPrivateIrrevocableNonGrantorTrust ;
    # Estate planning properties
    ep:hasGrantor :Founder ;
    ep:establishedBy :TrustIndenture ;
    ep:hasIncomeBeneficiary :FounderSpouse ;
    ep:hasRemainderBeneficiary :PublicCharityBeneficiary ;

    # Foundation compliance properties
    :hasPurpose :FoundationMission ;
    :subjectToTax :EstateTax ;
    :makesGrant :GrantToStanfordMedicine ;

    # Temporal tracking
    :holdsAsset :TrustCorpus .
```

## Loading Both Ontologies

### Using Protégé

1. Open `trust-domain-ontology.ttl` (base)
2. File → Import → Select `trust-domain-estate-planning.ttl`
3. Reasoner will classify both ontologies

### Using Apache Jena

```java
OntModel base = ModelFactory.createOntologyModel(OntModelSpec.OWL_DL_MEM);
base.read("trust-domain-ontology.ttl", "TURTLE");

OntModel extension = ModelFactory.createOntologyModel(OntModelSpec.OWL_DL_MEM);
extension.read("trust-domain-estate-planning.ttl", "TURTLE");
extension.addSubModel(base);  // Extension imports base
```

### Using RDFLib (Python)

```python
from rdflib import Graph, Namespace

# Load base ontology
g = Graph()
g.parse("trust-domain-ontology.ttl", format="turtle")
g.parse("trust-domain-estate-planning.ttl", format="turtle")

# Both namespaces available
TD = Namespace("http://example.org/trust-domain#")
EP = Namespace("http://example.org/trust-domain/estate-planning#")
```

## Validation Examples

### Validate Trust Has Required Grantor

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

ASK {
  :SmithFamilyTrust a :TrustEntity ;
                    ep:hasGrantor ?grantor .
}
```

**Expected**: `true` (cardinality requires ≥1 grantor)

### Find Trusts Missing Required Elements

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?trust WHERE {
  ?trust a :TrustEntity .

  # Missing required grantor
  FILTER NOT EXISTS { ?trust ep:hasGrantor ?grantor }
}
```

**Expected**: EMPTY in valid ontology

### Validate Functional Properties

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

# Find trusts with multiple governing documents (violation)
SELECT ?trust (COUNT(?doc) AS ?count) WHERE {
  ?trust ep:governedBy ?doc .
}
GROUP BY ?trust
HAVING (COUNT(?doc) > 1)
```

**Expected**: EMPTY (governedBy is functional - max 1)

## Benefits

### 1. **Bidirectional Navigation**

All relationships have inverses:

```sparql
# Forward: Trust → Grantor
?trust ep:hasGrantor ?grantor .

# Reverse: Grantor → Trust
?grantor ep:creates ?trust .
```

### 2. **Cardinality Enforcement**

OWL reasoner detects violations:

```turtle
# VALID
:MyTrust ep:hasGrantor :JohnDoe .

# INVALID (would trigger reasoner error)
:MyTrust ep:governedBy :Doc1, :Doc2 .  # governedBy is functional!
```

### 3. **Property Chain Inference**

Complex patterns automatically inferred:

```turtle
# Explicitly stated:
:MyTrust :hasTrustee :FidelityBank .
:FidelityBank ep:owes :FiduciaryDuty_XYZ .

# Automatically inferred via property chain:
:MyTrust ep:requiresFiduciaryDuty :FiduciaryDuty_XYZ .
```

### 4. **Complete Legal Vocabulary**

Maps to Passbuckdefs glossary terms for legal precision.

### 5. **Modular Architecture**

Use extension **only when needed** - base ontology remains focused on foundations.

---

**See Also**:
- [Home](Home.md) - Main ontology documentation
- [Classes](Classes.md) - Base ontology classes
- [Properties](Properties.md) - Base ontology properties
- [Examples](Examples.md) - Foundation-focused examples
