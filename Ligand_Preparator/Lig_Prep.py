import os
import subprocess

for files in os.listdir("."):
    if files.endswith(".sdf"):
    	ligand = files.strip('.sdf')
    	#subprocess.run(["obabel", "-isdf", files, "-osdf", "-O" + files.strip('.sdf') + "_conf.sdf", "--gen3d", "--conformer", "--nconf", "10", "--weighted", "--ff"], check=True)
    	subprocess.run(["obabel", "-isdf", files, "-osdf", "-O" + ligand + "_conf.sdf", "--gen3d", "--conformer", "--nconf", "10", "--weighted", "--ff"], check=True)
  
for files in os.listdir("."):
    if files.endswith("_conf.sdf"):
    	#ligand1 = files.strip('_conf.sdf')
    	subprocess.run(["obabel", "-isdf", files, "-osdf", "-O" + files.strip('conf.sdf') + "lig.sdf", "--minimize", "--ff", "MMFF94"], check=True)
    	#subprocess.run(["obabel", "-isdf", files, "-osdf", "-O" + ligand1 + "lig.sdf", "--minimize", "--ff", "MMFF94"], check=True)

for files in os.listdir("."):
    if files.endswith("_lig.sdf"):
    	subprocess.run(["obabel", "-isdf", files, "-opdbqt", "-O" + files.strip('_lig.sdf') + ".pdbqt", "--partialcharge", "gasteiger"], check=True)

for files in os.listdir("."):
    if files.endswith("_conf.sdf"):
        os.remove(files)
    #if files.endswith("_lig.sdf"):
        #os.remove(files)

subprocess.run(["mkdir", "Prepared_Ligands_pdbqt"])
        
for files in os.listdir("."):
    if files.endswith(".pdbqt"):
    	subprocess.run(["mv", files, "Prepared_Ligands_pdbqt/"])

subprocess.run(["mkdir", "Minimized_Ligands_sdf"])
        
for files in os.listdir("."):
    if files.endswith("_lig.sdf"):
    	subprocess.run(["mv", files, "Minimized_Ligands_sdf/"])
    	
#subprocess.run(["mkdir", "Raw_Ligands_sdf"])

#for files in os.listdir("."):
    #if files.endswith(".sdf"):
    	#subprocess.run(["mv", files, "Raw_Ligands_sdf/"])
