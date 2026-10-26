# Thor CAN connector provenance

Origin: [pcb-agx-thor-can-breakout](https://github.com/mvalancy/pcb-agx-thor-can-breakout), A0 engineering prototype,2026-10-26.

## Samtec SHF-113-01-L-D-SM

Original footprint from [Samtec footprint drawing](https://suddendocs.samtec.com/prints/shf-1xx-01-x-d-xx-xx-footprint.pdf), revisionA, and [product drawing](https://suddendocs.samtec.com/prints/shf-1xx-01-x-d-xx-xx-xx-mkt.pdf). No locating-post option. Twenty-six0.74×2.54mm SMT pads on1.27mm X pitch, alternating rows atY±2.16mm; body22.86×5.08mm. Pin1 atX−7.62,Y+2.16, top-view convention. Courtyard0.5mm around pad/body envelope.

The FFSD family lists SHF among its mates. No claim is made that this footprint matches Wieson AC2800-0011-022-H0, the actual Thor J47 BOM part. Manufacturer sample mating, pin1 orientation and solder process are unverified.

## Assmann A-DS09A/KG-T2S

Source: Assmann ASS4888CO, revision10, sheet1/2 Male,2023-10-27, via [datasheet](https://www.lcsc.com/datasheet/C3127392.pdf). Supplier C3127392 / DigiKey AE10968-ND. Derived from KiCad10.0.1 `DSUB-9_Pins_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm`.

Signal centers remain unchanged (2.77×2.84mm,1.00mm drills). Shell centers becomeX−6.955/+18.035,Y+1.44mm relative to pin1; drill3.05mm. TheY datum comes from face→pin1=10.94 and face→shell=9.5; the drawing's rounded dimensions leave a0.02mm distinction from the row midpoint. Verify on a sample. The standard courtyard is retained as a nominal envelope; body/flange/axis and mating cable fit remain mechanical checks.

The standard KiCad3D model is retained as an approximate review model, not manufacturer-certified geometry. The original and derivative library files are©KiCad contributors under [CC BY-SA4.0 with design exception](https://www.kicad.org/libraries/license/).

## Checks and limits

Run `python tools/check_library.py --footprints`, `--symbols`, and `--no-backups`. Native KiCad10 loading and project ERC/DRC/parity are exercised in the originating hardware project. Balanced s-expressions do not prove correct dimensions or mating. No proprietary vendor PDFs are redistributed.

## Wieson AC2800-0011-022-H0 — exact reference-layout lands

The NVIDIA P4071A02 native ODB++ package, placed copper and Allegro ASCII extraction were cross-checked for all26pads. The top-side normalized footprint has0.74×3.00mm pads, odd-rowY+1.93 and even-rowY−1.93,1.27mm pitch,0.05mm mask expansion and1:1 paste. No pin drills were found. [Derived measurement authority](j47-footprint-measurements.json) records source archive hashes, member names, line references and normalized polygons.

The body outline is associated with the source's explicit Wieson MPN annotation. A separately dashed CAP outline is included but is not represented as a polarizing key or shroud. The courtyard encloses the source DFA bounds plus0.5mm. The carrier's original bottom-side/180-degree placement is not copied into the new top-side footprint.

This is original footprint code derived from dimensional facts in the reference layout, not a redistribution of vendor CAD/PDF files. The footprint is MIT in the originating project and also offered under this library's CC BY-SA4.0 license. Current manufacturer drawing, order availability, exact height and physical mating remain unverified.
