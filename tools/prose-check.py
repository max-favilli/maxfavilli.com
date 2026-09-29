#!/usr/bin/env python
"""Report the prose faults CLAUDE.md's writing principle actually names.

Usage:  python tools/prose-check.py <file.md> [more.md ...]

No score out of a hundred. Five signals, each with the offending text,
so every finding is actionable rather than a number to optimise.
"""
import io, re, sys, unicodedata, statistics

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HEDGES = ["somewhat","arguably","quite","rather","very","really","fairly",
          "perhaps","possibly","essentially","basically","actually","simply",
          "just","clearly","obviously","of course","it is worth noting",
          "it's worth noting","in order to","the fact that","needless to say",
          "at the end of the day","that being said","incredibly","extremely"]

NOT_NOMINAL = {"sentence","science","evidence","experience","difference","presence",
    "instance","audience","essence","patience","silence","absence","violence","influence",
    "conference","sequence","reference","preference","confidence","consequence","city",
    "quality","quantity","security","ability","activity","community","majority","minority",
    "opportunity","priority","reality","university","authority","identity","utility",
    "moment","comment","element","document","argument","instrument","environment","equipment",
    "department","government","parliament","management","payment","agreement","statement",
    "business","witness","fitness","illness","darkness","happiness","mention","question",
    "attention","intention","station","nation","condition","position","tradition","edition",
    "version","vision","decision","division","mission","session","profession","expression"}

NOMINAL = re.compile(r"\b\w{4,}(?:tion|sion|ment|ance|ence|ity|ness|isation|ization)\b", re.I)

IRREG = r"(?:been|done|made|given|taken|seen|known|shown|written|built|held|kept|left|sent|found|told|brought|caught|driven|chosen)"
PASSIVE = re.compile(r"\b(?:am|is|are|was|were|be|been|being)\b\s+(?:\w+ly\s+)?(?:\w+ed|" + IRREG + r")\b", re.I)

def clean(t):
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)      # frontmatter
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"```.*?```", "", t, flags=re.S)             # code blocks
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)          # links -> text
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"^#+\s*", "", t, flags=re.M)
    t = re.sub(r"^>\s*", "", t, flags=re.M)
    t = re.sub(r"[*_`]", "", t)
    return t.strip()

def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]

def report(path):
    raw = io.open(path, encoding="utf-8").read()
    if "## Post body" in raw:                                # linkedin drafts
        raw = raw.split("## Post body")[1].split("## First comment")[0]
        raw = re.sub(r"^#.*$", "", raw, flags=re.M)
    t = clean(raw)
    sents = sentences(t)
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", t)
    if not sents:
        print(f"{path}: nothing to read"); return
    lens = [len(s.split()) for s in sents]

    print("=" * 68)
    print(path)
    print("=" * 68)
    print(f"{len(words)} words, {len(sents)} sentences")
    print(f"sentence length: mean {statistics.mean(lens):.1f}  median {statistics.median(lens)}  "
          f"longest {max(lens)}  spread {statistics.pstdev(lens):.1f}")
    if statistics.pstdev(lens) < 4:
        print("  ! low spread - uniform sentence length reads as a slog; vary it")
    print()

    longest = sorted(sents, key=lambda s: -len(s.split()))[:3]
    print("LONGEST SENTENCES")
    for s in longest:
        if len(s.split()) >= 25:
            print(f"  [{len(s.split())}w] {s}")
    if not any(len(s.split()) >= 25 for s in longest):
        print("  none over 25 words")
    print()

    print("NOMINALISATIONS  (a verb trapped inside a noun)")
    hits = []
    for s in sents:
        first = s.split()[0] if s.split() else ""
        for m in NOMINAL.finditer(s):
            w = m.group(0)
            if w.lower() in NOT_NOMINAL:
                continue
            if w[0].isupper() and w != first:      # proper noun
                continue
            hits.append((w, s))
    if hits:
        for w, s in hits[:8]:
            print(f"  {w:<16} {s[:70]}")
        print(f"  {len(hits)} total, {100*len(hits)/len(words):.1f}% of words")
    else:
        print("  none")
    print()

    print("HEDGES AND FILLER")
    found = [(h, s) for s in sents for h in HEDGES
             if re.search(r"\b" + re.escape(h) + r"\b", s, re.I)]
    if found:
        for h, s in found[:8]:
            print(f"  {h:<16} {s[:70]}")
        print(f"  {len(found)} total")
    else:
        print("  none")
    print()

    print("PASSIVE VOICE")
    pas = [(m.group(0), s) for s in sents for m in PASSIVE.finditer(s)]
    if pas:
        for p, s in pas[:6]:
            print(f"  {p:<20} {s[:66]}")
        print(f"  {len(pas)} in {len(sents)} sentences ({100*len(pas)/len(sents):.0f}%)")
    else:
        print("  none")
    print()

    print("LONG WINDUP  (reader waits for the claim)")
    SUB = r"^(?:if|when|while|although|though|because|after|before|since|given|unless|"           r"whereas|despite|once|until|as|having|being|\w+ing)"
    slow = [s for s in sents
            if "," in s and len(s.split(",")[0].split()) >= 8
            and re.match(SUB, s, re.I)]
    if slow:
        for s in slow[:5]:
            n = len(s.split(",")[0].split())
            print(f"  [{n}w before the comma] {s[:66]}")
    else:
        print("  none")
    print()



def metrics(path):
    raw = io.open(path, encoding="utf-8").read()
    if "## Post body" in raw:
        raw = raw.split("## Post body")[1].split("## First comment")[0]
        raw = re.sub(r"^#.*$", "", raw, flags=re.M)
    t = clean(raw)
    sents = sentences(t)
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", t)
    if not sents or not words:
        return None
    lens = [len(x.split()) for x in sents]
    nom = 0
    for x in sents:
        first = x.split()[0] if x.split() else ""
        for m in NOMINAL.finditer(x):
            w = m.group(0)
            if w.lower() in NOT_NOMINAL or (w[0].isupper() and w != first):
                continue
            nom += 1
    hedge = sum(1 for x in sents for h in HEDGES
                if re.search(r"" + re.escape(h) + r"", x, re.I))
    pas = sum(1 for x in sents for _ in PASSIVE.finditer(x))
    SUB = (r"^(?:if|when|while|although|though|because|after|before|since|given|unless|"
           r"whereas|despite|once|until|as|having|being|\w+ing)")
    wind = sum(1 for x in sents if "," in x
               and len(x.split(",")[0].split()) >= 8 and re.match(SUB, x, re.I))
    return dict(words=len(words), sents=len(sents), mean=statistics.mean(lens),
                longest=max(lens), spread=statistics.pstdev(lens),
                hedge=hedge, passive=pas, windup=wind,
                nom=100.0*nom/len(words))


def table(paths):
    rows = []
    for p in paths:
        m = metrics(p)
        if m:
            name = p.split("/")[-1].replace(".md", "")
            rows.append((name, m))
    rows.sort(key=lambda r: -r[1]["mean"])
    hdr = f'{"post":<46}{"words":>6}{"mean":>7}{"max":>5}{"var":>6}{"hedge":>7}{"pass":>6}{"wind":>6}{"nom%":>6}'
    print(hdr); print("-" * len(hdr))
    for name, m in rows:
        print(f'{name[:45]:<46}{m["words"]:>6}{m["mean"]:>7.1f}{m["longest"]:>5}'
              f'{m["spread"]:>6.1f}{m["hedge"]:>7}{m["passive"]:>6}{m["windup"]:>6}{m["nom"]:>6.1f}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    args = sys.argv[1:]
    if args[0] == "--table":
        table(args[1:])
    else:
        for p in args:
            report(p)
