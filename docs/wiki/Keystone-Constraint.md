# The Keystone Constraint

[← Back to Home](Home.md) | [← Architecture](Architecture.md)

## The Fundamental Rule

> **Private enablement is permissible when and only when it is BOTH:**
> 1. **Incidental to** purpose-driven execution (not the primary purpose), AND
> 2. **Inseparable from** purpose-driven execution (necessarily coupled with mission advancement)

This constraint is the **fundamental boundary** between legitimate operations and private inurement.

## What is Private Enablement?

**Private enablement** = any benefit, compensation, or resource provided to private individuals:
- Employee salaries
- Contractor payments
- Health insurance and benefits
- Professional development
- Distributions to beneficiaries
- Any expenditure benefiting a private person

---

## The Two-Part Test

### Test 1: Incidentality

**Question**: Is the private enablement **incidental to** the purpose?

**Meaning**: The enablement serves the mission, not the person.

#### ✅ Passes Incidentality Test:
- Researcher salary to conduct health research
- Teacher salary to provide education
- Program director compensation to manage charitable programs
- **The purpose is the mission; compensation is how you achieve it**

#### ❌ Fails Incidentality Test:
- Luxury vacation unrelated to mission
- Personal expenses with no mission nexus
- Enrichment disguised as compensation
- **The enablement IS the purpose (enrichment)**

### Test 2: Inseparability

**Question**: Is the private enablement **inseparable from** execution?

**Meaning**: You cannot achieve the mission without this enablement.

#### ✅ Passes Inseparability Test:
- Researcher salary - cannot do research without researcher
- Health insurance - cannot retain qualified staff without benefits
- Professional development - cannot maintain expertise without training
- **Remove the enablement → execution stops**

#### ❌ Fails Inseparability Test:
- Excessive compensation - can achieve same result with reasonable compensation
- Lavish benefits - can retain staff with standard benefits
- Personal enrichment - separable from mission entirely
- **Remove the enablement → execution continues**

---

## The Formal Logic

```
PermissiblePrivateEnablement ⟺ (incidental ∧ inseparable)

Where:
  incidental = enablement serves purpose, not person
  inseparable = mission cannot be achieved without enablement
```

In OWL:

```turtle
:PermissiblePrivateEnablement rdf:type owl:Class ;
    rdfs:subClassOf :PrivateEnablement ,
        [ rdf:type owl:Restriction ;
          owl:onProperty :isIncidentalTo ;
          owl:minCardinality "1"^^xsd:nonNegativeInteger
        ] ,
        [ rdf:type owl:Restriction ;
          owl:onProperty :isInseparableFrom ;
          owl:minCardinality "1"^^xsd:nonNegativeInteger
        ] .
```

**Translation**: To be permissible, enablement MUST be incidental to at least one purpose AND inseparable from at least one operational activity.

---

## Examples

### ✅ Example 1: Research Scientist Compensation

**Scenario**: Foundation pays Dr. Smith $12,500/month to conduct clinical trials for cancer research.

**Test 1 - Incidental?**
- Purpose: Advance health through medical research
- Enablement: Dr. Smith's salary
- **Result**: ✅ Salary is incidental to health mission (serves research, not enrichment)

**Test 2 - Inseparable?**
- Activity: Conducting clinical trials
- Enablement: Qualified research scientist
- **Result**: ✅ Clinical trials cannot occur without qualified researcher

**Conclusion**: **PERMISSIBLE** - satisfies both tests

```turtle
:SalaryEnablement_DrSmith rdf:type :PermissiblePrivateEnablement ;
    :isIncidentalTo :FoundationHealthMission ;
    :isInseparableFrom :ClinicalTrialsActivity ;
    :satisfiesKeystoneConstraint :TheKeystoneConstraint .
```

### ✅ Example 2: Employee Health Insurance

**Scenario**: Foundation provides health insurance ($850/month) to research staff.

**Test 1 - Incidental?**
- Purpose: Advance health mission
- Enablement: Health benefits for staff
- **Result**: ✅ Benefits enable mission execution, not personal enrichment

**Test 2 - Inseparable?**
- Activity: Retaining qualified research staff
- Enablement: Competitive benefits package
- **Result**: ✅ Cannot sustain workforce capability without benefits

**Conclusion**: **PERMISSIBLE** - satisfies both tests

```turtle
:BenefitsEnablement_DrSmith rdf:type :PermissiblePrivateEnablement ;
    :isIncidentalTo :FoundationHealthMission ;
    :isInseparableFrom :ClinicalTrialsActivity ;
    :satisfiesKeystoneConstraint :TheKeystoneConstraint .
```

### ❌ Example 3: Trustee Luxury Vacation

**Scenario**: Trust pays $50,000 for trustee's luxury vacation unrelated to trust activities.

**Test 1 - Incidental?**
- Purpose: Charitable mission
- Enablement: Personal luxury vacation
- **Result**: ❌ Serves personal enjoyment, NOT mission

**Test 2 - Inseparable?**
- Activity: None - vacation unrelated to trust activities
- Enablement: Personal enrichment
- **Result**: ❌ Completely separable from any mission activity

**Conclusion**: **IMPROPER** - fails both tests → **PRIVATE INUREMENT**

```turtle
:ExampleImproperLavishExpense rdf:type :ImproperPrivateEnablement ;
    :violatesKeystoneConstraint :TheKeystoneConstraint .

:ImproperPrivateEnablement rdfs:subClassOf :PrivateInurement .
```

### ❌ Example 4: Excessive Compensation

**Scenario**: Foundation pays employee $500,000 for work with market rate of $150,000.

**Analysis**:
- Base compensation ($150,000): ✅ Incidental + inseparable = PERMISSIBLE
- Excess portion ($350,000):
  - Test 1: ❌ NOT incidental (serves enrichment)
  - Test 2: ❌ Separable (can achieve same result with market rate)

**Conclusion**: **EXCESS IS IMPROPER** - the separable portion violates keystone constraint

---

## The Disjoint Classes

**Critical axiom**:

```turtle
:PermissiblePrivateEnablement owl:disjointWith :ImproperPrivateEnablement .
```

**Meaning**: Private enablement is EITHER permissible OR improper - never both.

If it passes both tests → permissible
If it fails either test → improper → private inurement

---

## Connection to Authority Cascade

The keystone constraint is **proven** by the [Authority Cascade](Authority-Cascade.md):

```
If spend can trace:
  Actual Spend → Expense Domain → Operator in Role →
  Authorized Activity → Purpose

Then:
  - Incidental to purpose (traces back to mission)
  - Inseparable from execution (required for activity)

∴ Satisfies keystone constraint
```

**The cascade IS the proof mechanism for the keystone constraint.**

---

## Automated Validation

### SPARQL Query: Find Improper Enablement

```sparql
PREFIX : <http://example.org/trust-domain#>

SELECT ?enablement ?description WHERE {
  ?enablement rdf:type :PrivateEnablement .

  # Check if it's missing incidentality
  FILTER NOT EXISTS {
    ?enablement :isIncidentalTo ?purpose
  }

  OPTIONAL { ?enablement rdfs:comment ?description }
}
```

### SPARQL Query: Validate Permissibility

```sparql
PREFIX : <http://example.org/trust-domain#>

ASK {
  ?enablement rdf:type :PermissiblePrivateEnablement ;
              :isIncidentalTo ?purpose ;
              :isInseparableFrom ?activity .
}
```

Returns `true` if enablement satisfies both tests.

---

## Why This Matters

Traditional compliance question: "Is this expense reasonable?"

**This ontology asks**:
1. Does it serve purpose? (incidental)
2. Is it necessary for execution? (inseparable)

If YES to both → permissible
If NO to either → private inurement

**No ambiguity. No judgment calls. Testable constraint.**

---

**Next**: [The Authority Cascade →](Authority-Cascade.md)
