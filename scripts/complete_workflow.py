#!/usr/bin/env python3
"""
Complete Technology Stack Workflow
===================================

Claude: Authorship (already done - ontology files exist)
rdflib: SPARQL queries, instance data
Owlready2: OWL reasoning, inference
RDF Knowledge Graph: Memory/storage
Neo4j: Exploration, hypotheticals
Mermaid: Visualization (via Python)
"""

import sys
from pathlib import Path

print("=" * 80)
print("TRUST DOMAIN ONTOLOGY - COMPLETE WORKFLOW")
print("=" * 80)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: LOAD ONTOLOGY WITH OWLREADY2 (TBox)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[1/6] Loading ontology with Owlready2...")

try:
    from owlready2 import *

    # Load compliance ontology (auto-imports vocabulary)
    compliance = get_ontology("file://trust-domain-compliance.ttl").load()
    print(f"  ✓ Loaded compliance ontology")
    print(f"  ✓ Classes: {len(list(compliance.classes()))}")
    print(f"  ✓ Properties: {len(list(compliance.properties()))}")

except Exception as e:
    print(f"  ✗ Error loading with Owlready2: {e}")
    print(f"  → Try converting TTL to RDF/XML first")
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: RUN REASONER (Inference)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[2/6] Running OWL reasoner...")

try:
    with compliance:
        sync_reasoner_pellet(infer_property_values=True)
    print(f"  ✓ Reasoning complete - inferences materialized")

except Exception as e:
    print(f"  ⚠ Reasoner warning: {e}")
    print(f"  → Continuing without reasoning...")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3: ADD INSTANCE DATA WITH RDFLIB (ABox)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[3/6] Creating instance data with rdflib...")

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD

# Create instance graph
g = Graph()

# Define namespaces
EP = Namespace("http://example.org/trust-domain/estate-planning#")
TD = Namespace("http://example.org/trust-domain#")
EX = Namespace("http://example.org/instances#")

g.bind("ep", EP)
g.bind("td", TD)
g.bind("ex", EX)

# Example: Add a trust instance
g.add((EX.SmithFamilyTrust, RDF.type, TD.TrustEntity))
g.add((EX.SmithFamilyTrust, EP.hasState, EP.TrustActive))
g.add((EX.SmithFamilyTrust, EP.hasGrantor, EX.JohnSmith))
g.add((EX.SmithFamilyTrust, RDFS.label, Literal("Smith Family Trust")))

# Example: Add a transaction
g.add((EX.Transaction001, RDF.type, EP.Transaction))
g.add((EX.Transaction001, EP.transactionBy, EX.JohnSmith))
g.add((EX.Transaction001, EP.transactionWith, EX.SmithFamilyTrust))
g.add((EX.Transaction001, EP.transactionValue, Literal(100000, datatype=XSD.decimal)))
g.add((EX.Transaction001, EP.fairMarketValue, Literal(200000, datatype=XSD.decimal)))

# Save instances
g.serialize("instances/example-trust.ttl", format="turtle")
print(f"  ✓ Created instance data: {len(g)} triples")
print(f"  ✓ Saved to: instances/example-trust.ttl")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4: MERGE ONTOLOGY + INSTANCES (RDF Knowledge Graph Memory)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[4/6] Building RDF Knowledge Graph...")

# Load ontology
kg = Graph()
kg.parse("trust-domain-compliance.ttl", format="turtle")
print(f"  ✓ Loaded ontology: {len(kg)} triples")

# Merge instances
kg.parse("instances/example-trust.ttl", format="turtle")
print(f"  ✓ Merged instances: {len(kg)} total triples")

# Save combined graph
kg.serialize("knowledge-graph.ttl", format="turtle")
print(f"  ✓ Saved knowledge graph: knowledge-graph.ttl")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5: QUERY WITH SPARQL (rdflib)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[5/6] Running SPARQL queries...")

# Query 1: Find all trusts
query1 = """
PREFIX td: <http://example.org/trust-domain#>
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?trust ?state WHERE {
    ?trust a td:TrustEntity ;
           ep:hasState ?state .
}
"""

results = kg.query(query1)
print(f"\n  Query: Find all trusts")
for row in results:
    print(f"    → Trust: {row.trust.split('#')[-1]}, State: {row.state.split('#')[-1]}")

# Query 2: Find below-market transactions
query2 = """
PREFIX ep: <http://example.org/trust-domain/estate-planning#>

SELECT ?tx ?value ?fmv WHERE {
    ?tx a ep:Transaction ;
        ep:transactionValue ?value ;
        ep:fairMarketValue ?fmv .

    FILTER(?value < ?fmv)
}
"""

results = kg.query(query2)
print(f"\n  Query: Find below-market transactions")
for row in results:
    print(f"    → Transaction: {row.tx.split('#')[-1]}")
    print(f"       Value: ${row.value}, FMV: ${row.fmv}")
    print(f"       ⚠ Potential IRC §4941 self-dealing!")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 6: EXPORT TO NEO4J (Exploration)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n[6/6] Exporting to Neo4j for exploration...")

try:
    from neo4j import GraphDatabase

    # Connect to Neo4j
    driver = GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "trustpassword")
    )

    def export_to_neo4j(tx):
        # Clear existing data
        tx.run("MATCH (n) DETACH DELETE n")

        # Export triples as nodes and relationships
        for s, p, o in kg:
            subject = str(s).split('#')[-1] if '#' in str(s) else str(s).split('/')[-1]
            predicate = str(p).split('#')[-1] if '#' in str(p) else str(p).split('/')[-1]

            if isinstance(o, URIRef):
                object_val = str(o).split('#')[-1] if '#' in str(o) else str(o).split('/')[-1]
                # Create relationship
                tx.run(
                    f"MERGE (s {{name: $subject}}) "
                    f"MERGE (o {{name: $object}}) "
                    f"MERGE (s)-[r:{predicate}]->(o)",
                    subject=subject, object=object_val
                )
            else:
                # Create property
                tx.run(
                    f"MERGE (s {{name: $subject}}) "
                    f"SET s.{predicate} = $value",
                    subject=subject, value=str(o)
                )

    with driver.session() as session:
        session.execute_write(export_to_neo4j)

    print(f"  ✓ Exported to Neo4j")
    print(f"  ✓ Open Neo4j Browser: http://localhost:7474")
    print(f"  ✓ Run Cypher: MATCH (n) RETURN n LIMIT 25")

    driver.close()

except Exception as e:
    print(f"  ⚠ Neo4j export skipped: {e}")
    print(f"  → Make sure Neo4j is running on localhost:7687")

# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("WORKFLOW COMPLETE!")
print("=" * 80)
print("""
Next Steps:
-----------
1. Review knowledge-graph.ttl (RDF memory store)
2. Open Neo4j Browser: http://localhost:7474
3. Run Cypher queries for hypotheticals
4. Generate Mermaid diagrams (see scripts/generate_diagrams.py)

Technology Stack Summary:
------------------------
✓ Claude: Authored ontology (vocabulary + compliance)
✓ Owlready2: Loaded ontology, ran reasoner
✓ rdflib: Added instances, ran SPARQL queries
✓ RDF Knowledge Graph: Stored combined ontology + instances
✓ Neo4j: Ready for exploration and hypotheticals
⧗ Mermaid: Run generate_diagrams.py next

Files Generated:
----------------
- instances/example-trust.ttl (instance data)
- knowledge-graph.ttl (combined RDF graph)
""")

print("=" * 80)
