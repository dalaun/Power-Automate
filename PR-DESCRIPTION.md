# Dual-Ontology Architecture (v3.0) + Wiki Auto-Sync

This PR implements a clean separation of semantic commitments from authority commitments in the Trust Domain Estate Planning Extension, following the principle:

> **"Meaning can tolerate ambiguity. Authority cannot."**

## 🎯 Summary

Every axiom in the estate planning ontology was evaluated and categorized:
- **"If I remove this, do I lose understanding?"** → VOCABULARY (semantic layer)
- **"If I remove this, do I lose authority?"** → COMPLIANCE (operational layer)

## 📦 What's Included

### 1. Dual-Ontology Files
- **trust-domain-vocabulary.ttl** (1,628 triples / 86.1%) - Defines what things MEAN
  - All class/property definitions, taxonomy, labels, domain/range
  - No enforcement constraints
  - Use for: Data modeling, interoperability, shared semantics

- **trust-domain-compliance.ttl** (263 triples / 13.9%) - Enforces what is ALLOWED
  - Disjointness, cardinality, state machine, outcome determination
  - Imports vocabulary automatically
  - Use for: Legal compliance, tax outcomes, automated reasoning

### 2. Automation Tools
- **extract_semantic.py** - Extract semantic commitments from original ontology
- **extract_authority.py** - Extract authority commitments from original ontology
- **validate_separated.py** - Validate dual-ontology separation

### 3. Wiki Synchronization 🆕
- **.github/workflows/sync-wiki.yml** - GitHub Action to auto-sync docs/wiki/ → GitHub wiki
- **sync-wiki.sh** - Manual sync script for local use

### 4. Updated Documentation
- **docs/wiki/Home.md** - Updated with v3.0 architecture overview
- **docs/wiki/Estate-Planning-Extension.md** - Comprehensive v3.0 documentation

## 🔑 Key Benefits

✅ **Clarity** - Every axiom explicitly categorized: semantic or authority
✅ **Modularity** - Use vocabulary without enforcement burden
✅ **Flexibility** - Add/remove authority layer as needed
✅ **Auditability** - Clear separation makes governance easier
✅ **Interoperability** - Vocabulary layer sharable across systems
✅ **Evolution** - Semantic and authority layers can evolve independently

## 📊 Validation Results

```
Vocabulary Ontology:
✓ 1,628 triples (semantic commitments only)
✓ 0 functional properties
✓ 0 disjointness axioms

Compliance Ontology:
✓ 263 triples (authority commitments only)
✓ 14 functional properties
✓ 39 disjointness axioms
✓ Automatically imports vocabulary

Combined:
✓ 1,891 triples (original: 1,887 - difference is metadata only)
✓ All axioms accounted for
✓ Clean logical layering achieved
```

## 🚀 After Merging

Once merged to main:
1. ✅ GitHub Action will automatically sync docs/wiki/ to the public GitHub wiki
2. ✅ Future updates to docs/wiki/ will auto-sync on every push
3. ✅ Users can load vocabulary alone for interoperability OR compliance for enforcement

## 📖 Breaking Changes

**Version: 2.0 → 3.0** (major version bump)

The ontology now exists as **TWO files** instead of one:
- trust-domain-vocabulary.ttl (semantic layer)
- trust-domain-compliance.ttl (authority layer)

Original trust-domain-estate-planning.ttl remains for backward compatibility but is superseded.

## 📚 Documentation

All documentation has been updated:
- Architecture explanation
- Separation examples (trust states, transactions, properties)
- Usage patterns (vocabulary-only, compliance, incremental migration)
- Migration guide from v2.0 to v3.0
- Benefits table

**Once merged, the GitHub wiki will automatically update within minutes!**

## 📋 Commits Included

1. Add wiki synchronization automation
2. Update GitHub wiki documentation for dual-ontology architecture (v3.0)
3. Separate ontology into data-centric (vocabulary) and operational (compliance) layers
4. Add comprehensive ontology axiom analysis for semantic vs authority separation
5. Update GitHub wiki documentation for Estate Planning Extension v2.0 closed system
6. Transform Estate Planning Extension into closed outcome-determining decision system (v2.0)

## ✅ Ready to Merge

All files validated, documentation complete, automation ready!
