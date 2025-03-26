# Horizontal Gene Transfer (HGT) Detection Workflow

## Step 1: Homology Search using DIAMOND
**Objective**: Identify homologous protein sequences in a reference database.

### Method:
1. Use **DIAMOND BLASTP** to compare the **query protein sequence** against a **RefSeq+** database.
2. The **RefSeq+ database** consists of:
   - NCBI Reference Sequence Database (RefSeq)
   - All proteins from **query group genomes**
3. **Cutoff e-value**: `1e-10`
4. Output: A BLASTP result file containing the top hits for each query sequence.

---

## Step 2: Parse BLASTP Output and Construct Phylogenetic Tree
**Objective**: Identify genes with statistical signatures of horizontal transfer.


### **2.1 Extract Homologs**
- Parse the **BLASTP output file** to extract **1,000 homologous sequences** from the **top 1,000 hits** in the **RefSeq+ database**.
### Method:
1. **Calculate Alien Index (AI)**:

$$ AI = \left(\frac{bbhO}{maxB}\right) - \left(\frac{bbhG}{maxB}\right) $$

2. **Compute outg_pct**:
   - **outg_pct**: Percentage of species in the **OUTGROUP lineage** within the **top 1,000 hits**.
   - **Criteria**: Outgroup species should have **different taxonomic species names**.
3. **Define thresholds for HGT candidates**:
   - **AI Score > 0** (Indicates a stronger similarity to outgroup than in-group)
   - **outg_pct ≥ 80%** (High proportion of top hits from the outgroup)
     


---

## Step 3: Detect Putative HGT Events
**Objective**: Extract taxonomic information, align homologs, infer phylogeny, and manually inspect HGT events.

### **3.2 Alignment, Trimming, and Maximum Likelihood Tree**
- **Align homologs** using **MAFFT** (`--auto`).
- **Trim ambiguous regions** using **trimAl** (`-automated1`).
- **Infer a maximum likelihood (ML) tree** using **IQ-TREE** with:
  - **Model selection** (`-m TEST`)
  - **Bootstrap support** (`-bb 1000`)

### **2.3 Root and Visualize Tree**
- **Root the ML tree** using **midpoint rooting** in **R**.
- **Visualize the tree**:
  - **Color tree branches** using **iTOL**.

### **2.4 Manually Inspect the HGT Event**
- Review the phylogenetic tree for potential **HGT signals**.
- Identify cases where:
  - The query gene clusters with distant taxa.
  - Bootstrap support is strong for unexpected phylogenetic placements.

---

## 🔹 Output:
- A list of **putative HGT genes** satisfying AI and outgroup percentage thresholds.
- Annotated phylogenetic trees to support HGT hypothesis.
- Visualization of detected HGT events with taxonomic context.
