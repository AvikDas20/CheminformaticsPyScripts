Hello ! This is a script developed by Avik Das, M.Pharm, BITS Pilani

This code prepares an output file containing the list of ligands and their scores of the best pose from and output file in pdbqt format.

NECESSARY REQUIREMENTS
	1) Keep all your output files in PDBQT format in the directory where the script is present.
	2) It prompts the user for the root directory of the files
	3) It works only on LINUX based system or Cygwin enabled OS platform. 
	
On running the script 
	1) It reads individual output pdbqt files.
	2) Extracts the MODEL no. from the output.
	3) Extracts the coorresponding Vina score for that particular model and particular ligand.
	4) Generates a text file with the list of files and the Vina Score
	
FUTURE MODIFICATIONS PLANNED:
	1) RMSD scores to be included.
	2) Scores to be shown in ascending order. 
	

