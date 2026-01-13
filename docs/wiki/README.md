# Trust Domain Ontology Wiki

This directory contains the complete documentation for the Trust Domain Ontology.

## Pages

### Getting Started
- **[Home](Home.md)** - Overview and introduction
- **[Architecture](Architecture.md)** - The control-plane framework
- **[Keystone Constraint](Keystone-Constraint.md)** - The fundamental rule
- **[Authority Cascade](Authority-Cascade.md)** - Mission to spend traceability

### Reference
- **[Classes](Classes.md)** - All ontology classes
- **[Properties](Properties.md)** - Object and data properties
- **[Examples](Examples.md)** - Concrete individuals and scenarios
- **[Usage Guide](Usage-Guide.md)** - Querying and validation

## Quick Links

- [View Ontology File](../../trust-domain-ontology.ttl)
- [Main Repository](../../)

## Using This Documentation

### As GitHub Wiki

To use this as a GitHub wiki:

1. Enable wiki on your GitHub repository
2. Clone the wiki: `git clone https://github.com/dalaun/Power-Automate.wiki.git`
3. Copy contents of `docs/wiki/` to the wiki repository
4. Commit and push

### As GitHub Pages

This documentation is compatible with GitHub Pages:

1. Go to repository Settings → Pages
2. Set source to `docs/` folder
3. Documentation will be available at `https://dalaun.github.io/Power-Automate/wiki/`

### As In-Repo Documentation

The documentation works as-is in the repository and can be browsed directly on GitHub.

---

## The Paradigm Shift

This ontology transforms tax compliance from legal opinion into **graph traversal**:

**Traditional**: "Is this private inurement?" → Hire lawyers, hope auditor agrees

**This Ontology**: "Is this private inurement?" → Run query, does path exist?

```sparql
SELECT ?spend WHERE {
  ?spend a :ActualSpend .
  FILTER NOT EXISTS { ?spend :tracesBackTo ?purpose }
}
```

If query returns results → private inurement.

---

**This is tax compliance as a database query.**
