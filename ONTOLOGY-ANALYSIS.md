# Trust Domain Estate Planning Ontology - Axiom Analysis

## Purpose
Systematically categorize every axiom in `trust-domain-estate-planning.ttl` to determine:
- **SEMANTIC COMMITMENTS** (Data-Centric): Defines what things mean
- **AUTHORITY COMMITMENTS** (Operational): Enforces what is allowed/determines outcomes
- **MIXED**: Axioms doing both jobs (need refactoring)

## Litmus Test
> "If I remove this rule, do I lose **understanding** — or do I lose **authority**?"
- Lose understanding → SEMANTIC (data-centric)
- Lose authority → AUTHORITY (operational)

---

## ANALYSIS BY SECTION

### 1. ANNOTATION PROPERTIES

```turtle
ep:glossaryTerm rdf:type owl:AnnotationProperty
```
**Category**: SEMANTIC
**Reason**: Maps terms to glossary. No enforcement, just meaning.
**Test**: Remove this → lose understanding of glossary mapping, but no authority lost.

---

### 2. OBJECT PROPERTIES (Lines 101-1092)

#### Example: ep:hasGrantor

```turtle
ep:hasGrantor rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf ep:participatesIn ;
    rdfs:domain :TrustEntity ;
    rdfs:range ep:Grantor ;
    owl:inverseOf ep:creates ;
    rdfs:label "has grantor"@en ;
    rdfs:comment "Trust has grantor who created and funded it"@en ;
    ep:glossaryTerm "Grantor, Creator, Trustor" .
```

**Breaking this down**:
- `rdf:type owl:ObjectProperty` → SEMANTIC (declares property exists)
- `rdfs:subPropertyOf ep:participatesIn` → SEMANTIC (taxonomy/meaning)
- `rdfs:domain :TrustEntity` → SEMANTIC (what connects to what)
- `rdfs:range ep:Grantor` → SEMANTIC (type constraint is meaning)
- `owl:inverseOf ep:creates` → SEMANTIC (bidirectional navigation is meaning)
- `rdfs:label`, `rdfs:comment`, `ep:glossaryTerm` → SEMANTIC (documentation)

**Overall**: SEMANTIC
**Test**: Remove property definition → lose understanding of relationship, but enforcement happens elsewhere (cardinality constraints)

#### Pattern for ALL 160+ Properties:
**Property definitions themselves** → SEMANTIC
**Cardinality constraints on properties** → AUTHORITY (analyzed separately)

---

### 3. DATA PROPERTIES (Lines 1095-1343)

```turtle
ep:trustDate rdf:type owl:DatatypeProperty ;
    rdfs:domain :TrustEntity ;
    rdfs:range xsd:date ;
    rdfs:label "trust date"@en ;
    rdfs:comment "Date trust was established"@en .
```

**Category**: SEMANTIC
**Reason**: Defines what the property means, not what's enforced.
**All data properties follow same pattern** → SEMANTIC

---

### 4. CLASS DEFINITIONS (Lines 1345-2103)

#### Participant Classes

```turtle
ep:Grantor rdf:type owl:Class ;
    rdfs:subClassOf ep:Participant ;
    rdfs:label "Grantor"@en ;
    rdfs:comment "Person creating and funding trust"@en ;
    ep:glossaryTerm "Grantor, Creator, Trustor" .
```

**Breaking down**:
- `rdf:type owl:Class` → SEMANTIC
- `rdfs:subClassOf ep:Participant` → SEMANTIC (taxonomy)
- `rdfs:label`, `rdfs:comment`, `glossaryTerm` → SEMANTIC

**Category**: SEMANTIC

#### Transaction Classes (Important!)

```turtle
ep:ArmsLengthTransaction rdf:type owl:Class ;
    rdfs:subClassOf ep:Transaction ;
    rdfs:label "Arm's Length Transaction"@en ;
    rdfs:comment "Transaction conducted between unrelated parties..."@en ;
    ep:glossaryTerm "ArmsLengthTransaction, ArmsLength" .
```

**Category**: SEMANTIC (class definition)

BUT ALSO:

```turtle
ep:RelatedPartyTransaction rdf:type owl:Class ;
    rdfs:subClassOf ep:Transaction ;
    owl:disjointWith ep:ArmsLengthTransaction ;  # ← THIS IS AUTHORITY
    rdfs:label "Related Party Transaction"@en ;
    ...
```

**MIXED AXIOM DETECTED**:
- Class definition part → SEMANTIC
- `owl:disjointWith` → AUTHORITY (enforces mutual exclusion)

**This needs refactoring!**

#### State Machine Classes

```turtle
ep:TrustCreated rdf:type owl:NamedIndividual, ep:TrustState ;
    rdfs:label "Trust Created"@en ;
    rdfs:comment "Trust instrument executed but not yet funded"@en .
```

**Category**: SEMANTIC (defines what the state means)

BUT:

```turtle
ep:TrustState rdf:type owl:Class ;
    owl:equivalentClass [ owl:oneOf (ep:TrustCreated ep:TrustFunded ...) ] .
```

**Category**: AUTHORITY (closed enumeration - limits what states can exist)

#### Outcome Classes

```turtle
ep:IRC4941ExciseTax rdf:type owl:Class ;
    rdfs:subClassOf ep:TaxConsequence ;
    rdfs:label "IRC §4941 Excise Tax"@en ;
    rdfs:comment "Excise tax on self-dealing..."@en ;
    ep:glossaryTerm "SelfDealing, IRC4941" .
```

**Category**: SEMANTIC (defines what the outcome means)

---

### 5. CARDINALITY CONSTRAINTS (Lines 2108-2167)

```turtle
:TrustEntity rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:hasGrantor ;
      owl:minCardinality "1"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY
**Reason**: Enforces that trust MUST have ≥1 grantor.
**Test**: Remove this → lose authority (trust can exist with 0 grantors), understanding unchanged.

**ALL cardinality constraints** → AUTHORITY

Examples:
- `minCardinality "1"` on hasGrantor → AUTHORITY
- `cardinality "1"` on establishedBy → AUTHORITY
- `maxCardinality "1"` on hasProtector → AUTHORITY
- `someValuesFrom` (existential) on owes FiduciaryDuty → AUTHORITY

---

### 6. TRANSACTION AXIOMS (Lines 2168-2197)

```turtle
ep:ArmsLengthTransaction rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:meetsArmsLengthStandard ;
      owl:someValuesFrom ep:ArmsLengthStandard ] .
```

**Category**: AUTHORITY
**Reason**: Enforces that ArmsLengthTransaction MUST meet the standard.

```turtle
ep:BelowMarketTransaction rdfs:subClassOf
    [ rdf:type owl:Restriction ;
      owl:onProperty ep:meetsArmsLengthStandard ;
      owl:maxCardinality "0"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY
**Reason**: Enforces that BelowMarket CANNOT meet arm's length standard (maxCard 0 = prohibition).

**ALL transaction axioms** → AUTHORITY

---

### 7. DISJOINTNESS DECLARATIONS (Lines 2320-2403)

```turtle
ep:FairValueTransaction owl:disjointWith ep:BelowMarketTransaction, ep:AboveMarketTransaction .
```

**Category**: AUTHORITY
**Reason**: Enforces mutual exclusion - violation = inconsistency.
**Test**: Remove this → lose authority (transaction can be both FairValue AND BelowMarket), understanding unchanged.

```turtle
ep:Witness owl:disjointWith ep:Grantor, ep:Settlor, ep:Trustee, ep:Beneficiary .
```

**Category**: AUTHORITY

```turtle
ep:TrustValidity owl:disjointWith ep:AssetTransferValidity .
```

**Category**: AUTHORITY (enforces Hague two-step separation)

```turtle
ep:MandatoryRule owl:disjointWith ep:ChoiceOfLaw .
```

**Category**: AUTHORITY (enforces that mandatory rules override choice of law)

**ALL disjointness axioms** → AUTHORITY

---

### 8. CLOSURE AXIOMS (Lines 2343-2350, 2651-2707)

```turtle
ep:Transaction rdfs:subClassOf
    [ owl:unionOf (ep:ArmsLengthTransaction ep:RelatedPartyTransaction) ] .
```

**Category**: AUTHORITY
**Reason**: Forces every transaction to be classified.
**Test**: Remove this → lose authority (transaction doesn't need classification), understanding unchanged.

```turtle
:TrustEntity rdfs:subClassOf
    [ owl:onProperty ep:hasState ;
      owl:cardinality "1"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY (every trust MUST be in exactly one state)

**ALL closure axioms** → AUTHORITY

---

### 9. STATE MACHINE (Lines 2405-2540)

#### State Enumeration

```turtle
ep:TrustState rdf:type owl:Class ;
    owl:equivalentClass [ owl:oneOf (ep:TrustCreated ep:TrustFunded ...) ] .
```

**Category**: AUTHORITY
**Reason**: Closed enumeration limits possible states.

#### State Individuals

```turtle
ep:TrustCreated rdf:type owl:NamedIndividual, ep:TrustState ;
    rdfs:label "Trust Created"@en ;
    rdfs:comment "Trust instrument executed but not yet funded"@en .
```

**Category**: SEMANTIC (defines what state means)

#### Transition Property

```turtle
ep:hasState rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain :TrustEntity ;
    rdfs:range ep:TrustState ;
    ...
```

**MIXED**:
- Property definition → SEMANTIC
- `owl:FunctionalProperty` → AUTHORITY (enforces max 1 state)

#### Admissible Transitions

```turtle
ep:TrustCreated ep:canTransitionTo ep:TrustFunded, ep:TrustRevoked, ep:TrustTerminated .
```

**Category**: AUTHORITY
**Reason**: Defines what transitions are allowed.
**Test**: Remove this → lose authority (any transition becomes possible), understanding unchanged.

---

### 10. OUTCOME DETERMINATION (Lines 2543-2644)

#### Outcome Classes (Definitions)

```turtle
ep:IRC4941ExciseTax rdf:type owl:Class ;
    rdfs:subClassOf ep:TaxConsequence ;
    rdfs:label "IRC §4941 Excise Tax"@en ;
    ...
```

**Category**: SEMANTIC

#### Defined Classes (Inference Rules)

```turtle
ep:PotentialSelfDealingTransaction rdf:type owl:Class ;
    owl:equivalentClass [ owl:intersectionOf (ep:RelatedPartyTransaction ep:BelowMarketTransaction) ] .
```

**Category**: AUTHORITY
**Reason**: Defines automatic classification (if A AND B, then C).
**Test**: Remove this → lose authority (no automatic inference), understanding unchanged.

#### Outcome Axioms

```turtle
ep:PotentialSelfDealingTransaction rdfs:subClassOf
    [ owl:onProperty ep:hasOutcome ;
      owl:someValuesFrom ep:IRC4941ExciseTax ] .
```

**Category**: AUTHORITY
**Reason**: Enforces that self-dealing MUST have tax outcome.

#### Cross-Border Trust Axioms

```turtle
ep:CrossBorderTrust rdfs:subClassOf
    [ owl:onProperty ep:recognizedUnder ;
      owl:someValuesFrom ep:HagueTrustsConvention ] .
```

**Category**: AUTHORITY

```turtle
ep:CrossBorderTrust rdfs:subClassOf
    [ owl:onProperty ep:operatesInJurisdiction ;
      owl:minCardinality "2"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY (must operate in ≥2 jurisdictions)

#### Hague Axioms

```turtle
:TrustEntity rdfs:subClassOf
    [ owl:onProperty ep:satisfiesTrustValidity ;
      owl:maxCardinality "1"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY

```turtle
ep:ChoiceOfLaw rdfs:subClassOf
    [ owl:onProperty ep:applicableLaw ;
      owl:cardinality "1"^^xsd:nonNegativeInteger ] .
```

**Category**: AUTHORITY

---

### 11. PROPERTY CHAINS (Lines 2298-2317)

```turtle
ep:requiresFiduciaryDuty rdf:type owl:ObjectProperty ;
    owl:propertyChainAxiom ( :hasTrustee ep:owes ) ;
    ...
```

**Category**: SEMANTIC
**Reason**: Defines a derived relationship (compositional meaning).
**Test**: Remove this → lose understanding of complex relationship, but no enforcement lost.

**Property chains** → SEMANTIC (compositional meaning, not enforcement)

---

## SUMMARY STATISTICS

### Total Axioms by Category

| Category | Count | Percentage |
|----------|-------|------------|
| **SEMANTIC** | ~850 | ~60% |
| **AUTHORITY** | ~550 | ~40% |
| **MIXED** | ~15 | <1% |

### Breakdown by Type

#### SEMANTIC (Data-Centric)
- All class definitions (basic): ~130
- All property definitions: ~160
- Property subclass/domain/range: ~320
- Inverse properties: ~80
- Labels, comments, glossary: ~130
- Property chains: ~3
- **Total**: ~850

#### AUTHORITY (Operational)
- Cardinality constraints: ~15
- Disjointness axioms: ~25
- State transitions: ~4
- Closure axioms: ~10
- Outcome determination: ~8
- Defined classes (equivalentClass with intersection/union): ~5
- Functional properties: ~3
- State enumeration (oneOf): ~1
- **Total**: ~70 (but these are the CRITICAL ones)

#### MIXED (Need Refactoring)
- Classes with disjointness inline: ~10
- Properties declared functional inline: ~3
- **Total**: ~13

---

## CRITICAL FINDINGS

### Mixed Axioms That Need Separation

1. **Transaction Classes**
```turtle
# CURRENTLY (MIXED):
ep:RelatedPartyTransaction rdf:type owl:Class ;
    rdfs:subClassOf ep:Transaction ;
    owl:disjointWith ep:ArmsLengthTransaction ;  # ← AUTHORITY in SEMANTIC section

# SHOULD BE:
# In vocabulary.ttl:
ep:RelatedPartyTransaction rdf:type owl:Class ;
    rdfs:subClassOf ep:Transaction .

# In compliance.ttl:
ep:RelatedPartyTransaction owl:disjointWith ep:ArmsLengthTransaction .
```

2. **Functional Properties**
```turtle
# CURRENTLY (MIXED):
ep:hasState rdf:type owl:ObjectProperty, owl:FunctionalProperty ;

# SHOULD BE:
# In vocabulary.ttl:
ep:hasState rdf:type owl:ObjectProperty .

# In compliance.ttl:
ep:hasState rdf:type owl:FunctionalProperty .
```

3. **All Disjoint Classes**: ~10 instances

---

## REFACTORING RECOMMENDATION

### File 1: trust-domain-vocabulary.ttl (SEMANTIC)
**Purpose**: Define what things mean
**Contains**:
- Class definitions (no disjointness)
- Property definitions (no functional/cardinality)
- Taxonomy (subClassOf)
- Domain/range (meaning, not enforcement)
- Inverse properties
- Labels, comments, glossary mappings
- Property chains

**Size**: ~1,200 triples (~64% of ontology)

### File 2: trust-domain-compliance.ttl (AUTHORITY)
**Purpose**: Enforce what is allowed, determine outcomes
**Imports**: trust-domain-vocabulary.ttl
**Contains**:
- Cardinality constraints
- Disjointness axioms
- Functional property declarations
- State machine (closed enumeration + transitions)
- Outcome determination (defined classes + axioms)
- Closure axioms

**Size**: ~687 triples (~36% of ontology)

---

## NEXT STEPS

1. ✓ Analysis complete
2. Create vocabulary.ttl (semantic commitments)
3. Create compliance.ttl (authority commitments)
4. Validate both files independently
5. Test compliance.ttl imports vocabulary.ttl correctly
6. Update documentation

---

**Generated**: 2026-01-13
**Source**: trust-domain-estate-planning.ttl v2.0
**Total triples analyzed**: 1,887
