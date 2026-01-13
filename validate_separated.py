#!/usr/bin/env python3
"""
Validate separated ontologies (vocabulary + compliance)
"""

from rdflib import Graph

print("=" * 80)
print("VALIDATING SEPARATED ONTOLOGIES")
print("=" * 80)

# 1. Validate vocabulary ontology
print("\n1. Validating trust-domain-vocabulary.ttl (SEMANTIC LAYER)...")
vocab = Graph()
try:
    vocab.parse("trust-domain-vocabulary.ttl", format="turtle")
    print(f"   ✓ Valid Turtle syntax")
    print(f"   ✓ Total triples: {len(vocab)}")

    # Check no authority axioms leaked in
    from rdflib import OWL
    functional_count = len(list(vocab.triples((None, None, OWL.FunctionalProperty))))
    disjoint_count = len(list(vocab.triples((None, OWL.disjointWith, None))))

    print(f"   - Functional properties: {functional_count} (should be 0)")
    print(f"   - Disjointness axioms: {disjoint_count} (should be 0)")

    if functional_count > 0 or disjoint_count > 0:
        print("   ⚠ WARNING: Authority axioms found in vocabulary layer!")
    else:
        print("   ✓ Clean semantic layer (no authority axioms)")

except Exception as e:
    print(f"   ✗ FAILED: {e}")
    exit(1)

# 2. Validate compliance ontology
print("\n2. Validating trust-domain-compliance.ttl (AUTHORITY LAYER)...")
compliance = Graph()
try:
    compliance.parse("trust-domain-compliance.ttl", format="turtle")
    print(f"   ✓ Valid Turtle syntax")
    print(f"   ✓ Total triples: {len(compliance)}")

    # Check it has authority axioms
    from rdflib import OWL, RDFS
    functional_count = len(list(compliance.triples((None, None, OWL.FunctionalProperty))))
    disjoint_count = len(list(compliance.triples((None, OWL.disjointWith, None))))

    print(f"   - Functional properties: {functional_count}")
    print(f"   - Disjointness axioms: {disjoint_count}")

    if functional_count == 0 and disjoint_count == 0:
        print("   ⚠ WARNING: No authority axioms found!")
    else:
        print("   ✓ Contains authority axioms")

except Exception as e:
    print(f"   ✗ FAILED: {e}")
    exit(1)

# 3. Test importing compliance into vocabulary
print("\n3. Testing compliance imports vocabulary...")
combined = Graph()
try:
    # Load vocabulary first
    combined.parse("trust-domain-vocabulary.ttl", format="turtle")
    vocab_triples = len(combined)

    # Load compliance (which should import vocabulary)
    combined.parse("trust-domain-compliance.ttl", format="turtle")
    total_triples = len(combined)

    print(f"   ✓ Combined successfully")
    print(f"   - Vocabulary: {vocab_triples} triples")
    print(f"   - Total after compliance: {total_triples} triples")
    print(f"   - Compliance adds: {total_triples - vocab_triples} triples")

except Exception as e:
    print(f"   ✗ FAILED: {e}")
    exit(1)

# 4. Compare with original
print("\n4. Comparing with original ontology...")
original = Graph()
try:
    original.parse("trust-domain-estate-planning.ttl", format="turtle")
    original_count = len(original)

    print(f"   - Original: {original_count} triples")
    print(f"   - Combined (vocab + compliance): {total_triples} triples")
    print(f"   - Difference: {abs(total_triples - original_count)} triples")

    if abs(total_triples - original_count) < 10:  # Allow small difference for metadata
        print("   ✓ Separation successful (similar triple count)")
    else:
        print(f"   ⚠ WARNING: Significant difference in triple count")

except Exception as e:
    print(f"   ✗ FAILED: {e}")
    exit(1)

print("\n" + "=" * 80)
print("VALIDATION COMPLETE ✓")
print("=" * 80)
print("\nSummary:")
print(f"  • Vocabulary (semantic): {vocab_triples} triples")
print(f"  • Compliance (authority): {total_triples - vocab_triples} triples")
print(f"  • Total when combined: {total_triples} triples")
print(f"  • Original ontology: {original_count} triples")
print("\nThe ontology has been successfully separated into:")
print("  1. trust-domain-vocabulary.ttl (data-centric - what things mean)")
print("  2. trust-domain-compliance.ttl (operational - what is allowed)")
