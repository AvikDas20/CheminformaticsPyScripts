import os
import subprocess

receptor = input("Enter the name of the receptor file without the extension ")

for files in os.listdir("."):
    if files.endswith(".pdbqt"):
        ligand = os.path.splitext(files)[0]
        if ligand == receptor:
            continue
        else:
            print("Processing ligand", ligand)
            subprocess.run(["mkdir", "-p", ligand])
            subprocess.run(
                ["vina", "--config", "conf.txt", "--ligand", ligand + ".pdbqt", "--out", ligand + "_out.pdbqt",
                 "--log", ligand + "/" + ligand + "_log.txt"], check=True)

subprocess.run(["mkdir", "Output_files_pdbqt"])
for files in os.listdir("."):
    if files.endswith("_out.pdbqt"):
        subprocess.run(["mv", files, "Output_files_pdbqt/"])
        # subprocess.run(
        # ["vina", "--config", "conf.txt", "--ligand", ligand + ".pdbqt", "--out", ligand + "/" + ligand + "_out.pdbqt",
        # "--log", ligand + "/" + ligand + "_log.txt"], check=True)

# for files in os.listdir("."):
# if files.endswith(".mol"):
# os.remove(files)
