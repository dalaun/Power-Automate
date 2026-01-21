# Claude Cowork Task Specifications

## Session 1: CI/CD Pipeline Engineer

### Objective
Build complete GitHub Actions automation for the Trust Domain Ontology stack.

### Context
- Repository: https://github.com/dalaun/Finch-Dagen-Foundation
- Stack: Owlready2, rdflib, Neo4j, Mermaid
- Ontology files: trust-domain-vocabulary.ttl, trust-domain-compliance.ttl

### Tasks

#### 1.1 Ontology Validation Workflow
**File**: `.github/workflows/validate-ontology.yml`

**Triggers**: Push to main, pull requests
**Steps**:
- Install rdflib, owlready2
- Parse both .ttl files
- Run validate_separated.py
- Check for syntax errors
- Report validation status

#### 1.2 Test Execution Workflow
**File**: `.github/workflows/run-tests.yml`

**Triggers**: Push to main, pull requests
**Steps**:
- Install dependencies (pytest, rdflib, owlready2)
- Run pytest on tests/ directory
- Generate coverage report
- Upload results as artifact

#### 1.3 Neo4j Deployment Workflow
**File**: `.github/workflows/deploy-neo4j.yml`

**Triggers**: Manual (workflow_dispatch), release tags
**Steps**:
- Start Neo4j container
- Run export_to_neo4j.py
- Verify data loaded
- Health check endpoint

#### 1.4 Documentation Generation
**File**: `.github/workflows/generate-docs.yml`

**Triggers**: Push to docs/**, main branch
**Steps**:
- Run generate_diagrams.py
- Commit generated diagrams
- Sync to wiki (if WIKI_TOKEN available)

### Acceptance Criteria
- [ ] All 4 workflows created
- [ ] Workflows pass on test run
- [ ] Documentation for each workflow
- [ ] Badge integration for README

### Deliverables
- .github/workflows/*.yml (4 files)
- README.md updated with status badges
- WORKFLOWS.md documentation

---

## Session 2: Test Engineer

### Objective
Create comprehensive unit test suite for all Python scripts.

### Context
- Scripts: complete_workflow.py, export_to_neo4j.py, generate_diagrams.py
- Python utilities: extract_semantic.py, extract_authority.py, validate_separated.py

### Tasks

#### 2.1 Vocabulary Tests
**File**: `tests/test_vocabulary.py`

```python
def test_vocabulary_loads_correctly()
def test_vocabulary_has_no_functional_properties()
def test_vocabulary_has_no_disjointness()
def test_vocabulary_class_count()
def test_vocabulary_property_count()
```

#### 2.2 Compliance Tests
**File**: `tests/test_compliance.py`

```python
def test_compliance_loads_correctly()
def test_compliance_imports_vocabulary()
def test_compliance_has_functional_properties()
def test_compliance_has_disjointness()
def test_state_machine_transitions()
```

#### 2.3 Reasoner Tests
**File**: `tests/test_reasoner.py`

```python
def test_pellet_reasoner_runs()
def test_irc4941_detection()
def test_transaction_classification()
def test_state_transition_validation()
def test_inconsistency_detection()
```

#### 2.4 SPARQL Tests
**File**: `tests/test_sparql_queries.py`

```python
def test_find_all_trusts()
def test_find_below_market_transactions()
def test_authority_cascade_validation()
def test_compliance_check_queries()
```

#### 2.5 Neo4j Tests
**File**: `tests/test_neo4j_export.py`

```python
def test_neo4j_connection()
def test_export_creates_nodes()
def test_export_creates_relationships()
def test_cypher_queries()
```

### Test Infrastructure

#### 2.6 Test Fixtures
**File**: `tests/conftest.py`

- Pytest fixtures for ontology loading
- Mock Neo4j connection
- Sample trust instances
- Test data cleanup

#### 2.7 Test Data
**Directory**: `tests/fixtures/`

- sample-trust.ttl
- invalid-trust.ttl (for error testing)
- sample-transactions.ttl

### Acceptance Criteria
- [ ] 90%+ code coverage
- [ ] All scripts tested
- [ ] CI integration ready
- [ ] Fast execution (<30 seconds total)

### Deliverables
- tests/*.py (5+ test files)
- tests/conftest.py (fixtures)
- tests/fixtures/*.ttl (test data)
- pytest.ini (configuration)

---

## Session 3: API Engineer

### Objective
Build FastAPI REST service for ontology operations.

### Context
- Expose ontology operations via REST API
- Enable web applications to query trusts
- Support compliance checking
- Integrate with Neo4j

### Tasks

#### 3.1 API Server
**File**: `api/main.py`

```python
from fastapi import FastAPI

app = FastAPI(
    title="Trust Domain Ontology API",
    version="3.0.0"
)

# Endpoints:
# GET /api/v1/trusts - List all trusts
# GET /api/v1/trusts/{id} - Get trust details
# POST /api/v1/trusts - Create trust
# POST /api/v1/compliance/check - Run compliance check
# GET /api/v1/transactions/{id}/validate - Validate transaction
```

#### 3.2 Endpoint Implementation
**File**: `api/endpoints.py`

```python
@router.get("/trusts")
async def list_trusts():
    # SPARQL query to RDF KG

@router.post("/trusts")
async def create_trust(trust: TrustModel):
    # Add to RDF graph
    # Run reasoner
    # Return validation results

@router.post("/compliance/check")
async def check_compliance(trust_id: str):
    # Run SPARQL authority cascade query
    # Return compliance status
```

#### 3.3 Data Models
**File**: `api/models.py`

```python
from pydantic import BaseModel

class Trust(BaseModel):
    id: str
    state: str
    grantor: str
    beneficiaries: List[str]

class Transaction(BaseModel):
    id: str
    transaction_by: str
    transaction_with: str
    value: float
    fair_market_value: float

class ComplianceResult(BaseModel):
    compliant: bool
    violations: List[str]
    cascade_path: Optional[List[str]]
```

#### 3.4 Docker Deployment
**File**: `api/docker-compose.yml`

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
  neo4j:
    image: neo4j:latest
    ports:
      - "7474:7474"
      - "7687:7687"
```

### Acceptance Criteria
- [ ] RESTful API with OpenAPI docs
- [ ] CRUD operations for trusts
- [ ] Compliance checking endpoint
- [ ] Docker deployment ready
- [ ] API documentation

### Deliverables
- api/*.py (3+ files)
- api/Dockerfile
- api/docker-compose.yml
- api/requirements.txt
- API-DOCS.md

---

## Session 4: Performance Engineer

### Objective
Optimize reasoner performance, query execution, and Neo4j operations.

### Context
- Current: Pellet reasoner (may be slow on large datasets)
- Need: Benchmark, optimize, document performance characteristics

### Tasks

#### 4.1 Reasoner Benchmarking
**File**: `performance/benchmark_reasoners.py`

```python
# Compare: Pellet, HermiT, ELK
# Metrics: Load time, reasoning time, memory usage
# Dataset sizes: 100, 1000, 10000 triples
```

#### 4.2 SPARQL Optimization
**File**: `performance/optimize_sparql.py`

```python
# Profile slow queries
# Add indexes
# Rewrite queries for performance
# Cache frequently-used results
```

#### 4.3 Neo4j Optimization
**File**: `performance/optimize_neo4j.py`

```python
# Create indexes on key properties
# Optimize Cypher queries
# Batch import strategies
# Query plan analysis
```

#### 4.4 Caching Layer
**File**: `api/cache.py`

```python
# Redis caching for SPARQL results
# Invalidation strategy
# TTL configuration
```

### Acceptance Criteria
- [ ] Benchmark report comparing reasoners
- [ ] Optimized SPARQL queries
- [ ] Neo4j indexes created
- [ ] Performance documentation

### Deliverables
- performance/*.py (benchmark scripts)
- PERFORMANCE.md (optimization guide)
- Recommended configuration settings

---

## Session 5: Documentation Engineer

### Objective
Create interactive Jupyter notebooks and enhanced documentation.

### Context
- Make the stack accessible to non-programmers
- Provide step-by-step tutorials
- Interactive examples

### Tasks

#### 5.1 Getting Started Notebook
**File**: `notebooks/01-getting-started.ipynb`

```python
# Introduction to the dual-ontology architecture
# Load vocabulary and compliance ontologies
# Explore classes and properties
# Visual diagrams embedded
```

#### 5.2 Adding Trusts Notebook
**File**: `notebooks/02-adding-trusts.ipynb`

```python
# Create trust instances
# Add transactions
# Add participants
# Save to RDF graph
```

#### 5.3 Compliance Checking Notebook
**File**: `notebooks/03-compliance-checking.ipynb`

```python
# Run reasoner
# Check for IRC §4941 violations
# Validate authority cascade
# Generate compliance report
```

#### 5.4 Neo4j Exploration Notebook
**File**: `notebooks/04-neo4j-exploration.ipynb`

```python
# Export to Neo4j
# Cypher query examples
# Graph visualization
# What-if scenarios
```

#### 5.5 Video Tutorial Script
**File**: `docs/VIDEO-SCRIPT.md`

```markdown
# 10-minute walkthrough script
# Screen recording instructions
# Key talking points
```

### Acceptance Criteria
- [ ] 4+ interactive notebooks
- [ ] All cells execute successfully
- [ ] Clear explanations
- [ ] Visual outputs

### Deliverables
- notebooks/*.ipynb (4+ files)
- docs/TUTORIALS.md (index)
- docs/VIDEO-SCRIPT.md

---

## Coordination

### Main Session (You + Claude Orchestrator)

**Responsibilities**:
1. Launch 5 parallel Claude sessions
2. Provide each with their task spec
3. Review deliverables
4. Integrate all work
5. Final testing

### Timeline
- **Parallel execution**: 4 hours (all sessions working simultaneously)
- **Integration**: 1 hour
- **Testing**: 1 hour
- **Total**: 6 hours (vs 14+ hours sequential)

### Integration Order
1. CI/CD workflows (Session 1)
2. Unit tests (Session 2)
3. API (Session 3)
4. Performance optimizations (Session 4)
5. Documentation (Session 5)

---

## Expected Results

After Claude Cowork completion:

**Rating increase**: 9.8/10 → **10.0/10** ✅

**What gets added**:
- ✅ CI/CD automation (+0.1)
- ✅ Comprehensive tests (+0.1)
- ✅ REST API (bonus)
- ✅ Performance optimization (bonus)
- ✅ Interactive tutorials (bonus)

**Time saved**:
- Sequential: ~14 hours
- Parallel (5 Claudes): ~6 hours
- **Efficiency gain**: 58% faster

---

## How to Execute

### Option 1: Claude.ai Web (Manual)
1. Open 5 browser tabs/windows
2. Start new Claude conversation in each
3. Paste task spec into each
4. Download deliverables from each
5. Integrate locally

### Option 2: Claude API (Automated)
```python
# Orchestrator script
import anthropic

sessions = {
    "ci_cd": "Session 1 task spec...",
    "tests": "Session 2 task spec...",
    "api": "Session 3 task spec...",
    "performance": "Session 4 task spec...",
    "docs": "Session 5 task spec..."
}

results = {}
for name, task in sessions.items():
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4",
        max_tokens=8000,
        messages=[{"role": "user", "content": task}]
    )
    results[name] = message.content
```

### Option 3: Claude Code (Best)
- Use Claude Code's multi-agent Task tool
- Spawn 5 specialized agents in parallel
- Automatic file integration
- Git commit management

---

## Ready to Launch?

Want me to:
1. **Create all 5 task specs as separate .md files** (ready to copy/paste)
2. **Launch Session 1 (CI/CD) right now** in this session
3. **Create orchestrator script** for API-based parallel execution
4. **Something else**?

The stack is already 9.8/10 - these parallel sessions would push it to **10.0/10 perfection**! 🚀
