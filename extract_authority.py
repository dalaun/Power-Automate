#!/usr/bin/env python3
"""
Extract authority commitments from trust-domain-estate-planning.ttl
Creates trust-domain-compliance.ttl with only operational axioms.
"""

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, BNode
from rdflib.term import URIRef

# Load current ontology
g = Graph()
g.parse("trust-domain-estate-planning.ttl", format="turtle")

# Create new graph for compliance
compliance = Graph()

# Copy namespaces
for prefix, namespace in g.namespaces():
    compliance.bind(prefix, namespace)

EP = Namespace("http://example.org/trust-domain/estate-planning#")
TD = Namespace("http://example.org/trust-domain#")

# AUTHORITY COMMITMENTS TO EXTRACT:
# 1. Disjointness axioms
# 2. Cardinality constraints (restrictions with min/max/cardinality)
# 3. Functional property declarations
# 4. Closure axioms (unionOf forcing classification)
# 5. State machine (oneOf enumeration + transitions)
# 6. Outcome determination (equivalentClass with intersection/union + axioms)

print("Extracting authority commitments...")

# 1. Extract disjointness axioms
for s, p, o in g.triples((None, OWL.disjointWith, None)):
    compliance.add((s, p, o))

# 2. Extract functional property declarations
for s, p, o in g.triples((None, RDF.type, OWL.FunctionalProperty)):
    compliance.add((s, p, o))

# 3. Extract restrictions (cardinality constraints, someValuesFrom, etc.)
for s, p, o in g.triples((None, RDFS.subClassOf, None)):
    if not isinstance(o, URIRef):  # It's a blank node (restriction)
        compliance.add((s, p, o))
        # Get all triples about this restriction
        def extract_restriction_tree(node):
            for s2, p2, o2 in g.triples((node, None, None)):
                compliance.add((s2, p2, o2))
                # Recursively extract nested blank nodes
                if isinstance(o2, BNode):
                    extract_restriction_tree(o2)
        extract_restriction_tree(o)

# 4. Extract equivalent class definitions (for defined classes like PotentialSelfDealingTransaction)
for s, p, o in g.triples((None, OWL.equivalentClass, None)):
    compliance.add((s, p, o))
    # Extract the class expression tree
    if not isinstance(o, URIRef):
        def extract_class_expression(node):
            for s2, p2, o2 in g.triples((node, None, None)):
                compliance.add((s2, p2, o2))
                if isinstance(o2, BNode):
                    extract_class_expression(o2)
                # Handle RDF lists (for intersectionOf, unionOf, oneOf)
                if p2 in [OWL.intersectionOf, OWL.unionOf, OWL.oneOf]:
                    extract_rdf_list(o2)
        def extract_rdf_list(node):
            for s2, p2, o2 in g.triples((node, None, None)):
                compliance.add((s2, p2, o2))
                if isinstance(o2, BNode):
                    extract_rdf_list(o2)
        extract_class_expression(o)

# 5. Extract state transition assertions (ep:canTransitionTo)
CAN_TRANSITION_TO = EP.canTransitionTo
for s, p, o in g.triples((None, CAN_TRANSITION_TO, None)):
    compliance.add((s, p, o))

# 6. Add ontology metadata
ontology_uri = URIRef("http://example.org/trust-domain/estate-planning/compliance")
compliance.add((ontology_uri, RDF.type, OWL.Ontology))
compliance.add((ontology_uri, OWL.imports, URIRef("http://example.org/trust-domain/estate-planning/vocabulary")))
compliance.add((ontology_uri, RDFS.label, Literal("Trust Domain Estate Planning Compliance (Operational Layer)", lang="en")))
compliance.add((ontology_uri, OWL.versionInfo, Literal("3.0")))

comment = """AUTHORITY COMMITMENTS (Operational Layer)

This ontology enforces WHAT IS ALLOWED in the trust and estate planning domain.
It does NOT define what things mean - that is the job of the vocabulary layer.

Litmus test: "If I remove this axiom, do I lose authority?"
If yes → it belongs here. If no (lose understanding instead) → belongs in vocabulary layer.

Contains:
- Cardinality constraints (minCardinality, maxCardinality, cardinality)
- Disjointness axioms (mutual exclusion)
- Functional property declarations (max 1 value)
- State machine transitions (canTransitionTo)
- State enumeration (oneOf - closed world)
- Outcome determination rules (equivalentClass with intersection/union)
- Closure axioms (forcing classification via unionOf)

Does NOT contain:
- Class definitions (in vocabulary)
- Property definitions (in vocabulary)
- Labels, comments, glossary (in vocabulary)
- Domain/range (in vocabulary)

This layer IMPORTS the vocabulary layer and adds enforcement on top of meaning.

Design principle: "Meaning can tolerate ambiguity. Authority cannot."
"""

compliance.add((ontology_uri, RDFS.comment, Literal(comment, lang="en")))

print(f"Extracted {len(compliance)} authority triples")
print("Writing to trust-domain-compliance.ttl...")

# Serialize
compliance.serialize("trust-domain-compliance.ttl", format="turtle")

print("✓ Compliance ontology created")
print(f"  Total triples: {len(compliance)}")
