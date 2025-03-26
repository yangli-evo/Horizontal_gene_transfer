
import glob
import os
import subprocess

i = 0
filenames = glob.glob("*.treefile")

for filename in filenames:
    gene = filename.split('.')[0]  # Get file prefix (before .treefile)
    i += 1
    unr_file_r = f"{gene}_midpoint.R"
    
    # Write R script to file
    with open(unr_file_r, "a") as out3:
        out3.write("library(ape)\n")
        out3.write("library(phangorn)\n")
        out3.write(f"mytree{i} <- read.tree(\"{filename}\")\n")
        out3.write(f"midponit_mytree{i} <- ladderize(midpoint(mytree{i}))\n")
        out3.write(f"write.tree(midponit_mytree{i}, \"{gene}_midpoint.tree\")\n")
    
    # Run R script
    subprocess.run(["R", "CMD", "BATCH", unr_file_r])
    
    # Clean up
    os.remove(unr_file_r)
    for rout_file in glob.glob("*.Rout"):
        os.remove(rout_file)
    os.remove(".RData")
    os.remove(filename)
