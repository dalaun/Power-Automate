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

## Temporal Tracking Example (v4.0)

### Fiscal Year 2024 with Expenditures

```turtle
# Fiscal year with minimum distribution requirements
:FiscalYear2024 rdf:type :FiscalYear ;
    :fiscalYearStart "2024-01-01"^^xsd:date ;
    :fiscalYearEnd "2024-12-31"^^xsd:date ;
    :yearNumber "2024"^^xsd:integer ;
    :minimumDistributionRequired "500000.00"^^xsd:decimal ;
    :qualifyingDistributionsMade "625000.00"^^xsd:decimal ;
    rdfs:label "Fiscal Year 2024" .

# DNI computed for fiscal year
:DNI_2024 rdf:type :DistributableNetIncome ;
    :computedFor :FiscalYear2024 ;
    :dniAmount "750000.00"^^xsd:decimal ;
    rdfs:label "2024 DNI - $750,000" .

# Expenditure occurring during fiscal year
:SalaryPayment_DrSmith_January2024 rdf:type :ActualSpend ;
    :occursDuring :FiscalYear2024 ;
    :expenditureDate "2024-01-31"^^xsd:date ;
    :tracesBackTo :FoundationHealthMission ;
    rdfs:label "Dr. Smith Salary - January 2024 - $12,500" .

# Activity spanning fiscal year
:ClinicalTrialsActivity_2024 rdf:type :GrantmakingActivity ;
    :hasTemporalExtent :FiscalYear2024 ;
    :advancesPurpose :FoundationHealthMission .
```

**Key Features**:
- Fiscal year tracks minimum distribution requirement ($500K) vs actual ($625K) ✅
- DNI computed annually for tax compliance
- Expenditures linked to temporal periods via `occursDuring`
- Activities span fiscal years via `hasTemporalExtent`
- Enables time-series compliance queries

---

## Grantmaking Example (v4.0)

### Grant to Stanford Medicine

```turtle
# Public charity grantee
:StanfordMedicine rdf:type :PublicCharity ;
    rdfs:label "Stanford University School of Medicine" ;
    rdfs:comment "IRC §509(a) public charity - qualifying grantee" .

# Grant to advance health purpose
:GrantToStanfordMedicine rdf:type :Grant ;
    :grantAmount "250000.00"^^xsd:decimal ;
    :receivesGrant :StanfordMedicine ;
    :satisfiesQualifyingDistribution :QD_StanfordGrant ;
    rdfs:label "Grant to Stanford Medicine - $250,000" .

# Qualifying distribution for IRC §4942
:QD_StanfordGrant rdf:type :QualifyingDistribution ;
    rdfs:label "Qualifying Distribution: Stanford Grant" ;
    rdfs:comment "Counts toward $500K minimum distribution requirement" .

# Grantmaking activity (distinct from operations)
:GrantmakingActivity_Stanford rdf:type :GrantmakingActivity ;
    :advancesPurpose :FoundationHealthMission ;
    :hasTemporalExtent :FiscalYear2024 .

# Foundation makes the grant
:ExampleFoundationTrust :makesGrant :GrantToStanfordMedicine .
```

**Why Grantmaking is Distinct from Operations**:
- `GrantmakingActivity` is separate class from operational activities
- Grants to IRC §509(a) public charities automatically qualify
- Non-exempt grantees require expenditure responsibility
- Enables tracking qualifying distributions vs minimum requirements

---

## IRC §§4941-4945 Safeguard Examples (v4.0)

### Example: IRC §4941 Self-Dealing Violation

```turtle
# Disqualified person (substantial contributor)
:ExampleTrusteeAsDisqualifiedPerson rdf:type :SubstantialContributor ,
                                              :DisqualifiedPerson ;
    rdfs:label "Foundation Trustee (Disqualified Person)" .

# Self-dealing transaction
:ExampleSelfDealing rdf:type :SelfDealingTransaction ;
    :involvesDisqualifiedPerson :ExampleTrusteeAsDisqualifiedPerson ;
    :transactionAmount "100000.00"^^xsd:decimal ;
    rdfs:label "VIOLATION: Self-Dealing Transaction" ;
    rdfs:comment "Sale of property to disqualified person - IRC §4941 violation" .
```

**Result**: ❌ **VIOLATION** - Transaction with disqualified person triggers IRC §4941 self-dealing prohibition

### Example: IRC §4943 Excess Business Holding

```turtle
# Excess business holding (>20% ownership)
:ExampleExcessHolding rdf:type :ExcessBusinessHolding ;
    :hasOwnershipPercentage "35.0"^^xsd:decimal ;
    :excessHoldingPercentage "15.0"^^xsd:decimal ;
    rdfs:label "VIOLATION: Excess Business Holding (35%)" ;
    rdfs:comment "Ownership exceeds 20% limit - IRC §4943 violation" .
```

**Result**: ❌ **VIOLATION** - Holdings >20% violate IRC §4943 excess business holding limits

### Example: IRC §4944 Jeopardizing Investment

```turtle
# Jeopardizing investment
:ExampleJeopardizingInvestment rdf:type :JeopardizingInvestment ;
    :jeopardizesMission :FoundationHealthMission ;
    rdfs:label "VIOLATION: Jeopardizing Investment" ;
    rdfs:comment "Speculative investment endangering mission - IRC §4944 violation" .
```

**Result**: ❌ **VIOLATION** - Investment jeopardizes mission, prohibited by IRC §4944

### Example: IRC §4945 Taxable Expenditure

```turtle
# Lobbying expenditure
:ExampleLobbyingExpenditure rdf:type :LobbyingExpenditure ,
                                     :TaxableExpenditure ;
    :transactionAmount "50000.00"^^xsd:decimal ;
    rdfs:label "VIOLATION: Lobbying Expenditure" ;
    rdfs:comment "Expenditure for lobbying - IRC §4945 taxable expenditure" .

# Political expenditure
:ExamplePoliticalExpenditure rdf:type :PoliticalExpenditure ,
                                      :TaxableExpenditure ;
    :transactionAmount "25000.00"^^xsd:decimal ;
    rdfs:label "VIOLATION: Political Expenditure" ;
    rdfs:comment "Expenditure for political campaign - IRC §4945 taxable expenditure" .
```

**Result**: ❌ **VIOLATION** - Both are taxable expenditures prohibited by IRC §4945

**All violations are subclasses of `AuthorityCollapse`** and can be detected via disjoint class axioms.

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
