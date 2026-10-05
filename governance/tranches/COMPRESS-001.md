# COMPRESS-001 — Compression and Description Length

## Identity
- chapter: ATLAS-CH-COMPRESS-001
- implementation issue: #167
- protected baseline: 356273124481084c6c4d7f9a0d5fae59fe4405cb
- work branch: work/atlas-167

## Hard prerequisites
- ATLAS-CH-INFO-001
- ATLAS-CH-REP-001
- shared audit: AUDIT-004

## External sources
- Rissanen (1978), shortest data description.
- Eckart and Young (1936), lower-rank approximation.
- Han, Mao, and Dally (2016), pruning + trained quantization/weight sharing + Huffman coding.
- Hinton, Vinyals, and Dean (2015), distillation.

## Exact witness
- exact 4x4 all-ones map: dense code 17 bits, rank-one factor code 9 bits under declared codec;
- diagonal low-rank control: rank-1 squared error 10, rank-2 squared error 1;
- pruning control: output changes 1 -> 0 after removing weight 1/8 under threshold 1/4;
- fixed-grid quantization: 32 -> 8 payload bits with zero parameter error;
- learned two-centroid sharing: 32 -> 20 payload bits;
- MDL two-part example: 8 bits versus 12 bits.

## Durable boundaries
- parameter count != description length;
- lossless != lossy compression;
- pruning != quantization != weight sharing;
- low rank != sparsity;
- distillation != source coding;
- compression ratio requires retained-behavior/distortion context;
- compressibility != interpretability;
- compressibility != intelligence.

## Artifact set
- sources/source-locks/ATLAS-CH-COMPRESS-001.yaml
- manuscript/specifications/ATLAS-CH-COMPRESS-001.md
- mathematics/derivations/ATLAS-CH-COMPRESS-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-COMPRESS-001.md
- manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-COMPRESS-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- sources/bibliography.bib
- this receipt
