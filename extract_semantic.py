#!/usr/bin/env python3
"""
Extract semantic commitments from trust-domain-estate-planning.ttl
Creates trust-domain-vocabulary.ttl with only data-centric axioms.
"""

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal
from rdflib.term import URIRef

# Load current ontology
g = Graph()
g.parse("trust-domain-estate-planning.ttl", format="turtle")

# Create new graph for vocabulary
vocab = Graph()

# Copy namespaces
for prefix, namespace in g.namespaces():
    vocab.bind(prefix, namespace)

EP = Namespace("http://example.org/trust-domain/estate-planning#")
TD = Namespace("http://example.org/trust-domain#")

# SEMANTIC COMMITMENTS TO EXTRACT:
# 1. Annotation properties
# 2. Class definitions (rdf:type owl:Class, rdfs:subClassOf, labels, comments)
# 3. Property definitions (rdf:type owl:ObjectProperty/DatatypeProperty, domain, range, inverseOf, subPropertyOf)
# 4. Labels, comments, glossary terms
# 5. Property chains

print("Extracting semantic commitments...")

# 1. Extract annotation properties
for s, p, o in g.triples((None, RDF.type, OWL.AnnotationProperty)):
    vocab.add((s, p, o))
    # Get all triples about this annotation property
    for s2, p2, o2 in g.triples((s, None, None)):
        if p2 != OWL.disjointWith:  # Skip disjointness
            vocab.add((s2, p2, o2))

# 2. Extract class definitions (WITHOUT disjointness, WITHOUT restrictions)
for s, p, o in g.triples((None, RDF.type, OWL.Class)):
    vocab.add((s, p, o))
    # Get subClassOf ONLY if it's a simple URI (not a restriction)
    for s2, p2, o2 in g.triples((s, RDFS.subClassOf, None)):
        if isinstance(o2, URIRef):  # Simple subclass, not restriction
            vocab.add((s2, p2, o2))
    # Get labels, comments, glossary
    for s2, p2, o2 in g.triples((s, RDFS.label, None)):
        vocab.add((s2, p2, o2))
    for s2, p2, o2 in g.triples((s, RDFS.comment, None)):
        vocab.add((s2, p2, o2))
    for s2, p2, o2 in g.triples((s, EP.glossaryTerm, None)):
        vocab.add((s2, p2, o2))

# 3. Extract object properties (WITHOUT functional declarations)
for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty)):
    vocab.add((s, p, o))
    # Get property characteristics (except Functional)
    for s2, p2, o2 in g.triples((s, None, None)):
        if p2 in [RDFS.domain, RDFS.range, RDFS.subPropertyOf, OWL.inverseOf,
                  RDFS.label, RDFS.comment, EP.glossaryTerm, OWL.propertyChainAxiom]:
            vocab.add((s2, p2, o2))
            # For property chains, we need the blank node content
            if p2 == OWL.propertyChainAxiom and not isinstance(o2, URIRef):
                for s3, p3, o3 in g.triples((o2, None, None)):
                    vocab.add((s3, p3, o3))

# 4. Extract datatype properties
for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty)):
    vocab.add((s, p, o))
    for s2, p2, o2 in g.triples((s, None, None)):
        if p2 in [RDFS.domain, RDFS.range, RDFS.label, RDFS.comment, EP.glossaryTerm]:
            vocab.add((s2, p2, o2))

# 5. Extract named individuals that are NOT part of state machine
# (We'll include state individuals in vocabulary as they define meaning, not enforcement)
for s, p, o in g.triples((None, RDF.type, OWL.NamedIndividual)):
    vocab.add((s, p, o))
    # But only extract their basic properties
    for s2, p2, o2 in g.triples((s, RDFS.label, None)):
        vocab.add((s2, p2, o2))
    for s2, p2, o2 in g.triples((s, RDFS.comment, None)):
        vocab.add((s2, p2, o2))
    # Include their type assertions for state individuals
    for s2, p2, o2 in g.triples((s, RDF.type, None)):
        if o2 != OWL.NamedIndividual:  # Get other types (like ep:TrustState)
            vocab.add((s2, p2, o2))

# 6. Add ontology metadata (but update description for vocabulary-only)
ontology_uri = URIRef("http://example.org/trust-domain/estate-planning/vocabulary")
vocab.add((ontology_uri, RDF.type, OWL.Ontology))
vocab.add((ontology_uri, OWL.imports, URIRef("http://example.org/trust-domain")))
vocab.add((ontology_uri, RDFS.label, Literal("Trust Domain Estate Planning Vocabulary (Data-Centric Layer)", lang="en")))
vocab.add((ontology_uri, OWL.versionInfo, Literal("3.0")))

comment = """SEMANTIC COMMITMENTS (Data-Centric Layer)

This ontology defines WHAT THINGS MEAN in the trust and estate planning domain.
It does NOT enforce what is allowed - that is the job of the compliance layer.

Litmus test: "If I remove this axiom, do I lose understanding?"
If yes → it belongs here. If no (lose authority instead) → belongs in compliance layer.

Contains:
- Class definitions (taxonomy only, no disjointness)
- Property definitions (relationships only, no cardinality)
- Domain and range (what connects to what)
- Inverse properties (bidirectional navigation)
- Labels, comments, glossary mappings
- Property chains (compositional meaning)
- State definitions (what states mean, not transitions)

Does NOT contain:
- Cardinality constraints
- Disjointness axioms
- Functional property declarations
- State machine transitions
- Outcome determination rules
- Closure axioms

For enforcement of what is allowed, see: trust-domain-compliance.ttl"""

vocab.add((ontology_uri, RDFS.comment, Literal(comment, lang="en")))

print(f"Extracted {len(vocab)} semantic triples")
print("Writing to trust-domain-vocabulary.ttl...")

# Serialize
vocab.serialize("trust-domain-vocabulary.ttl", format="turtle")

print("✓ Vocabulary ontology created")
print(f"  Total triples: {len(vocab)}")
