#!/usr/bin/env python3
"""
Generate Mermaid Diagrams from Ontology
========================================

Generates .md files with embedded Mermaid diagrams for:
- Trust state machine
- Class hierarchy
- Transaction classification
- Authority cascade
"""

import sys
from rdflib import Graph, Namespace

EP = Namespace("http://example.org/trust-domain/estate-planning#")
TD = Namespace("http://example.org/trust-domain#")

def generate_state_machine(output_file="diagrams/trust-state-machine.md"):
    """Generate trust state machine diagram"""

    diagram = """# Trust State Machine

```mermaid
stateDiagram-v2
    [*] --> TrustCreated: Trust instrument executed

    TrustCreated --> TrustFunded: Initial funding
    TrustCreated --> TrustRevoked: Grantor revokes
    TrustCreated --> TrustTerminated: Fails validity

    TrustFunded --> TrustActive: Validity confirmed
    TrustFunded --> TrustRevoked: Grantor revokes
    TrustFunded --> TrustTerminated: Fails validity

    TrustActive --> TrustIrrevocable: Irrevocability event
    TrustActive --> TrustRevoked: Grantor revokes (if revocable)
    TrustActive --> TrustTerminated: Termination event

    TrustIrrevocable --> TrustTerminated: Termination event only

    TrustRevoked --> [*]
    TrustTerminated --> [*]

    note right of TrustCreated
        Document executed
        Not yet funded
    end note

    note right of TrustIrrevocable
        Cannot be revoked
        Only termination possible
    end note
```

## State Definitions

| State | Description | Can Transition To |
|-------|-------------|-------------------|
| **TrustCreated** | Instrument executed, not funded | Funded, Revoked, Terminated |
| **TrustFunded** | Assets transferred to trustee | Active, Revoked, Terminated |
| **TrustActive** | Operating with validity confirmed | Irrevocable, Revoked, Terminated |
| **TrustIrrevocable** | Cannot be revoked | Terminated only |
| **TrustRevoked** | Grantor cancelled trust | Terminal state |
| **TrustTerminated** | Trust ended (merger, RAP, etc.) | Terminal state |

## Irrevocability Events

- Grantor death
- Trust terms specify irrevocability from inception
- Explicit irrevocability declaration

## Termination Events

- Merger (legal + equitable title merge)
- Purpose fulfilled
- Rule Against Perpetuities violation
- Final distribution to remaindermen
"""

    with open(output_file, 'w') as f:
        f.write(diagram)

    print(f"✓ Generated: {output_file}")

def generate_transaction_classification(output_file="diagrams/transaction-classification.md"):
    """Generate transaction classification diagram"""

    diagram = """# Transaction Classification Matrix

```mermaid
graph TB
    subgraph "Relationship Dimension"
        TX[Transaction]
        TX --> ALT[Arms Length Transaction]
        TX --> RPT[Related Party Transaction]
    end

    subgraph "Pricing Dimension"
        TX2[Transaction]
        TX2 --> FVT[Fair Value Transaction]
        TX2 --> BMT[Below Market Transaction]
        TX2 --> AMT[Above Market Transaction]
    end

    subgraph "Outcome Determination"
        Combination[2D Classification]

        Combination --> Combo1[Related Party<br/>+ Below Market]
        Combination --> Combo2[Related Party<br/>+ Above Market]
        Combination --> Combo3[Arms Length<br/>+ Any Pricing]

        Combo1 --> IRC4941[IRC §4941<br/>Self-Dealing]
        Combo2 --> IRC4958[IRC §4958<br/>Excess Benefit]
        Combo3 --> OK[Permissible]

        style IRC4941 fill:#ffcccc
        style IRC4958 fill:#ffcccc
        style OK fill:#ccffcc
    end
```

## Classification Rules

### Disjointness Constraints

**Relationship Dimension** (mutually exclusive):
- `ArmsLengthTransaction ⊥ RelatedPartyTransaction`

**Pricing Dimension** (mutually exclusive):
- `FairValueTransaction ⊥ BelowMarketTransaction ⊥ AboveMarketTransaction`

### Closure Axioms

Every transaction MUST be classified on BOTH dimensions:

```turtle
ep:Transaction rdfs:subClassOf
    [ owl:unionOf ( ep:ArmsLengthTransaction ep:RelatedPartyTransaction ) ] .

ep:Transaction rdfs:subClassOf
    [ owl:unionOf ( ep:FairValueTransaction
                    ep:BelowMarketTransaction
                    ep:AboveMarketTransaction ) ] .
```

### Automatic Inference

```turtle
# IRC §4941 Self-Dealing
ep:PotentialSelfDealingTransaction owl:equivalentClass
    [ owl:intersectionOf ( ep:RelatedPartyTransaction
                          ep:BelowMarketTransaction ) ] .
```

The OWL reasoner automatically classifies transactions that meet both criteria!
"""

    with open(output_file, 'w') as f:
        f.write(diagram)

    print(f"✓ Generated: {output_file}")

def generate_authority_cascade(output_file="diagrams/authority-cascade.md"):
    """Generate authority cascade diagram"""

    diagram = """# Authority Cascade

```mermaid
graph TB
    Mission[Foundation Mission]

    Mission -->|legitimizes| Auth[Authority]
    Auth -->|has purpose| Purpose[Purpose Domains]
    Purpose -->|authorize| Activity[Authorized Activities]
    Activity -->|require| Operator[Operators in Role]
    Operator -->|necessitate| Expense[Expense Domains]
    Expense -->|manifest as| Spend[Actual Spend]

    Spend -->|traces back to| Check{Path exists?}

    Check -->|YES| Valid[✓ Permissible]
    Check -->|NO| Invalid[✗ Private Inurement]

    style Mission fill:#e1f5ff
    style Valid fill:#ccffcc
    style Invalid fill:#ffcccc

    subgraph "The Litmus Test"
        Check
    end

    subgraph "Keystone Constraint"
        KC[Private enablement permissible when:<br/>1. Incidental to purpose<br/>2. Inseparable from purpose]
    end
```

## SPARQL Validation Query

```sparql
PREFIX td: <http://example.org/trust-domain#>

ASK {
    ?spend td:manifestsIn ?expenseDomain .
    ?expenseDomain td:necessitatedBy ?operator .
    ?operator td:requiresFor ?activity .
    ?activity td:authorizedBy ?purpose .
    ?purpose td:hasPurpose ?mission .
}
```

**Returns TRUE** → Spend traces to mission → Permissible
**Returns FALSE** → Path broken → Private inurement

## The Keystone Constraint

> **Private enablement is permissible when and only when it is BOTH:**
> 1. **Incidental to** purpose-driven execution (not the primary purpose), AND
> 2. **Inseparable from** purpose-driven execution (necessarily coupled with mission)

This is tax compliance as a **graph traversal problem**.
"""

    with open(output_file, 'w') as f:
        f.write(diagram)

    print(f"✓ Generated: {output_file}")

def generate_architecture_diagram(output_file="diagrams/technology-stack.md"):
    """Generate complete technology stack diagram"""

    diagram = """# Technology Stack Architecture

```mermaid
graph TB
    subgraph "Authorship Layer"
        Claude[Claude AI]
        Claude -->|Creates| Ont[Ontology Files .ttl]
        Claude -->|Writes| Docs[Documentation .md]
    end

    subgraph "Interpretation Layer"
        Ont --> rdflib[rdflib]
        Ont --> Owlready[Owlready2]

        rdflib -->|SPARQL| Queries[Queries]
        Owlready -->|Reasoning| Infer[Inferences]
    end

    subgraph "Memory Layer"
        KG[(RDF Knowledge Graph)]
        rdflib --> KG
        Owlready --> KG

        KG -->|Stores| Instances[Trust Instances]
        KG -->|Stores| Facts[Compliance Facts]
    end

    subgraph "Visualization Layer"
        Mermaid[Mermaid.js]
        Docs --> Mermaid
        Mermaid -->|Renders| Viz[State Machines<br/>Flows<br/>Hierarchies]
    end

    subgraph "Exploration Layer"
        Neo4j[(Neo4j Property Graph)]
        KG -->|Export| Neo4j
        Neo4j -->|What-if| Scenarios[Hypotheticals]
        Neo4j -->|Analytics| Paths[Authority Paths]
    end

    subgraph "Version Control"
        GitHub[GitHub Repository]
        Ont --> GitHub
        Docs --> GitHub
        GitHub -->|Tracks| History[Change History]
    end

    style Claude fill:#e1f5ff
    style KG fill:#e8f5e9
    style Neo4j fill:#ffe0b2
    style GitHub fill:#fce4ec
```

## Technology Matrix

| Task | Tool | Purpose |
|------|------|---------|
| **Author ontology** | Claude | Design dual-ontology (vocabulary + compliance) |
| **Load ontology** | Owlready2 | TBox reasoning, automatic inference |
| **Add instances** | rdflib | ABox data, SPARQL queries |
| **Store knowledge** | RDF KG | Persistent triple store |
| **Explore scenarios** | Neo4j | Graph analytics, what-if analysis |
| **Visualize** | Mermaid | State machines, flows, hierarchies |
| **Version control** | GitHub | Track changes, review, rollback |

## File Organization

```
/
├── trust-domain-vocabulary.ttl    # Semantic layer
├── trust-domain-compliance.ttl    # Authority layer
├── instances/
│   └── *.ttl                      # RDF instance data
├── diagrams/
│   └── *.md                       # Mermaid diagrams
├── scripts/
│   ├── complete_workflow.py      # Full stack workflow
│   ├── export_to_neo4j.py        # Neo4j export
│   └── generate_diagrams.py      # Mermaid generator
└── knowledge-graph.ttl            # Combined RDF graph
```
"""

    with open(output_file, 'w') as f:
        f.write(diagram)

    print(f"✓ Generated: {output_file}")

if __name__ == "__main__":
    import os

    # Create diagrams directory
    os.makedirs("diagrams", exist_ok=True)

    print("Generating Mermaid diagrams...\n")

    generate_state_machine()
    generate_transaction_classification()
    generate_authority_cascade()
    generate_architecture_diagram()

    print(f"\n✓ All diagrams generated in diagrams/")
    print(f"\nView on GitHub - Mermaid renders automatically in .md files!")
