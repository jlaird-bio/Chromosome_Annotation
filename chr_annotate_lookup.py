#!/usr/bin/python

#######################################################################################
#Using a chromosome and its coordinates this program finds its corresponding annotation
#and reports the query and annotation to the file chr_annotate_lookup.txt
#######################################################################################

def read_coordinates(path):
    """
    opens and reads file in a given path
    removes the newline character and splits by \t
    """
    open_coordinates = open(path,"r")
    read_coordinates = open_coordinates.readlines()
    coordinates_list = [i.replace("\n","").split("\t") for i in read_coordinates]
    return coordinates_list

def match_annotation(path,lst,path2):
    """
    opens and reads file in a given path one line at a time due to file size
    removes newline character and splits by \t
    loops through coordinates list 
    creates a match if the chromosome matches
    creates a match if the coordinates are within the range of that gene's start and stop points
    """
    with open(path,"r") as annotations, open(path2,"w") as report:
        for annotation in annotations:
            split_annotate = annotation.replace("\n","").split("\t")
            annotate_start = int(split_annotate[3])
            annotate_end = int(split_annotate[4])
            for coordinates in lst:
                coordinates_num = int(coordinates[1])
                if (coordinates[0] == split_annotate[0] and \
                coordinates_num in range(annotate_start,annotate_end)):
                    match = "query: " +  str("\t".join(coordinates)) + "\n" + "annotation: " + str("\t".join(split_annotate)) + "\n"
                    report.write(match)
                    
#calls the functions with the necessary inputs
coordinates_list = read_coordinates(r"./*.txt")
match_annotation(r"./*.gtf",coordinates_list,r"./*.txt")