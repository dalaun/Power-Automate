# Architecture: The Control-Plane Framework

[← Back to Home](Home.md)

## Overview

The Trust Domain Ontology models trusts as **control planes** - systems of authority with clearly defined operational boundaries. This page explains the doctrinal stack that enables non-grantor and foreign trusts to function as autonomous systems.

## The Doctrinal Stack

Non-grantor and foreign trusts acquire operational instruments once **control, jurisdiction, and fiduciary authority** are cleanly separated under this stack:

### 1. IRC §§671-679: The GATEWAY

**Purpose**: Determine who is the economic operator

**What it does**: Creates the **control-of-income boundary**

```turtle
:IRC_671_679 rdf:type :IRCSection ;
    rdfs:comment "Control-of-income boundary - determines who is the economic operator,
                  the gateway to non-grantor status" .
```

#### The Test

If a grantor retains **any** of these enumerated control powers, the trust is a grantor trust:

- **Reversionary Interest** (IRC §673) - assets revert to grantor
- **Power to Control Beneficial Enjoyment** (IRC §674) - grantor controls distributions
- **Administrative Powers** (IRC §675) - grantor exercises admin powers for own benefit
- **Power to Revoke** (IRC §676) - grantor can revoke trust
- **Income for Grantor Benefit** (IRC §677) - income held for grantor/spouse

**If no retained control → Non-Grantor Trust System** (crosses the gateway)

### 2. IRC §§641-685: The OPERATING SYSTEM

**Purpose**: Enable trust as autonomous accounting system

**What it does**: Allows trust to **retain income, deploy expenses, distribute outputs**

```turtle
:IRC_641_685 rdf:type :IRCSection ;
    rdfs:comment "Trust as autonomous accounting system - enables trust to retain income,
                  deploy expenses, distribute outputs" .
```

#### Key Components

**Distributable Net Income (DNI)**
- Accounting concept limiting deductible distributions
- Carries income character to beneficiaries

**Distribution Mechanism**
- Income distributions (from current income)
- Corpus distributions (from principal)
- Character flow-through (ordinary, capital gain, etc.)

**Fiduciary Returns**
- Form 1041 (domestic trusts)
- Form 1040-NR (foreign trusts)
- Schedule K-1 (beneficiary statements)

### 3. IRC §7701(a)(30)-(31): The JURISDICTION

**Purpose**: Assign which sovereign's rules apply

**What it does**: Determines **domestic vs foreign** status via two tests

```turtle
:IRC_7701 rdf:type :IRCSection ;
    rdfs:comment "Jurisdictional identity - assigns which sovereign's rules apply
                  via court and control tests" .
```

#### The Two-Part Test (BOTH Required for Domestic)

**Court Test**
- Can a US court exercise primary supervision over trust administration?

**Control Test**
- Do one or more US persons control all substantial trust decisions?

**Result**:
- Pass BOTH tests → Domestic Trust
- Fail EITHER test → Foreign Trust

### 4. IRC §162 / §212 / §67(e): The EXPENSE INSTRUMENTS

**Purpose**: Provide operational spending power

**What these do**: Define what trusts can spend on

#### IRC §162: Trade or Business Expenses
```turtle
:IRC_162 rdf:type :IRCSection ;
    rdfs:comment "Defines the operating boundary - ordinary and necessary business expenses" .
```

For trusts conducting trade or business.

#### IRC §212: Income Production Expenses
```turtle
:IRC_212 rdf:type :IRCSection ;
    rdfs:comment "Expenses for income production without trade or business -
                  trust expense instrument" .
```

For trusts producing income without conducting business.

#### IRC §67(e): Fiduciary-Specific Expenses
```turtle
:IRC_67e rdf:type :IRCSection ;
    rdfs:comment "Trust-specific expenses that would not exist but for fiduciary status" .
```

Expenses that exist **only because** of fiduciary administration.

---

## The System Identifier: EIN

The EIN (Employer Identification Number) is **NOT** an instrument - it's a **system identifier**.

```turtle
:EIN owl:disjointWith :Instrument .
```

**Analogy**: EIN is like a MAC address, not the protocol.

- Required for interaction with authorities
- Meaningless without the doctrinal stack
- Foreign trusts often use 98-series EINs

---

## How It All Fits Together

```
┌─────────────────────────────────────────────────┐
│ 1. IRC §§671-679: Do we have a separate system? │
│    → No retained control powers = YES           │
└────────────────┬────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────┐
│ 2. IRC §§641-685: Can the system operate?       │
│    → DNI, distributions, character flow = YES   │
└────────────────┬────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────┐
│ 3. IRC §7701: Which jurisdiction?               │
│    → Court + control tests = Domestic/Foreign   │
└────────────────┬────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────┐
│ 4. IRC §162/§212/§67(e): What can it spend on?  │
│    → Expense instruments now available          │
└─────────────────────────────────────────────────┘
```

---

## Example: Foreign Private Irrevocable Non-Grantor Trust

```turtle
:ExampleForeignTrust rdf:type :ForeignPrivateIrrevocableNonGrantorTrust ;
    :isRevocable "false"^^xsd:boolean ;        # Irrevocable
    :isGrantorTrust "false"^^xsd:boolean ;     # Non-grantor (crossed §§671-679 gateway)
    :isForeign "true"^^xsd:boolean ;           # Foreign (failed §7701 tests)
    :jurisdiction "Nevis" ;
    :hasEIN "98-1234567" ;                     # System identifier
    :hasTrustee :ExampleTrustee ;
    :hasPurpose :FoundationMission .
```

This trust:
1. ✅ Crossed the §§671-679 gateway (no retained control)
2. ✅ Operates under §§641-685 (computes DNI, makes distributions)
3. ✅ Classified under §7701 (foreign jurisdiction)
4. ✅ Can use expense instruments (§162, §212, §67(e))

---

## Why This Matters

Traditional view: "Non-grantor foreign trusts are tax structures."

**This ontology**: "Non-grantor foreign trusts are **control planes** with:
- Clear separation of authority (gateway)
- Autonomous operations (operating system)
- Defined jurisdiction (sovereign boundary)
- Legitimate expense instruments (spending power)"

Once you cross the gateway and establish jurisdiction, you have a **system capable of deploying instruments** - not a "tax dodge."

---

**Next**: [The Keystone Constraint →](Keystone-Constraint.md)
