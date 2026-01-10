# Examples

[← Back to Home](Home.md)

This page shows concrete individuals from the ontology demonstrating permissible vs improper private enablement.

## Complete Authority Cascade Example

### Dr. Smith's Research Compensation

**The Scenario**: Foundation employs Dr. Smith as a research scientist to conduct clinical trials for novel cancer treatments.

**Compensation**: $12,500/month salary + $850/month health insurance

#### The Complete Traceable Chain

```turtle
# 1. MISSION
:FoundationMission rdf:type :CharitablePurpose ;
    :hasMissionStatement "Empowering lives through health, education, innovation, and opportunity" ;
    :hasSubPurpose :FoundationHealthMission .

# 2. PURPOSE DOMAIN
:FoundationHealthMission rdf:type :HealthPurpose ;
    :purposeDescription "Advancing health and wellness through medical research grants,
                        healthcare access programs, and public health initiatives" .

# 3. AUTHORIZED ACTIVITY
:ClinicalTrialsActivity rdf:type :AuthorizedActivity ;
    :advancesPurpose :FoundationHealthMission ;
    :requires :ResearchScientistDrSmith ;
    :performedBy :ResearchScientistDrSmith .

# 4. OPERATOR IN ROLE
:ResearchScientistDrSmith rdf:type :OperatorInRole ;
    :servesActivity :ClinicalTrialsActivity ;
    :necessitates :CompensationDomain_DrSmith ,
                  :BenefitsDomain_DrSmith .

# 5. EXPENSE DOMAINS
:CompensationDomain_DrSmith rdf:type :CompensationDomain ;
    :sustains :ResearchScientistDrSmith ;
    :manifestsAs :SalaryPayment_DrSmith_January2024 ;
    :enablesPrivately :SalaryEnablement_DrSmith .

:BenefitsDomain_DrSmith rdf:type :BenefitsDomain ;
    :sustains :ResearchScientistDrSmith ;
    :manifestsAs :HealthInsurance_DrSmith_January2024 ;
    :enablesPrivately :BenefitsEnablement_DrSmith .

# 6. ACTUAL SPEND
:SalaryPayment_DrSmith_January2024 rdf:type :ActualSpend ;
    :tracesBackTo :FoundationHealthMission ;
    rdfs:label "Actual Spend: Dr. Smith Salary (Jan 2024) - $12,500" .

:HealthInsurance_DrSmith_January2024 rdf:type :ActualSpend ;
    :tracesBackTo :FoundationHealthMission ;
    rdfs:label "Actual Spend: Dr. Smith Health Insurance (Jan 2024) - $850" .
```

#### Keystone Constraint Satisfaction

```turtle
# SALARY ENABLEMENT
:SalaryEnablement_DrSmith rdf:type :EmployeeCompensationEnablement ,
                                   :PermissiblePrivateEnablement ;
    :isIncidentalTo :FoundationHealthMission ;           # TEST 1: ✅
    :isInseparableFrom :ClinicalTrialsActivity ;        # TEST 2: ✅
    :satisfiesKeystoneConstraint :TheKeystoneConstraint .

# BENEFITS ENABLEMENT
:BenefitsEnablement_DrSmith rdf:type :OperationalBenefitEnablement ,
                                     :PermissiblePrivateEnablement ;
    :isIncidentalTo :FoundationHealthMission ;           # TEST 1: ✅
    :isInseparableFrom :ClinicalTrialsActivity ;        # TEST 2: ✅
    :satisfiesKeystoneConstraint :TheKeystoneConstraint .
```

#### Why It's Permissible

**Test 1 - Incidental to Purpose**:
- ✅ Purpose is advancing health through cancer research
- ✅ Salary serves the research mission, not personal enrichment
- ✅ Compensation is incidental to (enables) the health purpose

**Test 2 - Inseparable from Execution**:
- ✅ Clinical trials cannot be conducted without qualified researcher
- ✅ Cannot retain qualified researcher without competitive compensation
- ✅ Enablement is inseparable from mission execution

**Result**: ✅ **PERMISSIBLE** - Both tests satisfied

---

## Example: Improper Lavish Expense

### Trustee's Luxury Vacation

**The Scenario**: Trust pays $50,000 for trustee's luxury Caribbean vacation unrelated to trust activities.

```turtle
:ExampleImproperLavishExpense rdf:type :ImproperPrivateEnablement ;
    :violatesKeystoneConstraint :TheKeystoneConstraint ;
    rdfs:label "Example: Improper Lavish Personal Expense" ;
    rdfs:comment "Luxury vacation for trustee unrelated to mission activities." .
```

#### Why It's Improper

**Test 1 - Incidental to Purpose**:
- ❌ NO mission purpose served by personal vacation
- ❌ Serves personal enjoyment, not charitable purpose
- **FAILS TEST 1**

**Test 2 - Inseparable from Execution**:
- ❌ Vacation is completely separable from trust operations
- ❌ Can be removed without affecting mission execution
- **FAILS TEST 2**

**Result**: ❌ **IMPROPER** - Fails both tests → **PRIVATE INUREMENT**

#### The Failed Cascade

```
Attempted cascade:
1. Mission: "Empowering lives through..."
   ↓
2. Purpose Domain: ???
   ❌ NO PURPOSE SERVES PERSONAL LUXURY
   CASCADE BREAKS

:ExampleImproperLavishExpense
  :tracesBackTo ???
  ❌ CANNOT TRACE BACK TO PURPOSE
```

---

## Example: Excessive Compensation

### Above-Market Salary

**The Scenario**: Foundation pays employee $500,000 for work with market rate of $150,000.

```turtle
:ExampleImproperExcessCompensation rdf:type :ImproperPrivateEnablement ;
    :violatesKeystoneConstraint :TheKeystoneConstraint ;
    rdfs:label "Example: Improper Excessive Compensation" ;
    rdfs:comment "Compensation far exceeding market rate - the EXCESS portion
                  is separable and violates keystone constraint." .
```

#### Analysis

**Base Compensation ($150,000)**:
- ✅ Incidental to purpose (work advances mission)
- ✅ Inseparable from execution (need qualified employee)
- **Result**: PERMISSIBLE

**Excess Portion ($350,000)**:
- ❌ NOT incidental to purpose (serves enrichment)
- ❌ Separable from execution (same work achievable at market rate)
- **Result**: IMPROPER → PRIVATE BENEFIT

**Conclusion**: Excess above market rate violates keystone constraint.

---

## Foundation Trust Example

### Complete Trust Structure

```turtle
:ExampleFoundationTrust rdf:type :ForeignPrivateIrrevocableNonGrantorTrust ;
    # Classification
    :isRevocable "false"^^xsd:boolean ;
    :isGrantorTrust "false"^^xsd:boolean ;
    :isForeign "true"^^xsd:boolean ;
    :isDomestic "false"^^xsd:boolean ;

    # Jurisdiction
    :jurisdiction "Nevis" ;
    :hasCourtJurisdiction "Nevis High Court" ;
    :hasControlLocation "Nevis" ;

    # Identification
    :establishedDate "2024-01-15"^^xsd:date ;
    :hasEIN "98-7654321" ;

    # Structure
    :hasTrustee :FoundationTrustee ;
    :hasPurpose :FoundationMission ;

    rdfs:label "Example Foundation Trust" ;
    rdfs:comment "Foreign private irrevocable non-grantor trust operating as
                  a private foundation. Purpose legitimizes authority, which
                  enables deployment of instruments." .
```

**Key Features**:
- Crossed IRC §§671-679 gateway (no retained control)
- Operates under IRC §§641-685 (autonomous accounting)
- Classified under IRC §7701 (foreign jurisdiction)
- Mission-driven purpose (charitable)
- EIN system identifier (98-series for foreign trust)

---

## DNI and Distribution Example

```turtle
# Compute DNI for 2024
:ExampleDNI_2024 rdf:type :DistributableNetIncome ;
    :dniAmount "150000.00"^^xsd:decimal ;
    rdfs:label "2024 DNI" .

# Income distribution to beneficiary
:ExampleIncomeDistribution rdf:type :IncomeDistribution ;
    :flowsCharacterThrough :ExampleCharacterFlow .

# Character flows through to beneficiary
:ExampleCharacterFlow rdf:type :CharacterFlowThrough ;
    rdfs:label "Income character (ordinary, capital gain, etc.) flowing through" .
```

---

## The Four Sub-Purposes

```turtle
# HEALTH
:FoundationHealthMission rdf:type :HealthPurpose ;
    :purposeDescription "Advancing health and wellness through medical research
                        grants, healthcare access programs, and public health initiatives" .

# EDUCATION
:FoundationEducationMission rdf:type :EducationalPurpose ;
    :purposeDescription "Advancing education through scholarship programs,
                        educational technology, curriculum development, and teacher training" .

# INNOVATION
:FoundationInnovationMission rdf:type :InnovationPurpose ;
    :purposeDescription "Advancing innovation through scientific research grants,
                        technology development, and breakthrough discoveries" .

# OPPORTUNITY
:FoundationOpportunityMission rdf:type :OpportunityPurpose ;
    :purposeDescription "Advancing economic opportunity through workforce development,
                        entrepreneurship programs, and access to capital for underserved populations" .
```

---

## Doctrinal Source Examples

```turtle
# THE GATEWAY
:IRC_671_679 rdf:type :IRCSection ;
    rdfs:label "IRC §§671-679" ;
    rdfs:comment "Control-of-income boundary - determines who is the economic operator,
                  the gateway to non-grantor status" .

# THE OPERATING SYSTEM
:IRC_641_685 rdf:type :IRCSection ;
    rdfs:label "IRC §§641-685" ;
    rdfs:comment "Trust as autonomous accounting system - enables trust to retain income,
                  deploy expenses, distribute outputs with DNI and character flow-through" .

# THE JURISDICTION
:IRC_7701 rdf:type :IRCSection ;
    rdfs:label "IRC §7701" ;
    rdfs:comment "Jurisdictional identity - assigns which sovereign's rules apply
                  via court test and control test" .
```

---

**See Also**:
- [Authority Cascade](Authority-Cascade.md) - Understanding the traceable chain
- [Keystone Constraint](Keystone-Constraint.md) - The permissibility test
- [Usage Guide](Usage-Guide.md) - Querying these examples
