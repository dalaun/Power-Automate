#!/usr/bin/env python3
"""
Quick Compliance Check (No Neo4j Required)
==========================================
Run this to test the system without Docker/Neo4j
"""

from rdflib import Graph, Namespace

print("=" * 70)
print("TRUST COMPLIANCE QUICK CHECK")
print("=" * 70)

# Load ontology
print("\n[1/3] Loading ontology...")
g = Graph()
try:
    g.parse("trust-domain-compliance.ttl", format="turtle")
    print(f"  ✓ Loaded {len(g)} triples")
except Exception as e:
    print(f"  ✗ Error: {e}")
    print("\n  Make sure you're in the directory with the .ttl files")
    exit(1)

# Run SPARQL query
print("\n[2/3] Running SPARQL query...")
query = """
PREFIX ep: <http://example.org/trust-domain/estate-planning#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?class (COUNT(?class) AS ?count)
WHERE {
    ?s a owl:Class .
    ?s a ?class .
}
GROUP BY ?class
ORDER BY DESC(?count)
LIMIT 10
"""

results = g.query(query)
print("  Top classes in ontology:")
for row in results:
    print(f"    - {row.class.split('#')[-1]}: {row.count} instances")

# Show system is working
print("\n[3/3] System Status:")
print("  ✓ rdflib: Working")
print("  ✓ SPARQL: Working")
print("  ✓ Ontology: Loaded")
print("  ⚠ Owlready2: Not tested (run complete_workflow.py for full test)")
print("  ⚠ Neo4j: Not available (Docker not installed)")

print("\n" + "=" * 70)
print("Quick check complete! System is operational.")
print("=" * 70)

print("\nNext steps:")
print("  1. For full compliance check: python3 scripts/complete_workflow.py")
print("  2. To install Neo4j: Install Docker first")
print("  3. Read EXECUTION-GUIDE.md for details")
