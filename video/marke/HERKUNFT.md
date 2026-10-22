# Marken-Dateien — woher sie kommen

| Datei | Quelle | im Repo? |
|---|---|---|
| `ynb-logo-weiss.png` | Übergabe, 1,5 MB | ja |
| `ynb-outro-9x16.mov` | Drive `1kLsW8GjTWR-X4_02r7yqWuRUtCa6h5aX` („YNB Podcast: Outro 9:16"), 137,6 MB, 1080×1920, 4,21 s, mit Ton | **nein** — zu groß für git |

## Das Outro gehört hinter jeden Short

Seine Ansage vom 22.10.2026: *„du vergisst jetzt schon wieder mein Outro. Wo
ist mein Outro? Das gehört hinter jedes Short."* Es stand als Flag im
Renderer (`--outro`), wurde aber nie gesetzt — bei Sutcliffe wie bei
Aaronson fehlte es.

Anhängen mit `video/outro_anhaengen.py`, **nach** dem Musikbett. Über
`--outro` beim Rendern geht es auch, dann liegt das Bett aber hinterher
ebenfalls über dem Outro.

## Holen, wenn die Datei fehlt

```python
import importlib.util
spec = importlib.util.spec_from_file_location("dz", "video/drive_fernzugriff.py")
dz = importlib.util.module_from_spec(spec); spec.loader.exec_module(dz)
r = dz.SITZUNG.get(dz.bestaetigte_url("1kLsW8GjTWR-X4_02r7yqWuRUtCa6h5aX"), stream=True)
open("video/marke/ynb-outro-9x16.mov", "wb").write(r.content)
```

`bestaetigte_url` wird gebraucht, weil Drive vor großen Dateien eine
Virenscan-Warnung schiebt und die Bytes erst mit deren Token herausgibt.
