# Estate Planning Extension

[← Back to Home](Home.md)

## Overview

The **Trust Domain Estate Planning Extension** adds comprehensive traditional trust and estate planning vocabulary to the Trust Domain Ontology. Based on the Passbuckdefs legal glossary, this extension provides complete coverage of:

- **Participant roles** (Grantor, Settlor, Trustee, Beneficiary variants)
- **Document hierarchy** (Trust Indentures, Deeds, Amendments)
- **Property tenure** (Fee Simple, Life Estate, Remainder)
- **Legal actions** (Trust Contests, Reformation, Accounting)
- **Comprehensive relationships** with inverse properties
- **Cardinality constraints** ensuring ontological integrity

## File Structure

```
trust-domain-ontology.ttl          # Base ontology (v4.0)
trust-domain-estate-planning.ttl   # Estate planning extension (v1.0)
```

The extension **imports** the base ontology, allowing selective use:

```turtle
<http://example.org/trust-domain/estate-planning> rdf:type owl:Ontology ;
    owl:imports <http://example.org/trust-domain> .
```

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

### Compatible with Foundation Model

The estate planning extension focuses on **traditional trusts** while the base ontology focuses on **private foundations**:

| Feature | Base Ontology (v4.0) | Estate Planning Extension (v1.0) |
|---------|----------------------|----------------------------------|
| **Focus** | Private foundations, charitable trusts | Traditional irrevocable trusts, estates |
| **Key Actors** | Foundation managers, grantees, disqualified persons | Grantors, settlors, income/remainder beneficiaries |
| **Documents** | IRS forms (706, 709, 1041) | Trust indentures, deeds, amendments |
| **Compliance** | IRC §§4941-4945 safeguards | Fiduciary duties, property tenure |
| **Temporal** | Fiscal years, qualifying distributions | Life estates, remainder interests |
| **Operations** | Grantmaking, exempt activities | Asset holding, distributions, conveyances |

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
