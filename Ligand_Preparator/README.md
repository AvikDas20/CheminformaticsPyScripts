This code prepares a ligand for docking from a hand sketched 2D SDF file.

NECESSARY REQUIREMENTS
	1) Keep all your ligands in sdf format in the directory where the script is present.
	2) Open babel 2.4.0 or higher must be installed in your system
	3) It works only on LINUX based system or Cygwin enabled OS platform

On running the script 
	1) It generates the 3D structure of the ligand
	2) Generates conformer search using the MMFF94 forcefield and returns the lowest energy conformer
	3) Energy minimization of the ligand is performed using MMFF94 forcefield
	4) Conversion of sdf files to pdbqt files and adding Gasteiger partialcharges simultaneously
	5) Creating two directories for the segregation of sdf file and pdbqt file
	6) The raw sdf files and prepared pdbqt ligands are kept in directories "Raw_Ligands_sdf" and "Prepared_Ligands_pdbqt" respectively.
	
A set of test files .sdf has been added in the directory for perusal.
