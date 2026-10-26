# Thor adapter connector footprints

[Library root](../../README.md) · [Provenance and qualification](../../docs/thor-connectors.md)

- `Samtec_SHF-113-01-L-D-SM`: original26-way1.27mm SMT header footprint from Samtec's recommended layout. It is an FFSD-compatible prototype choice, not a verified Wieson replacement.
- `Assmann_A-DS_09_A-KG-T2S`: derivative of the standard KiCad DE9 footprint, updated to the specific manufacturer shell-hole dimensions. The attached standard KiCad3D model is approximate for this part.

Both require physical sample verification before production. Shared under this repository's CC BY-SA4.0 terms; original Samtec work is also MIT in the originating project. The Assmann derivative retains KiCad attribution and license exception.

- `Wieson_AC2800-0011-022-H0`: actual J47 MPN and native NVIDIA reference-layout lands, cross-checked across ASCII and ODB evidence. It supersedes the Samtec candidate as the default in the Thor project. CAP geometry does not prove a keyed mating interface. Current manufacturer drawing, procurement and sample fit remain open.
