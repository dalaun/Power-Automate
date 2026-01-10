# Usage Guide

[← Back to Home](Home.md)

This guide shows how to load, query, and validate the Trust Domain Ontology.

## Loading the Ontology

### Using Protégé

1. Download [Protégé](https://protege.stanford.edu/)
2. File → Open → Select `trust-domain-ontology.ttl`
3. The reasoner will automatically classify the ontology

### Using Apache Jena

```java
import org.apache.jena.rdf.model.*;
import org.apache.jena.ontology.*;

// Load the ontology
OntModel model = ModelFactory.createOntologyModel(OntModelSpec.OWL_DL_MEM);
model.read("trust-domain-ontology.ttl", "TURTLE");

// Run reasoner
InfModel inf = ModelFactory.createInfModel(
    ReasonerRegistry.getOWLReasoner(), model
);
```

### Using RDFLib (Python)

```python
from rdflib import Graph, Namespace

# Load ontology
g = Graph()
g.parse("trust-domain-ontology.ttl", format="turtle")

# Define namespace
TD = Namespace("http://example.org/trust-domain#")
```

---

## SPARQL Queries

### Find All Spending That Fails to Trace Back to Purpose

**Use Case**: Identify potential private inurement

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?spend ?label WHERE {
  ?spend a :ActualSpend .

  # Spend exists but cannot trace back to purpose
  FILTER NOT EXISTS {
    ?spend :tracesBackTo ?purpose .
  }

  OPTIONAL { ?spend rdfs:label ?label }
}
```

**Expected Result**: Should return EMPTY (all spend traces back in valid ontology)

### Validate Complete Authority Cascade

**Use Case**: Audit trail for specific expenditure

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?spend ?operator ?activity ?purpose WHERE {
  ?spend a :ActualSpend ;
         :tracesBackTo ?purpose .

  # Trace backward through cascade
  ?expenseDomain :manifestsAs ?spend ;
                 :sustains ?operator .

  ?operator :servesActivity ?activity .

  ?activity :advancesPurpose ?purpose .
}
```

**Example Result**:
```
| spend                                  | operator                  | activity               | purpose                   |
|----------------------------------------|---------------------------|------------------------|---------------------------|
| SalaryPayment_DrSmith_January2024      | ResearchScientistDrSmith  | ClinicalTrialsActivity | FoundationHealthMission   |
| HealthInsurance_DrSmith_January2024    | ResearchScientistDrSmith  | ClinicalTrialsActivity | FoundationHealthMission   |
```

### Find All Permissible Private Enablement

**Use Case**: Verify all private enablement satisfies keystone constraint

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?enablement ?purpose ?activity WHERE {
  ?enablement a :PermissiblePrivateEnablement ;
              :isIncidentalTo ?purpose ;
              :isInseparableFrom ?activity ;
              :satisfiesKeystoneConstraint :TheKeystoneConstraint .
}
```

### Find Improper Private Enablement

**Use Case**: Flag potential private inurement for review

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?enablement ?description WHERE {
  ?enablement a :ImproperPrivateEnablement ;
              :violatesKeystoneConstraint :TheKeystoneConstraint .

  OPTIONAL { ?enablement rdfs:comment ?description }
}
```

**Example Result**:
```
| enablement                      | description                                                    |
|---------------------------------|----------------------------------------------------------------|
| ExampleImproperLavishExpense    | Luxury vacation for trustee unrelated to mission activities   |
| ExampleImproperExcessCompensation | Compensation far exceeding market rate                       |
```

### List All Authorized Activities by Purpose Domain

**Use Case**: What activities does each purpose domain authorize?

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?purpose ?purposeLabel ?activity ?activityLabel WHERE {
  ?purpose a :Purpose ;
           :authorizes ?activity .

  ?activity a :AuthorizedActivity .

  OPTIONAL { ?purpose rdfs:label ?purposeLabel }
  OPTIONAL { ?activity rdfs:label ?activityLabel }
}
```

### Find All Expense Domains for an Operator

**Use Case**: What expense domains does a specific operator necessitate?

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?operator ?expenseDomain ?spend WHERE {
  ?operator a :OperatorInRole ;
            :necessitates ?expenseDomain .

  ?expenseDomain :manifestsAs ?spend .

  FILTER(?operator = :ResearchScientistDrSmith)
}
```

---

## Temporal Tracking Queries (v4.0)

### Find All Expenditures for Fiscal Year

**Use Case**: Track all spending during a specific fiscal year

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?spend ?date ?purpose WHERE {
  ?spend a :ActualSpend ;
         :occursDuring :FiscalYear2024 ;
         :tracesBackTo ?purpose .

  OPTIONAL { ?spend :expenditureDate ?date }
  OPTIONAL { ?spend rdfs:label ?label }
}
ORDER BY ?date
```

### Check Minimum Distribution Compliance (IRC §4942)

**Use Case**: Verify foundation meets minimum distribution requirements

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?fiscalYear ?required ?actual ?compliant WHERE {
  ?fiscalYear a :FiscalYear ;
              :minimumDistributionRequired ?required ;
              :qualifyingDistributionsMade ?actual .

  BIND((?actual >= ?required) AS ?compliant)
}
ORDER BY DESC(?fiscalYear)
```

**Example Result**:
```
| fiscalYear      | required | actual  | compliant |
|-----------------|----------|---------|-----------|
| FiscalYear2024  | 500000   | 625000  | true      |
```

### Find DNI for Specific Fiscal Year

**Use Case**: Retrieve DNI computation for tax reporting

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?fiscalYear ?dniAmount WHERE {
  ?dni a :DistributableNetIncome ;
       :computedFor ?fiscalYear ;
       :dniAmount ?dniAmount .

  FILTER(?fiscalYear = :FiscalYear2024)
}
```

### Time-Series Analysis: Spending Trends

**Use Case**: Analyze spending patterns over time

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?fiscalYear (COUNT(?spend) AS ?spendCount) WHERE {
  ?fiscalYear a :FiscalYear .
  ?spend a :ActualSpend ;
         :occursDuring ?fiscalYear .
}
GROUP BY ?fiscalYear
ORDER BY ?fiscalYear
```

---

## Grantmaking Queries (v4.0)

### Find All Grants to Public Charities

**Use Case**: List all qualifying grants

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?grant ?grantee ?amount ?qd WHERE {
  ?grant a :Grant ;
         :grantAmount ?amount ;
         :receivesGrant ?grantee ;
         :satisfiesQualifyingDistribution ?qd .

  ?grantee a :PublicCharity .

  OPTIONAL { ?grantee rdfs:label ?granteeLabel }
}
ORDER BY DESC(?amount)
```

**Example Result**:
```
| grant                    | grantee          | amount  | qd              |
|--------------------------|------------------|---------|-----------------|
| GrantToStanfordMedicine  | StanfordMedicine | 250000  | QD_StanfordGrant|
```

### Calculate Total Qualifying Distributions

**Use Case**: Sum all qualifying distributions for IRC §4942 compliance

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?fiscalYear (SUM(?amount) AS ?totalQualifying) WHERE {
  ?grant a :Grant ;
         :grantAmount ?amount ;
         :satisfiesQualifyingDistribution ?qd .

  ?activity a :GrantmakingActivity ;
            :hasTemporalExtent ?fiscalYear .
}
GROUP BY ?fiscalYear
```

### Find Grants Requiring Expenditure Responsibility

**Use Case**: Identify grants to non-exempt grantees

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?grant ?grantee ?amount WHERE {
  ?grant a :Grant ;
         :grantAmount ?amount ;
         :receivesGrant ?grantee .

  ?grantee a :NonExemptGrantee .
}
```

### List All Grantmaking Activities

**Use Case**: Track grantmaking separate from operations

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?activity ?purpose ?fiscalYear WHERE {
  ?activity a :GrantmakingActivity ;
            :advancesPurpose ?purpose ;
            :hasTemporalExtent ?fiscalYear .
}
```

---

## IRC §§4941-4945 Safeguard Queries (v4.0)

### Detect IRC §4941 Self-Dealing Violations

**Use Case**: Find transactions with disqualified persons

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?transaction ?disqualifiedPerson ?amount WHERE {
  ?transaction a :SelfDealingTransaction ;
               :involvesDisqualifiedPerson ?disqualifiedPerson .

  OPTIONAL { ?transaction :transactionAmount ?amount }
  OPTIONAL { ?transaction rdfs:label ?label }
}
```

**Expected**: EMPTY in compliant foundation (violations trigger alerts)

### Find Excess Business Holdings (IRC §4943)

**Use Case**: Identify holdings exceeding 20% limit

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?holding ?percentage ?excess WHERE {
  ?holding a :ExcessBusinessHolding ;
           :hasOwnershipPercentage ?percentage ;
           :excessHoldingPercentage ?excess .

  FILTER(?percentage > 20.0)
}
```

### Detect Jeopardizing Investments (IRC §4944)

**Use Case**: Find investments endangering mission

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?investment ?purpose WHERE {
  ?investment a :JeopardizingInvestment ;
              :jeopardizesMission ?purpose .
}
```

### Find All Taxable Expenditures (IRC §4945)

**Use Case**: Identify prohibited expenditures

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?expenditure ?type ?amount WHERE {
  ?expenditure a :TaxableExpenditure ;
               a ?type .

  OPTIONAL { ?expenditure :transactionAmount ?amount }

  # Filter to specific subtypes
  FILTER(?type IN (:LobbyingExpenditure, :PoliticalExpenditure,
                   :GrantWithoutExpenditureResponsibility))
}
```

### Detect All Authority Collapses

**Use Case**: Find any violations across all safeguards

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?violation ?type ?description WHERE {
  ?violation a :AuthorityCollapse ;
             a ?type .

  OPTIONAL { ?violation rdfs:comment ?description }

  # All violations are subclasses of AuthorityCollapse
}
```

**Example Result**:
```
| violation                     | type                    | description                      |
|-------------------------------|-------------------------|----------------------------------|
| ExampleSelfDealing            | SelfDealingTransaction  | Sale to disqualified person      |
| ExampleExcessHolding          | ExcessBusinessHolding   | 35% ownership exceeds limit      |
| ExampleJeopardizingInvestment | JeopardizingInvestment  | Speculative investment           |
| ExampleLobbyingExpenditure    | LobbyingExpenditure     | Expenditure for lobbying         |
```

---

## Validation Queries

### Check if Trust Has Required Purpose

```sparql
PREFIX : <http://example.org/trust-domain#>

ASK {
  :ExampleFoundationTrust a :TrustEntity ;
                          :hasPurpose ?purpose .
}
```

**Expected**: `true` (TrustEntity MUST have purpose)

### Check if Enablement Satisfies Keystone Constraint

```sparql
PREFIX : <http://example.org/trust-domain#>

ASK {
  ?enablement a :PermissiblePrivateEnablement ;
              :isIncidentalTo ?purpose ;
              :isInseparableFrom ?activity .
}
```

**Expected**: `true` (PermissiblePrivateEnablement MUST satisfy both tests)

### Check for Orphaned Spending

**Use Case**: Find spend that doesn't connect to expense domain

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?spend WHERE {
  ?spend a :ActualSpend .

  FILTER NOT EXISTS {
    ?expenseDomain :manifestsAs ?spend .
  }
}
```

**Expected**: EMPTY (all spend should come from expense domain)

---

## Reasoning Queries

### Infer Missing Classifications

The reasoner can infer that something is improper if it's PrivateEnablement but not Permissible:

```sparql
PREFIX : <http://example.org/trust-domain#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?enablement WHERE {
  ?enablement a :PrivateEnablement .

  FILTER NOT EXISTS {
    ?enablement a :PermissiblePrivateEnablement .
  }

  # Must be ImproperPrivateEnablement (disjoint classes)
}
```

### Detect Inconsistencies

If something claims to be both Permissible AND Improper (impossible due to disjoint axiom):

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?enablement WHERE {
  ?enablement a :PermissiblePrivateEnablement ,
                :ImproperPrivateEnablement .
}
```

**Expected**: EMPTY or reasoner error (disjoint violation)

---

## Property Path Queries

### Trace Complete Cascade with Property Paths

**Use Case**: Navigate from spend all the way back to mission

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?spend ?mission WHERE {
  ?spend a :ActualSpend .

  # Trace backward through full cascade
  ?spend ^:manifestsAs / ^:necessitates / ^:requires / ^:authorizes ?purpose .

  ?mission :hasSubPurpose* ?purpose .
}
```

### Find All Descendants of Mission

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?descendant WHERE {
  :FoundationMission :hasSubPurpose+ ?descendant .
}
```

**Result**: All four sub-purposes (Health, Education, Innovation, Opportunity)

---

## Aggregate Queries

### Count Spending by Purpose Domain

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?purpose (COUNT(?spend) AS ?spendCount) WHERE {
  ?spend a :ActualSpend ;
         :tracesBackTo ?purpose .
}
GROUP BY ?purpose
ORDER BY DESC(?spendCount)
```

### Sum Total Permissible Enablement

If spend amounts were stored:

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT (SUM(?amount) AS ?total) WHERE {
  ?spend a :ActualSpend ;
         :amount ?amount .

  ?expenseDomain :manifestsAs ?spend ;
                 :enablesPrivately ?enablement .

  ?enablement a :PermissiblePrivateEnablement .
}
```

---

## Python Examples

### Using RDFLib to Query

```python
from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

# Load ontology
g = Graph()
g.parse("trust-domain-ontology.ttl", format="turtle")

# Define namespace
TD = Namespace("http://example.org/trust-domain#")

# Query: Find all actual spend
query = prepareQuery("""
    PREFIX : <http://example.org/trust-domain#>

    SELECT ?spend ?purpose WHERE {
        ?spend a :ActualSpend ;
               :tracesBackTo ?purpose .
    }
""")

results = g.query(query)
for row in results:
    print(f"Spend: {row.spend}, Purpose: {row.purpose}")
```

### Validate Keystone Constraint

```python
def validate_keystone_constraint(g, enablement_uri):
    """Check if enablement satisfies both keystone tests"""

    query = prepareQuery("""
        PREFIX : <http://example.org/trust-domain#>

        ASK {
            ?enablement :isIncidentalTo ?purpose ;
                       :isInseparableFrom ?activity .
        }
    """, initNs={"enablement": enablement_uri})

    result = g.query(query, initBindings={"enablement": enablement_uri})
    return bool(result)
```

---

## Common Patterns

### Pattern 1: Validate New Expenditure

Before approving spend, ensure cascade completes:

```python
def can_approve_spend(spend_uri):
    # Check if spend traces to purpose
    if not traces_to_purpose(spend_uri):
        return False, "Spend does not trace to purpose"

    # Check if expense domain sustains operator
    if not sustains_operator(spend_uri):
        return False, "Expense domain does not sustain operator"

    # Check if operator serves authorized activity
    if not serves_activity(spend_uri):
        return False, "Operator does not serve authorized activity"

    return True, "Spend approved - cascade complete"
```

### Pattern 2: Generate Audit Report

```python
def generate_audit_trail(spend_uri):
    """Generate complete audit trail for expenditure"""

    report = []
    report.append(f"Audit Trail for: {spend_uri}")

    # Query cascade
    cascade_query = """
        SELECT ?expenseDomain ?operator ?activity ?purpose WHERE {
            ?spend :tracesBackTo ?purpose .
            ?expenseDomain :manifestsAs ?spend ;
                          :sustains ?operator .
            ?operator :servesActivity ?activity .
            ?activity :advancesPurpose ?purpose .
        }
    """

    results = g.query(cascade_query, initBindings={"spend": spend_uri})

    for row in results:
        report.append(f"  Expense Domain: {row.expenseDomain}")
        report.append(f"  Operator: {row.operator}")
        report.append(f"  Activity: {row.activity}")
        report.append(f"  Purpose: {row.purpose}")

    return "\n".join(report)
```

---

**See Also**:
- [Examples](Examples.md) - Concrete individuals to query
- [Properties](Properties.md) - Available properties for queries
- [Architecture](Architecture.md) - Understanding the framework
