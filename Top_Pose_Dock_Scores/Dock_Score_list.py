from pathlib import Path
import math
import os

input_folder_path = r""
input_folder_path = input("\n" " Please enter the path of your folder containing all output files in pdbqt format: ")

pose = 1

def Fetching_each_file(input_folder_path):
	input_folder_path = Path(input_folder_path)
	
	# extracting only the .pdbqt files from input folder using glob function
	# glob functions returns the path of the .pdbqt files
	# is_file() checks whether a particular item is a file or not
	files_list = [item for item in input_folder_path.glob("*.pdbqt") if item.is_file()]
	files_list.sort()
	out_path = input_folder_path/"Final_List.txt"

	with open(out_path,"w") as fw:
		header = ["Ligand","\t","\t","  ","Pose_No","\t","Dock_Score","\t","\n"]
		fw.writelines(header)

	for input_path in files_list:
		#Output_filename = "Output_" + input_path.parts[-1] + ".txt"
		#out_path = input_folder_path/Output_filename
		#print(out_path)
		#print(input_path.parts[-1])
		ligand = input_path.parts[-1].split("_")[0]
				
		out_path = Main(input_path, out_path, ligand)
	print("\n" " Output file successfully generated at:  ", out_path)
		
		#print(ligand)



def Main(input_path, out_path, ligand):
	final_list = []
	#score_list = []
	with open(input_path, "r") as fr:
		for line in fr:
			line_list = Remove_unwanted_spaces(line)
			#print(line_list)
			#print(len(line_list))
			if line_list[0] == "MODEL":
				model = Checking_model_number(line_list,pose)
				if model == "Null":
					break
				
			#print(model)
			if "RESULT:" in line_list:
				docking_score = float(Extract_docking_score(line_list))
				#print(docking_score)
				#score = float(Extract_docking_score(line_list))
				coordinates_list = []	
				coordinates_list.insert(0,ligand)
				coordinates_list.insert(1,model)
				coordinates_list.insert(2,docking_score)
				#score_list.append(dock_score)
				#score_list.sort()
				#print(score_list)
			#coordinates_list.insert(5,dist)
			#print(coordinates_list)
				final_list.append(coordinates_list)
			#final_list.sort()
			final_list.sort(key = lambda final_list: final_list[2])
			#final_list.sort(key = lambda i: final_list.index(i[2]))
			#print(final_list)
																																
	
		#### for writing data to the model
		Write_data(final_list,out_path)
			
	return out_path
	
def Remove_unwanted_spaces(line):
	line = line.strip(" \n") # making each line of uniform length
	for j in range(7,0,-1):
		line = line.replace(" "*j,"#")	
		line_list = line.split("#")
	#print(line_list)
	#print(len(line_list))
	return line_list

def Checking_model_number(line_list,pose):
		model_number = int(line_list[1])
		if model_number > int(pose):
			return "Null"
		else:
			model = "".join(line_list).strip("\n")
			return model
	

def Extract_docking_score(line_list):
	docking_score = line_list[3]
	return docking_score

	
def Write_data(final_list,out_path):
	#header = ["Ligand","\t","Model Number","\t","Score","\t","Atom","\t","AtomNo","\t","Distance from Fe","\n"]
	#print(final_list)
	#print(len(final_list))
	#print(out_path)
	
	with open(out_path,"a") as fw:
		#fw.writelines(header)
		for line in final_list:
			line = [str(item)+"\t"+"   " for item in line]
			fw.writelines(line[0:3])
			#fw.writelines(line[2:-3])
						
			fw.write("\n")
		#fw.write("\n")
		
Fetching_each_file(input_folder_path)
