#!/usr/bin/env python3
"""
Export RDF Knowledge Graph to Neo4j Property Graph
===================================================

Usage:
    python export_to_neo4j.py knowledge-graph.ttl

Converts RDF triples to Neo4j nodes and relationships.
"""

import sys
from rdflib import Graph, URIRef, Literal
from neo4j import GraphDatabase

def export_to_neo4j(rdf_file, neo4j_uri="bolt://localhost:7687", username="neo4j", password="trustpassword"):
    """Export RDF graph to Neo4j"""

    print(f"Loading RDF from {rdf_file}...")
    g = Graph()
    g.parse(rdf_file, format="turtle")
    print(f"✓ Loaded {len(g)} triples")

    print(f"\nConnecting to Neo4j at {neo4j_uri}...")
    driver = GraphDatabase.driver(neo4j_uri, auth=(username, password))

    def clear_and_export(tx):
        # Clear existing data
        print("  Clearing existing Neo4j data...")
        tx.run("MATCH (n) DETACH DELETE n")

        # Export triples
        print("  Exporting triples to Neo4j...")
        count = 0

        for s, p, o in g:
            # Extract local names
            subject = str(s).split('#')[-1] if '#' in str(s) else str(s).split('/')[-1]
            predicate = str(p).split('#')[-1] if '#' in str(p) else str(p).split('/')[-1]

            # Clean predicate for Neo4j relationship type
            predicate_clean = predicate.replace('-', '_').replace(' ', '_')

            if isinstance(o, URIRef):
                # Object is a resource → create relationship
                object_val = str(o).split('#')[-1] if '#' in str(o) else str(o).split('/')[-1]

                tx.run(
                    f"MERGE (s:Resource {{uri: $s_uri, name: $s_name}}) "
                    f"MERGE (o:Resource {{uri: $o_uri, name: $o_name}}) "
                    f"MERGE (s)-[r:`{predicate_clean}` {{predicate: $predicate}}]->(o)",
                    s_uri=str(s), s_name=subject,
                    o_uri=str(o), o_name=object_val,
                    predicate=predicate
                )
            else:
                # Object is a literal → create property
                tx.run(
                    f"MERGE (s:Resource {{uri: $s_uri, name: $s_name}}) "
                    f"SET s.`{predicate_clean}` = $value",
                    s_uri=str(s), s_name=subject,
                    value=str(o)
                )

            count += 1
            if count % 100 == 0:
                print(f"    Exported {count} triples...")

        print(f"  ✓ Exported {count} triples")

    with driver.session() as session:
        session.execute_write(clear_and_export)

    driver.close()

    print(f"\n✓ Export complete!")
    print(f"\nNext Steps:")
    print(f"  1. Open Neo4j Browser: http://localhost:7474")
    print(f"  2. Login: neo4j / {password}")
    print(f"  3. Run Cypher queries:")
    print(f"")
    print(f"     // View all nodes")
    print(f"     MATCH (n) RETURN n LIMIT 25")
    print(f"")
    print(f"     // Find trusts")
    print(f"     MATCH (t:Resource)-[:type]->(c {{name: 'TrustEntity'}}) RETURN t")
    print(f"")
    print(f"     // Find transaction paths")
    print(f"     MATCH p=(tx)-[:transactionBy|transactionWith*1..3]-(n) RETURN p")
    print(f"")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_to_neo4j.py <rdf_file.ttl>")
        sys.exit(1)

    rdf_file = sys.argv[1]
    export_to_neo4j(rdf_file)
