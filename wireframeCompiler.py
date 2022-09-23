
def main():
    
    #Get the filename from the user.
    obj_file_name = (str(input("Enter object files name, file must be in directory of script. ")) + ".obj")
    
    #Open the file and get its contents.
    with open(obj_file_name) as f:
        lines = f.readlines()
        
    #Get a list of verticies and faces. Verticies are in string form, faces are integers.
    verticies = []
    faces = []
    for line in enumerate(lines):
        i, string = line
        if(string[0] == "v"):
            string = string.replace("v","")
            position = string.replace("\n","")
            position = position.replace(" ", "",1)
            position = position.split(" ")
            position[0] = float(position[0])
            position[1] = float(position[1])
            position[2] = float(position[2])

            
            verticies.append(position)
        else:
            if(string[0] == "f"):
                string = string.replace("f","")
                string = string.replace("\n","")
                face = string.split()
                for chars in enumerate(face):
                    i, char = chars
                    face[i] = int(char)
                faces.append(face)
                
    largest = 0
    for point in verticies:
        x,y,z = point
        if(abs(x) > largest):
            largest = abs(x)
        if(abs(y) < largest):
            largest = abs(y)
        if(abs(z) > largest):
            largest = abs(z)
        
    for point in enumerate(verticies):
        i,pont = point
        x,y,z = pont

        verticies[i][0] = round(x/largest,4)
        verticies[i][1] = round(y/largest,4)
        verticies[i][2] = round(z/largest,4)

    #Create a list of positions in 512 length strings, where every three ints comprise a single vertex. Each vertex can be 30 chars long so only 9 will fit in a 512 length string.
    temp_string = ''
    positions_string_form_list = []
    for points in enumerate(verticies):
        i, point = points
        x,y,z = point
        temp_string += " " + str(x) + " " + str(y) + " " + str(z)
        k = i + 1
        if(k  % 11 == 0 and i != 0):
            temp_string = temp_string[1 : : ]
            positions_string_form_list.append(temp_string)
            temp_string = ''
    temp_string = temp_string[1 : : ]
    positions_string_form_list.append(temp_string)


        

    
    
        
    #Get all edges.
    edges = []
    for face in faces:
        face_length = len(face)
        for i in range(0,face_length):
            if i == face_length - 1:
                one_point = face[i]
                other_point = face[0]
            else:
                one_point = face[i]
                other_point = face[i+1]
            if(one_point < other_point):
                edges.append([one_point,other_point])
            else:
                edges.append([other_point,one_point])
                
    #Remove duplicate edges.
    for edge in enumerate(edges):
        e, first_edge = edge
        for edge in enumerate(edges):
            o, other_edge = edge
            if(e != o):
                if(first_edge == other_edge):
                    edges.pop(o)

    #Create a list of edges in 512 length strings, where every two ints comprise a single edge. Limited to an object where there are less than 10,000 vertices. Each edge can be 5 chars long so only 102 will fit in a 512 length string.
    temp_string = ''
    edges_string_form_list = []
    for side in enumerate(edges):
        i, edge = side
        edge = str(edge)
        edge = edge.replace("[","")
        edge = edge.replace("]","")
        edge = edge.replace(",","")
        edge = " " + edge
        temp_string += edge
        k = i + 1
        if(k % 28 == 0 and i != 0):
            temp_string = temp_string[1 : : ]
            edges_string_form_list.append(temp_string)
            temp_string = ''
            k = 0
    temp_string = temp_string[1 : : ]
    edges_string_form_list.append(temp_string)
    
    print("sizes")
    for edge in positions_string_form_list:
        print(len(edge.split(" ")))
        print(len(edge))


    outputFile = open("verticies","w")
    for strA in positions_string_form_list:
        outputFile.write(strA + "\n")
    outputFile.close()

    outputFile = open("edges","w")
    for strA in edges_string_form_list:
        outputFile.write(strA + "\n")
    outputFile.close()
   
            

    #Keep program from closing.
    input("Press enter to close. ")


if __name__ == '__main__':
    main()



