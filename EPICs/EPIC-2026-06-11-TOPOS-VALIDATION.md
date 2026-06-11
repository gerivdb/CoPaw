---
intent_hash: 0xEPIC_COPAW_VALIDATION_20260611
status: active
priority: P1
owner: Kilo Agent
repo: gerivdb/CoPaw
type: EPIC
---

# EPIC-2026-06-11-COPAW-TOPOS-VALIDATION

**Statut** : ACTIF
**Type** : Consumer / Validation
**Priorité** : P1 — HAUTE
**Propriétaire** : Kilo Agent
**Dépôt** : `gerivdb/CoPaw`
**IntentHash** : `0xEPIC_COPAW_VALIDATION_20260611`

---

## Objectif

Implémenter le bridge TOPOS validator dans CoPaw pour la conformité des profils d'environnement contre le schéma.

## Context

BRIDGES.yaml déclare le bridge `TOPOS-COPAW-VALIDATION` en statut `active`. L'implémentation (N+16) a produit le code mais l'EPIC formel n'a jamais été créé.

## Livrables

### 1. TOPOS Validator Bridge
- [x] `copaw/bridges/topos_validator_bridge.py` — validation schéma
- [ ] Tests unitaires
- [ ] Intégration CoPaw core

### 2. Métriques de couverture
- [ ] Calcul de la couverture des profils
- [ ] Rapports de non-conformité
- [ ] Recommandations de correction

## Dependances

### Realises :
- [x] `copaw/bridges/topos_validator_bridge.py` (commit 4a2edc26)

### En Cours :
- [ ] Tests unitaires
- [ ] Intégration

---

## Metriques de Succes

| Objectif | Cible | Actuel |
|----------|-------|--------|
| topos_validator | Oui | Code pret |
| Tests unitaires | > 80% | 0% |
| Intégration | Oui | Non |

---

## Statut Global

```
topos_validator : ✅ 100%
Tests unitaires : 🔄 0%
Intégration     : 🔄 0%
```

---

**Derniere mise a jour** : 2026-06-11
**Statut** : ACTIF
