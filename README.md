# KiCAD_Libs

Reusable KiCad symbols, footprints, and 3D models from my hardware projects.

## Contents

| Location | Contents |
| --- | --- |
| [MRV_ICs.lib](Symbols/MRV_ICs.lib) | Legacy IC symbol library |
| [MRV_Passives.lib](Symbols/MRV_Passives.lib) | Legacy passive-component symbol library |
| [MRV_SMD_Packages.pretty](Footprints/MRV_SMD_Packages.pretty) | Surface-mount package footprints |
| [MRV_SMD_Passives.pretty](Footprints/MRV_SMD_Passives.pretty) | Surface-mount passive footprints |
| [MRV_TH_Passives.pretty](Footprints/MRV_TH_Passives.pretty) | Through-hole passive footprints |
| [VNE.pretty](Footprints/VNE.pretty) | Additional project footprints |
| [3d_models](3d_models) | STEP models for use with footprints |

The `.dcm` files alongside the symbols contain legacy symbol documentation.

## Add the libraries to KiCad

```sh
git clone https://github.com/mvalancy/KiCAD_Libs.git
```

Keep the clone at a stable location; library tables reference files on disk.

1. In **Preferences → Manage Symbol Libraries**, add the two `.lib` files from `Symbols/`. Choose the project-specific table for a single project or the global table for all projects. Use the **KiCad Legacy** format for these files.
2. In **Preferences → Manage Footprint Libraries**, add each desired `.pretty` directory from `Footprints/` as a separate library. Select the directory, rather than an individual `.kicad_mod` file.
3. The models in `3d_models/` are separate assets. Inspect a footprint's 3D model settings and assign or repair its model path as needed; registering a footprint library does not automatically assign these files.

Modern KiCad reads legacy `.lib` symbol libraries, but editing requires migration to `.kicad_sym`. Make a branch or copy first, then use **Migrate Libraries** in the symbol library table. See the official [symbol library and migration guide](https://docs.kicad.org/9.0/en/eeschema/eeschema.html#managing-symbol-libraries) and [KiCad library overview](https://www.kicad.org/libraries/download/).

Check pin numbering, pad dimensions, and model alignment against the component datasheet before using a library entry in a new board. These files have not been migrated or requalified as part of this documentation update.

## License

[Creative Commons Attribution-ShareAlike 4.0](LICENSE.md).
