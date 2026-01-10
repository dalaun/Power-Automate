# Ontology Properties

[← Back to Home](Home.md) | [Classes](Classes.md)

## Object Properties

### Authority Cascade Properties

The traceable chain from mission to spend:

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **legitimizes** | Purpose | Authority | Mission/purpose legitimizes exercise of authority |
| **authorizes** | Purpose | AuthorizedActivity | Purpose domain authorizes specific activities |
| **requires** | AuthorizedActivity | OperatorInRole | Activity requires operators in specific roles |
| **necessitates** | OperatorInRole | ExpenseDomain | Operator necessitates expense domains (enablement) |
| **manifestsAs** | ExpenseDomain | ActualSpend | Expense domain manifests as actual spend |
| **tracesBackTo** | ActualSpend | Purpose | Spend traces back to purpose (CLOSES THE LOOP) |

**The complete cascade**: Mission → Purpose → Activity → Operator → Expense → Spend → Purpose ✓

### Supporting Cascade Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **performedBy** | AuthorizedActivity | OperatorInRole | Activity performed by operator |
| **servesActivity** | OperatorInRole | AuthorizedActivity | Operator serves activity |
| **sustains** | ExpenseDomain | OperatorInRole | Expense domain sustains operator capability |

### Core Framework Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **exercisesAuthority** | TrustEntity | Authority | Trust exercises authority |
| **hasPurpose** | TrustEntity | Purpose | Trust has purpose (REQUIRED) |
| **hasSubPurpose** | Purpose | Purpose | Purpose composed of sub-purposes |
| **advancesPurpose** | OperationalActivity | Purpose | Activity advances purpose |
| **implementedBy** | Purpose | Instrument | Purpose implemented by instruments |

### Keystone Constraint Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **isIncidentalTo** | PrivateEnablement | Purpose | Enablement incidental to purpose (TEST 1) |
| **isInseparableFrom** | PrivateEnablement | OperationalActivity | Enablement inseparable from execution (TEST 2) |
| **enablesPrivately** | Instrument | PrivateEnablement | Instrument provides private enablement |
| **satisfiesKeystoneConstraint** | PrivateEnablement | KeystoneConstraint | Enablement satisfies both tests |
| **violatesKeystoneConstraint** | PrivateEnablement | KeystoneConstraint | Enablement violates constraint |

### Evidence & Validation Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **substantiatedBy** | Instrument | Evidence | Instrument substantiated by evidence |
| **governedBy** | Instrument | DoctrinalSource | Doctrinal source governs instrument |
| **requiresEvidence** | Instrument | EvidenceDiscipline | Instrument requires evidence discipline |

### Trust Structure Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasBeneficiary** | TrustStructure | Beneficiary | Trust has beneficiary |
| **hasTrustee** | TrustStructure | Trustee | Trust has trustee |
| **hasProtector** | TrustStructure | Protector | Trust has protector |

### Non-Grantor Trust Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **retainsControlPower** | Grantor | ControlPower | Grantor retains control power (→ grantor trust) |
| **lacksRetainedControl** | NonGrantorTrustSystem | ControlPower | Trust lacks control powers (crossed gateway) |
| **computesDNI** | NonGrantorTrustSystem | DistributableNetIncome | Trust computes DNI |
| **makesDistribution** | NonGrantorTrustSystem | Distribution | Trust makes distribution |
| **flowsCharacterThrough** | Distribution | CharacterFlowThrough | Distribution carries income character |
| **requiresFiling** | NonGrantorTrustSystem | FiduciaryReturn | Trust must file fiduciary return |

### Jurisdictional Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **passesJurisdictionalTest** | TrustStructure | JurisdictionalTest | Trust satisfies court/control tests |

### Operational Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **employs** | TrustEntity | HumanCapability | Trust employs human capability |
| **controls** | TrustEntity | Asset | Trust controls asset |
| **incurs** | TrustEntity | Expenditure | Trust incurs expenditure |
| **withinBoundary** | OperationalActivity | OperatingBoundary | Activity within operating boundary |

### System Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasSystemIdentifier** | TrustEntity | SystemIdentifier | Trust has system identifier (EIN) |

### Temporal Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **occursDuring** | ActualSpend | TemporalPeriod | Expenditure occurs during temporal period |
| **computedFor** | DistributableNetIncome | FiscalYear | DNI computed for specific fiscal year |
| **hasTemporalExtent** | OperationalActivity | TemporalPeriod | Activity spans temporal period |

### Grantmaking Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **makesGrant** | TrustEntity | Grant | Trust entity makes charitable grant |
| **receivesGrant** | Grantee | Grant | Grantee receives grant from trust |
| **satisfiesQualifyingDistribution** | Grant | QualifyingDistribution | Grant counts toward qualifying distribution (IRC §4942) |

### Safeguard Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **preventsMisuse** | SafeguardMechanism | AuthorityCollapse | Safeguard prevents authority collapse |

### IRC §§4941-4945 Safeguard Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **involvesDisqualifiedPerson** | Transaction | DisqualifiedPerson | Transaction involves disqualified person (IRC §4941) |
| **constitutesExcessBenefit** | Transaction | ExcessBenefit | Transaction provides excess benefit |
| **jeopardizesMission** | Investment | Purpose | Investment jeopardizes mission (IRC §4944) |
| **hasOwnershipPercentage** | Investment | xsd:decimal | Ownership percentage in business |
| **violatesSelfDealing** | Transaction | SelfDealingTransaction | Transaction violates self-dealing prohibition |
| **violatesExcessHolding** | Investment | ExcessBusinessHolding | Investment violates excess business holding limits |

---

## Data Properties

### Trust Classification Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **isRevocable** | TrustStructure | xsd:boolean | Trust is revocable |
| **isGrantorTrust** | TrustStructure | xsd:boolean | Trust is grantor trust |
| **isForeign** | TrustStructure | xsd:boolean | Trust is foreign |
| **isDomestic** | TrustStructure | xsd:boolean | Trust is domestic |

### Location Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **jurisdiction** | TrustStructure | xsd:string | Trust jurisdiction |
| **hasCourtJurisdiction** | TrustStructure | xsd:string | Court jurisdiction controlling trust |
| **hasControlLocation** | TrustStructure | xsd:string | Location of substantial decisions |

### Identification Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasEIN** | TrustEntity | xsd:string | Employer Identification Number |
| **establishedDate** | TrustStructure | xsd:date | Date trust established |

### Purpose Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasMissionStatement** | Purpose | xsd:string | Formal mission statement |
| **purposeDescription** | Purpose | xsd:string | Detailed purpose description |

### Operational Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasBusinessPurpose** | OperationalActivity | xsd:string | Business purpose of activity |

### Expense Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **isOrdinaryAndNecessary** | Expenditure | xsd:boolean | Expense is ordinary and necessary |
| **isCapitalExpense** | Expenditure | xsd:boolean | Expense is capital expenditure |

### Asset Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **hasUsefulLife** | Asset | xsd:integer | Useful life in years (depreciation) |

### Accounting Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **dniAmount** | DistributableNetIncome | xsd:decimal | DNI amount for tax year |

### Temporal Data Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **fiscalYearStart** | FiscalYear | xsd:date | Start date of fiscal year |
| **fiscalYearEnd** | FiscalYear | xsd:date | End date of fiscal year |
| **yearNumber** | FiscalYear | xsd:integer | Calendar year number |
| **expenditureDate** | ActualSpend | xsd:date | Date of expenditure |

### Grantmaking Data Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **grantAmount** | Grant | xsd:decimal | Dollar amount of grant |
| **minimumDistributionRequired** | FiscalYear | xsd:decimal | Minimum qualifying distributions required (IRC §4942) |
| **qualifyingDistributionsMade** | FiscalYear | xsd:decimal | Actual qualifying distributions made |

### Safeguard Data Properties (v4.0)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| **excessHoldingPercentage** | Investment | xsd:decimal | Percentage exceeding 20% limit |
| **transactionAmount** | Transaction | xsd:decimal | Dollar amount of transaction |

---

## Critical Property Chains

### The Authority Cascade Chain

```
:tracesBackTo ← :manifestsAs ← :necessitates ← :requires ← :authorizes
```

This chain connects ActualSpend back to Purpose through 5 intermediate relationships.

**Query pattern** to validate cascade:
```sparql
?spend :tracesBackTo ?purpose .

# Equivalent to traversing:
?spend ^:manifestsAs ?expenseDomain .
?expenseDomain ^:necessitates ?operator .
?operator ^:requires ?activity .
?activity ^:authorizes ?purpose .
```

### The Keystone Constraint Chain

```
PermissiblePrivateEnablement ⊆ (:isIncidentalTo some Purpose) ⊓ (:isInseparableFrom some OperationalActivity)
```

Both properties MUST be satisfied for enablement to be permissible.

---

**See Also**:
- [Classes](Classes.md)
- [Authority Cascade](Authority-Cascade.md)
- [Examples](Examples.md)
