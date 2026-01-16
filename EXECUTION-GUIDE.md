# Execution Guide: Complete Technology Stack

This guide shows you exactly how to execute the complete ontology-driven trust compliance system.

## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Authorship** | Claude AI | Ontology design, documentation |
| **Interpretation** | Owlready2 + rdflib | OWL reasoning + SPARQL queries |
| **Memory** | RDF Knowledge Graph | Persistent triple store |
| **Visualization** | Mermaid | State machines, flows, diagrams |
| **Exploration** | Neo4j | Graph analytics, hypotheticals |
| **Version Control** | GitHub | Change tracking, review, rollback |

---

## Prerequisites

### 1. Install Python 3.8+

```bash
# Check version
python3 --version

# If not installed, download from: https://www.python.org/downloads/
```

### 2. Install Python Libraries

```bash
# Install required packages
pip install rdflib owlready2 neo4j

# Verify installation
python3 -c "import rdflib, owlready2, neo4j; print('✓ All libraries installed')"
```

### 3. Install Neo4j (Choose One Option)

**Option A: Docker (Recommended - Easiest)**

```bash
# Pull Neo4j image
docker pull neo4j:latest

# Run Neo4j container
docker run \
    --name neo4j-trust \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/trustpassword \
    -d \
    neo4j:latest

# Verify it's running
docker ps | grep neo4j
```

**Option B: Neo4j Desktop**

1. Download from: https://neo4j.com/download/
2. Install Neo4j Desktop
3. Create new project: "Trust Domain"
4. Create database with password: `trustpassword`
5. Start the database

**Option C: Neo4j Community Edition (Linux/Mac)**

```bash
# Download and extract
wget https://neo4j.com/artifact.php?name=neo4j-community-5.x.x-unix.tar.gz
tar -xzf neo4j-community-5.x.x-unix.tar.gz
cd neo4j-community-5.x.x

# Set password
bin/neo4j-admin set-initial-password trustpassword

# Start Neo4j
bin/neo4j start

# Verify
curl http://localhost:7474
```

### 4. Clone Repository

```bash
git clone https://github.com/dalaun/Finch-Dagen-Foundation.git
cd Finch-Dagen-Foundation
```

---

## Execution Steps

### Step 1: Run Complete Workflow

This single script executes the entire stack:

```bash
# Make script executable
chmod +x scripts/complete_workflow.py

# Run complete workflow
python3 scripts/complete_workflow.py
```

**What it does:**
1. ✅ Loads ontology with Owlready2 (TBox)
2. ✅ Runs Pellet reasoner for inference
3. ✅ Creates instance data with rdflib (ABox)
4. ✅ Builds RDF Knowledge Graph (memory)
5. ✅ Runs SPARQL compliance queries
6. ✅ Exports to Neo4j for exploration

**Expected output:**

```
===============================================================================
TRUST DOMAIN ONTOLOGY - COMPLETE WORKFLOW
===============================================================================

[1/6] Loading ontology with Owlready2...
  ✓ Loaded compliance ontology
  ✓ Classes: 131
  ✓ Properties: 160

[2/6] Running OWL reasoner...
  ✓ Reasoning complete - inferences materialized

[3/6] Creating instance data with rdflib...
  ✓ Created instance data: 10 triples
  ✓ Saved to: instances/example-trust.ttl

[4/6] Building RDF Knowledge Graph...
  ✓ Loaded ontology: 1891 triples
  ✓ Merged instances: 1901 total triples
  ✓ Saved knowledge graph: knowledge-graph.ttl

[5/6] Running SPARQL queries...
  Query: Find all trusts
    → Trust: SmithFamilyTrust, State: TrustActive

  Query: Find below-market transactions
    → Transaction: Transaction001
       Value: $100000, FMV: $200000
       ⚠ Potential IRC §4941 self-dealing!

[6/6] Exporting to Neo4j for exploration...
  ✓ Exported to Neo4j
  ✓ Open Neo4j Browser: http://localhost:7474
  ✓ Run Cypher: MATCH (n) RETURN n LIMIT 25

===============================================================================
WORKFLOW COMPLETE!
===============================================================================
```

### Step 2: Explore in Neo4j Browser

```bash
# Open Neo4j Browser
open http://localhost:7474
# Or manually navigate to: http://localhost:7474
```

**Login:**
- Username: `neo4j`
- Password: `trustpassword`

**Try these Cypher queries:**

```cypher
// View all nodes and relationships
MATCH (n) RETURN n LIMIT 25

// Find all trusts
MATCH (t:Resource)-[:type]->(c {name: 'TrustEntity'}) RETURN t

// Find transaction paths
MATCH p=(tx)-[:transactionBy|transactionWith*1..3]-(n)
RETURN p

// Find below-market transactions (potential self-dealing)
MATCH (tx:Resource)-[:type]->(t {name: 'Transaction'})
WHERE toFloat(tx.transactionValue) < toFloat(tx.fairMarketValue)
RETURN tx

// Authority cascade path traversal
MATCH path=(spend)-[:manifestsIn]->()-[:necessitatedBy]->()
           -[:requiresFor]->()-[:authorizedBy]->()-[:hasPurpose]->(mission)
RETURN path
```

### Step 3: Generate Mermaid Diagrams

```bash
# Generate all diagrams
python3 scripts/generate_diagrams.py
```

**Output files:**
- `diagrams/trust-state-machine.md` - Trust lifecycle
- `diagrams/transaction-classification.md` - IRC §4941 detection
- `diagrams/authority-cascade.md` - Spend validation
- `diagrams/technology-stack.md` - Architecture overview

**View diagrams:**

1. **On GitHub**: Push to repository, diagrams render automatically
2. **Locally**: Use VS Code with Markdown Preview Mermaid extension
3. **Online**: Copy diagram code to https://mermaid.live/

### Step 4: Run Custom SPARQL Queries

```bash
# Open Python interactive shell
python3
```

```python
from rdflib import Graph

# Load knowledge graph
kg = Graph()
kg.parse("knowledge-graph.ttl", format="turtle")

# Custom query: Find all IRC §4941 violations
query = """
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?tx ?grantor ?trust ?value ?fmv WHERE {
    ?tx a ep:Transaction ;
        ep:transactionBy ?grantor ;
        ep:transactionWith ?trust ;
        ep:transactionValue ?value ;
        ep:fairMarketValue ?fmv .

    FILTER(?value < ?fmv)
}
"""

results = kg.query(query)
for row in results:
    print(f"Self-dealing: {row.tx}")
    print(f"  Grantor: {row.grantor}")
    print(f"  Trust: {row.trust}")
    print(f"  Below market: ${row.value} < ${row.fmv}")
```

### Step 5: Run Hypothetical Scenarios (Neo4j)

**Scenario: What if we change a transaction value?**

```cypher
// Find a transaction
MATCH (tx:Resource {name: 'Transaction001'})
RETURN tx

// Change the value (hypothetical)
MATCH (tx:Resource {name: 'Transaction001'})
SET tx.transactionValue = '250000'  // Now ABOVE market!

// Check if it's still self-dealing
MATCH (tx:Resource {name: 'Transaction001'})
WHERE toFloat(tx.transactionValue) < toFloat(tx.fairMarketValue)
RETURN count(tx) as self_dealing_count
// Returns 0 - no longer self-dealing!

// Rollback: reset to original value
MATCH (tx:Resource {name: 'Transaction001'})
SET tx.transactionValue = '100000'
```

**Scenario: Find all possible authority cascade paths**

```cypher
// Find all paths from spend to mission
MATCH path=shortestPath(
    (spend:Resource)-[*]-(mission:Resource {name: 'FoundationMission'})
)
RETURN path
```

---

## Advanced Usage

### Export RDF to Different Formats

```bash
python3 -c "
from rdflib import Graph
g = Graph()
g.parse('knowledge-graph.ttl', format='turtle')

# Export to JSON-LD
g.serialize('knowledge-graph.jsonld', format='json-ld')

# Export to N-Triples
g.serialize('knowledge-graph.nt', format='nt')

# Export to RDF/XML (for Protégé)
g.serialize('knowledge-graph.owl', format='xml')

print('✓ Exported to multiple formats')
"
```

### Load in Protégé (Visual Ontology Editor)

1. Download Protégé: https://protege.stanford.edu/
2. Open Protégé
3. File → Open → Select `trust-domain-compliance.ttl`
4. Reasoner → Pellet
5. Start reasoner
6. View inferences in "Inferred" tabs

### Run Standalone Neo4j Export

```bash
# Export any RDF file to Neo4j
python3 scripts/export_to_neo4j.py knowledge-graph.ttl
```

### Add Your Own Trust Instances

Create `instances/my-trust.ttl`:

```turtle
@prefix ep: <http://example.org/trust-domain/estate-planning#> .
@prefix td: <http://example.org/trust-domain#> .
@prefix ex: <http://example.org/instances#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:MyFamilyTrust a td:TrustEntity ;
    ep:hasState ep:TrustActive ;
    ep:hasGrantor ex:MyGrantor ;
    rdfs:label "My Family Trust" .

ex:MyGrantor a ep:Grantor ;
    rdfs:label "John Doe" .

ex:MyTransaction a ep:Transaction ;
    ep:transactionBy ex:MyGrantor ;
    ep:transactionWith ex:MyFamilyTrust ;
    ep:transactionValue "50000"^^xsd:decimal ;
    ep:fairMarketValue "100000"^^xsd:decimal .
```

Then load it:

```python
from rdflib import Graph

kg = Graph()
kg.parse("trust-domain-compliance.ttl", format="turtle")
kg.parse("instances/my-trust.ttl", format="turtle")

# Query your trust
query = """
SELECT ?trust ?state WHERE {
    ?trust a <http://example.org/trust-domain#TrustEntity> ;
           <http://example.org/trust-domain/estate-planning#hasState> ?state .
}
"""
for row in kg.query(query):
    print(row)
```

---

## Troubleshooting

### Issue: Owlready2 can't load TTL

**Solution**: Convert to RDF/XML first

```python
from rdflib import Graph

# Convert TTL → RDF/XML
g = Graph()
g.parse("trust-domain-compliance.ttl", format="turtle")
g.serialize("trust-domain-compliance.owl", format="xml")

# Load with Owlready2
from owlready2 import *
onto = get_ontology("file://trust-domain-compliance.owl").load()
```

### Issue: Neo4j connection refused

**Solution**: Check Neo4j is running

```bash
# Docker
docker ps | grep neo4j

# If not running, start it
docker start neo4j-trust

# Or run a new container
docker run --name neo4j-trust -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/trustpassword -d neo4j:latest
```

### Issue: Pellet reasoner takes too long

**Solution**: Use HermiT or ELK instead

```python
from owlready2 import *

onto = get_ontology("file://trust-domain-compliance.ttl").load()

# Try HermiT (faster)
with onto:
    sync_reasoner_hermit()

# Or ELK (fastest, but less complete)
with onto:
    sync_reasoner_elk()
```

### Issue: Mermaid diagrams don't render

**Solutions**:
1. **GitHub**: Diagrams auto-render in `.md` files
2. **VS Code**: Install "Markdown Preview Mermaid Support" extension
3. **Online**: Copy code to https://mermaid.live/

---

## Next Steps

1. **Add your own trust data** to `instances/`
2. **Run compliance queries** to validate authority cascade
3. **Explore scenarios** in Neo4j Browser
4. **Generate reports** from SPARQL query results
5. **Commit changes** to GitHub for version control

---

## Quick Reference Commands

```bash
# Full workflow
python3 scripts/complete_workflow.py

# Generate diagrams
python3 scripts/generate_diagrams.py

# Export to Neo4j
python3 scripts/export_to_neo4j.py knowledge-graph.ttl

# Open Neo4j Browser
open http://localhost:7474

# Start Neo4j (Docker)
docker start neo4j-trust

# Stop Neo4j (Docker)
docker stop neo4j-trust

# View logs (Docker)
docker logs neo4j-trust
```

---

## File Structure After Execution

```
/
├── trust-domain-vocabulary.ttl         # Semantic layer (authored by Claude)
├── trust-domain-compliance.ttl         # Authority layer (authored by Claude)
├── instances/
│   ├── example-trust.ttl               # Generated by workflow
│   └── my-trust.ttl                    # Your custom instances
├── diagrams/
│   ├── trust-state-machine.md          # Generated by generate_diagrams.py
│   ├── transaction-classification.md
│   ├── authority-cascade.md
│   └── technology-stack.md
├── scripts/
│   ├── complete_workflow.py            # Main execution script
│   ├── export_to_neo4j.py              # Neo4j export utility
│   └── generate_diagrams.py            # Mermaid diagram generator
├── knowledge-graph.ttl                 # Combined RDF graph (memory)
└── EXECUTION-GUIDE.md                  # This file
```

---

**You now have a complete ontology-driven trust compliance system running!** 🎉

- **Claude**: Authored the dual-ontology architecture ✅
- **Owlready2**: Reasoning and inference ✅
- **rdflib**: SPARQL queries and instance data ✅
- **RDF Knowledge Graph**: Persistent memory ✅
- **Neo4j**: Graph exploration and hypotheticals ✅
- **Mermaid**: Visual diagrams ✅
- **GitHub**: Version control ✅
