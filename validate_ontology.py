#!/usr/bin/env python3
"""
Validate Trust Domain Ontology Turtle syntax and report statistics.
"""

from rdflib import Graph
import sys

def validate_ontology(filepath):
    """Load and validate Turtle ontology file."""
    g = Graph()

    try:
        print(f"Loading ontology from {filepath}...")
        g.parse(filepath, format='turtle')

        print("✓ Ontology syntax is valid!")
        print(f"\nStatistics:")
        print(f"  Total triples: {len(g)}")

        # Count classes
        classes_query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(DISTINCT ?class) AS ?count)
        WHERE {
            ?class a owl:Class .
        }
        """
        result = list(g.query(classes_query))
        if result:
            print(f"  Total classes: {result[0][0]}")

        # Count properties
        properties_query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(DISTINCT ?prop) AS ?count)
        WHERE {
            { ?prop a owl:ObjectProperty . }
            UNION
            { ?prop a owl:DatatypeProperty . }
        }
        """
        result = list(g.query(properties_query))
        if result:
            print(f"  Total properties: {result[0][0]}")

        # Count individuals
        individuals_query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT (COUNT(DISTINCT ?ind) AS ?count)
        WHERE {
            ?ind a owl:NamedIndividual .
        }
        """
        result = list(g.query(individuals_query))
        if result:
            print(f"  Named individuals: {result[0][0]}")

        return True

    except Exception as e:
        print(f"✗ Ontology validation failed!")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "trust-domain-estate-planning.ttl"
    success = validate_ontology(filepath)
    sys.exit(0 if success else 1)
