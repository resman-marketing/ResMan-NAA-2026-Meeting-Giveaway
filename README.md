# ResMan NAA 2026 Meeting Giveaway

Sales field guide for the **NAA Apartmentalize 2026** Booth 2801 AirPods 4 Party Link giveaway.

**Live page:** https://resman-marketing.github.io/ResMan-NAA-2026-Meeting-Giveaway/

## How it's built

`index.html` is **generated** — don't hand-edit it. The single self-contained file
(logos, QR, both GIFs, and all styles are embedded) is produced by the build script.

```
src/
  build.py            # generator — all copy, layout, and styles live here
  assets/             # source files embedded into index.html
    logo_white_clean.svg
    logo_color_clean.svg
    partylink_qr.svg
    prospect_orig.gif  # the Sendoso Party Link experience (phone frame)
    jazzed.gif         # NAA "Get Jazzed" spinning badge
index.html            # built output, served by GitHub Pages
deploy.sh             # build + commit + push in one step
```

## To make a change

1. Edit `src/build.py` (copy, sections, styles) or swap a file in `src/assets/`.
2. Run the deploy script:

   ```bash
   ./deploy.sh "describe the change"
   ```

   It rebuilds `index.html`, commits, and pushes. GitHub Pages refreshes in ~1 minute.

To preview locally before deploying, open `index.html` in a browser (the 3D AirPods
model and Roboto font load from the web; everything else is embedded).

## Notes

- The rotating AirPods is a Sketchfab 3D embed (loads over HTTPS, needs internet).
- This giveaway is **not publicized** — it's an internal tool for reps to book ResMan
  meetings on-site at NAA.
