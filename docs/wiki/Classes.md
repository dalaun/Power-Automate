# Ontology Classes

[← Back to Home](Home.md)

## Core Class Hierarchy

### Trust Structures

```
TrustEntity
├── TrustStructure
│   ├── PrivateIrrevocableNonGrantorTrust
│   │   └── ForeignPrivateIrrevocableNonGrantorTrust
│   └── DomesticTrust
└── NonGrantorTrustSystem
```

**Key Classes**:

- **TrustEntity**: A trust operating as a system of authority
- **NonGrantorTrustSystem**: Trust that has crossed IRC §§671-679 gateway
- **ForeignPrivateIrrevocableNonGrantorTrust**: Foreign trust subject to IRC §7701

### Authority Framework

```
Authority
├── FiduciaryAuthority
└── EmployerAuthority

Purpose
├── ExemptPurpose
│   └── CharitablePurpose
│       ├── HealthPurpose
│       ├── EducationalPurpose
│       ├── InnovationPurpose
│       └── OpportunityPurpose
└── BusinessPurpose
```

### Operational Classes

```
OperationalActivity
├── AuthorizedActivity
└── TradeOrBusiness

OperatorInRole
Role
├── ResearchScientistRole
├── ProgramDirectorRole
└── EducatorRole
```

### Instruments & Expenditures

```
Instrument
├── CompensationInstrument
│   ├── FringeBenefit
│   └── WageInstrument
├── NonCashOperationalInstrument
├── MobilityInstrument
├── ReimbursementInstrument
├── CapabilityInvestmentInstrument
└── DepreciationInstrument

Expenditure
├── OrdinaryAndNecessaryExpense
├── CapitalExpenditure
├── IncomeProductionExpense
├── FiduciarySpecificExpense
└── ActualSpend
```

### Private Enablement

```
PrivateEnablement
├── PermissiblePrivateEnablement
│   ├── EmployeeCompensationEnablement
│   └── OperationalBenefitEnablement
└── ImproperPrivateEnablement (DISJOINT from Permissible)

ExpenseDomain (subclass of PrivateEnablement)
├── CompensationDomain
├── BenefitsDomain
├── ProfessionalDevelopmentDomain
└── OperationalSupportDomain
```

**Critical Axiom**:
```turtle
:PermissiblePrivateEnablement owl:disjointWith :ImproperPrivateEnablement .
```

### Constraints & Safeguards

```
SafeguardMechanism
├── KeystoneConstraint
│   ├── IncidentalityTest
│   └── InseparabilityTest
├── SelfDealingProhibition (IRC §4941)
├── MinimumDistributionRequirement (IRC §4942)
├── ExcessBusinessHoldingLimit (IRC §4943)
├── JeopardizingInvestmentRule (IRC §4944)
└── TaxableExpenditureProhibition (IRC §4945)

AuthorityCollapse
├── PrivateInurement
└── PrivateBenefit
```

### IRC §§4941-4945 Safeguards (v4.0 - Fully Axiomatized)

#### IRC §4941: Self-Dealing

```
DisqualifiedPerson
├── SubstantialContributor
├── FoundationManager
├── OwnerOfControlledEntity
└── FamilyMember

Transaction
├── SelfDealingTransaction (DISJOINT from Permitted)
│   └── [any transaction with DisqualifiedPerson]
└── PermittedTransaction

ExcessBenefit
```

**Axiom**: `SelfDealingTransaction` MUST involve `DisqualifiedPerson`

**Disjointness**: `PermittedTransaction owl:disjointWith SelfDealingTransaction`

#### IRC §4942: Minimum Distributions

Covered in [Grantmaking](#grantmaking-v40) section above.

- Foundation MUST make qualifying distributions
- Tracked via `minimumDistributionRequired` vs `qualifyingDistributionsMade`

#### IRC §4943: Excess Business Holdings

```
Investment
├── ExcessBusinessHolding (>20% ownership triggers violation)
└── PermittedBusinessHolding (DISJOINT from Excess)
```

**Axiom**: Holdings >20% constitute `ExcessBusinessHolding`

**Disjointness**: `PermittedBusinessHolding owl:disjointWith ExcessBusinessHolding`

#### IRC §4944: Jeopardizing Investments

```
Investment
├── JeopardizingInvestment (endangers mission)
└── PrudentInvestment (DISJOINT from Jeopardizing)
```

**Property**: `jeopardizesMission` links investment to purpose

**Disjointness**: `PrudentInvestment owl:disjointWith JeopardizingInvestment`

#### IRC §4945: Taxable Expenditures

```
TaxableExpenditure (subclass of AuthorityCollapse)
├── LobbyingExpenditure
├── PoliticalExpenditure
└── GrantWithoutExpenditureResponsibility
```

**All violations are subclasses of `AuthorityCollapse`**

### Doctrinal Sources

```
DoctrinalSource
├── InternalRevenueCode
│   └── IRCSection
│       ├── IRC_162 (operating boundary)
│       ├── IRC_212 (income production expenses)
│       ├── IRC_67e (fiduciary-specific expenses)
│       ├── IRC_671_679 (THE GATEWAY)
│       ├── IRC_641_685 (THE OPERATING SYSTEM)
│       ├── IRC_7701 (THE JURISDICTION)
│       ├── IRC_4941-4945 (safeguards)
│       └── [others...]
└── IRSPublication
    ├── Pub_15 (labor control-plane)
    ├── Pub_15B (fringe benefits)
    ├── Pub_463 (mobility)
    ├── Pub_535 (operational costs)
    ├── Pub_557 (exempt authority)
    ├── Pub_583 (system genesis)
    └── Pub_946 (asset time-binding)
```

### Trust Accounting

```
DistributableNetIncome (DNI)

Distribution
├── IncomeDistribution
└── CorpusDistribution

CharacterFlowThrough
```

### Temporal Dimension (v4.0)

```
TemporalPeriod
├── FiscalYear
├── Quarter
└── Month
```

**Key Classes**:

- **FiscalYear**: 12-month accounting period for DNI computation and distribution tracking
- **Quarter**: Quarterly period for tax estimation and interim reporting
- **Month**: Monthly period for operational tracking

**Temporal Properties**:

- `occursDuring`: Links expenditures to temporal periods
- `computedFor`: Links DNI to specific fiscal year
- `hasTemporalExtent`: Activities span temporal periods
- `fiscalYearStart`, `fiscalYearEnd`: Date boundaries for fiscal years
- `minimumDistributionRequired`, `qualifyingDistributionsMade`: IRC §4942 tracking

### Grantmaking (v4.0)

```
GrantmakingActivity (subclass of AuthorizedActivity)

Grant
└── ProgramRelatedInvestment

Grantee
├── PublicCharity (IRC §509(a))
└── NonExemptGrantee

QualifyingDistribution (IRC §4942)
```

**Key Classes**:

- **GrantmakingActivity**: Charitable grantmaking distinct from operations
- **Grant**: Charitable grant to advance exempt purpose
- **ProgramRelatedInvestment**: Investment primarily for charitable purpose
- **PublicCharity**: IRC §509(a) public charity (qualifying grantee)
- **NonExemptGrantee**: Grantee requiring expenditure responsibility
- **QualifyingDistribution**: Distribution counting toward minimum requirement

### Evidence & Validation

```
Evidence
├── PayrollRecords
├── BenefitPlan
├── BusinessRecords
├── TravelSubstantiation
├── AssetRecords
├── FiduciaryReturn
├── ScheduleK1
└── TrustAccounting

EvidenceDiscipline
└── AccountablePlan
```

### System Identifiers

```
SystemIdentifier
└── EIN (Employer Identification Number)
```

**Critical Axiom**:
```turtle
:EIN owl:disjointWith :Instrument .
:SystemIdentifier owl:disjointWith :Instrument .
```

EIN is NOT an instrument - it's a system identifier (MAC address analogy).

### Control Powers (IRC §§671-679)

```
ControlPower
├── ReversionaryInterest (IRC §673)
├── PowerToControlBeneficialEnjoyment (IRC §674)
├── AdministrativePower (IRC §675)
├── PowerToRevoke (IRC §676)
└── IncomeForGrantorBenefit (IRC §677)
```

If grantor retains ANY of these → Grantor Trust
If grantor retains NONE → Non-Grantor Trust (crosses the gateway)

### Jurisdictional Tests

```
JurisdictionalTest
├── CourtTest (can US court exercise primary supervision?)
└── ControlTest (do US persons control substantial decisions?)
```

Pass BOTH → Domestic Trust
Fail EITHER → Foreign Trust

---

## Key Restrictions

### Purpose Legitimizes Authority
```turtle
:TrustEntity rdfs:subClassOf
    [ owl:onProperty :hasPurpose ;
      owl:minCardinality "1" ] .
```

### Instruments Require Evidence
```turtle
:Instrument rdfs:subClassOf
    [ owl:onProperty :substantiatedBy ;
      owl:minCardinality "1" ] .
```

### Spend Must Trace to Purpose
```turtle
:ActualSpend rdfs:subClassOf
    [ owl:onProperty :tracesBackTo ;
      owl:minCardinality "1" ] .
```

---

**See Also**:
- [Properties](Properties.md)
- [Architecture](Architecture.md)
- [Examples](Examples.md)
