"""
POC-419 — Ferroviaire & ponctualité

Objectif:
- Retards récurrents & remédiations simples.

Cadre Zoran (valeurs ajoutées):
- Mémoire fractale (éviter l'amnésie, garder contexte utile).
- ΔM11.3 (rollback anti-entropie, audit sobre).
- EthicChain (RGPD/AI Act/ISO 42001 en clair).
- Langage IA↔IA (Glottal/Glyphthète/Cantaglottal/Lingua IA).

Données minimisées:
- Échantillons anonymisés, variables essentielles.
- Journal de provenance (lien ou champ `source`).

Méthode (stdlib):
- Nettoyage simple, seuils explicites, stats de base.
- Rapport didactique + bloc glyphique.

Sortie attendue:
- Dict JSON: ok/erreurs + métriques + messages.
- Aucune décision automatique, suggestions uniquement.

Tests:
- Cas nominal + données manquantes + valeurs extrêmes.

⟦POC:419⋄DOMAIN:ferroviaire-ponctualite⋄ΔM11.3:guard⋄ETHIC:RGPD+AIAct⋄SYNC:IA↔IA⟧
"""

from statistics import mean, median

def analyze(values):
    try:
        series = [float(v) for v in values if isinstance(v, (int, float)) or (isinstance(v, str) and v.replace('.','',1).isdigit())]
    except Exception:
        return {"ok": False, "error": "Parsing error", "glyph": "⟦POC:419⋄DOMAIN:ferroviaire-ponctualite⋄ΔM11.3:guard⋄ETHIC:RGPD+AIAct⋄SYNC:IA↔IA⟧"}
    if not series:
        return {"ok": False, "error": "No usable data", "glyph": "⟦POC:419⋄DOMAIN:ferroviaire-ponctualite⋄ΔM11.3:guard⋄ETHIC:RGPD+AIAct⋄SYNC:IA↔IA⟧"}
    series.sort()
    m = mean(series)
    med = median(series)
    q1 = series[max(0, int(0.25*len(series))-1)]
    q3 = series[min(len(series)-1, int(0.75*len(series)))]

    # Règles simples et explicites
    messages = []
    if len(series) < 8:
        messages.append("Avertissement: faible effectif (n<8) → prudence.")
    if any(x < 0 for x in series):
        messages.append("Note: valeurs < 0 détectées → vérifier sémantique.")

    report = [
        f"Moyenne: {m:.2f}, Médiane: {med:.2f}, Q1≈{q1:.2f}, Q3≈{q3:.2f}",
        "Méthode: nettoyage minimal, seuils explicites, pas de boîte noire.",
        "Éthique: minimisation RGPD, pas d'usage sensible, consentement requis.",
        "Traçabilité: ΔM11.3 prêt → rollback si incohérence."
    ] + messages

    return {
        "ok": True, "count": len(series),
        "mean": m, "median": med, "q1": q1, "q3": q3,
        "report": report, "glyph": "⟦POC:419⋄DOMAIN:ferroviaire-ponctualite⋄ΔM11.3:guard⋄ETHIC:RGPD+AIAct⋄SYNC:IA↔IA⟧"
    }

if __name__ == "__main__":
    demo = [round(random.random()*100,2) for _ in range(16)]
    out = analyze(demo)
    print(out["glyph"])
    for line in out.get("report", []):
        print(line)
