# SPELL-Adjusted

This repository provides an adjusted version of the [SPELL](https://github.com/spell-system/SPELL) learning system, tailored specifically for large-scale ontology-based malware detection experiments.

## Key Modifications

Compared to the original system, this version includes:

- **Improved Logging**: `fitting.py` now provides more informative log output and skips irrelevant axioms like `topObjectProperty`.
- **Nominal Handling Enhancements**: `structures.py` has been modified to better assert class types, allowing more expressive concepts.
- **Task & Prop Integration**: All relevant `.plist` property files and learning tasks have been bundled for convenience.

## Snapshot Included

This repository includes a pre-configured snapshot of the original benchmark suite:

```
sml-bench-core-0.3-SNAPSHOT/
```

Please refer to the [original SPELL setup instructions](https://github.com/spell-system/SPELL#installation) for general installation and usage. This snapshot is ready to use with minimal setup.

**Note**: In the provided snapshot, some learning system files under `learning-systems/spell/` (e.g., `run`, `validate`) may not have the executable bit set. If you encounter permission errors, run:

```bash
chmod +x run validate
```

## Contact

For questions, issues, or collaboration opportunities, feel free to contact me at:  
demovic17@uniba.sk
