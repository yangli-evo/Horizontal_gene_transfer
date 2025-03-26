# Horizontal Gene Transfer (HGT) Detection Workflow

# Step 1
## Step 1.1: Homology Search using DIAMOND
**Objective**: Identify homologous protein sequences in a reference database.

### Method:
1. Use **DIAMOND BLASTP** to compare the **query protein sequence** against a **RefSeq+** database.
2. The **RefSeq+ database** consists of:
   - NCBI Reference Sequence Database (RefSeq)
   - All proteins from **218 insect genomes**
3. **Cutoff e-value**: `1e-10`
4. Output: A BLASTP result file containing the top hits for each query sequence.

---

## Step 1.2: Parse BLASTP Output File
**Objective**: Extract taxonomic information and compute bitscore metrics for further analysis.

### Method:
1. Incorporate the **NCBI Taxonomy Database** to assign **taxon IDs** to each BLASTP hit.
2. Extract **bitscore values** for different evolutionary lineages:
   - **bbhO**: Bitscore of the **best hit** in the **OUTGROUP lineage**.
   - **bbhG**: Bitscore of the **best hit** in the **GROUP lineage** but **not in the RECIPIENT lineage**.
   - **maxB**: Bitscore of the query **to itself** (self-hit).
3. Store results in a structured format for downstream analysis.

---

## Step 1.3: Detect Putative HGT Events
**Objective**: Identify genes with statistical signatures of horizontal transfer.

### Method:
1. **Calculate Alien Index (AI)**:
   \[
   AI = \left(\frac{bbhO}{maxB}\right) - \left(\frac{bbhG}{maxB}\right)
   \]
2. **Compute outg_pct**:
   - **outg_pct**: Percentage of species in the **OUTGROUP lineage** within the **top 1,000 hits**.
   - **Criteria**: Outgroup species should have **different taxonomic species names**.
3. **Define thresholds for HGT candidates**:
   - **AI Score > 0** (Indicates a stronger similarity to outgroup than in-group)
   - **outg_pct ≥ 80%** (High proportion of top hits from the outgroup)

---

# Step 2



## 🔹 Output:
- A list of **putative HGT genes** satisfying AI and outgroup percentage thresholds.
- Annotated results with taxonomic and bitscore-based classification.
