# Generates nodes for the SEM.

meshplot = 1            # Decides whether or not to plot the mesh.

# Input parameters:
domain_start_x = -2        # Start of domain.
domain_end_x = 2         # End of domain.
Nel_x = 12                # Number of elements.
N_x = 2                   # Number of clusters.
cluster_x = 0.6      # Amount to cluster elements (geometric ratio).
order = 9               # Order of the simulation.

domain_start_y = 0        # Start of domain.
domain_end_y = 8        # End of domain.
Nel_y = 30                # Number of elements.
N_y = 1                   # Number of clusters.
cluster_y = 1/0.9      # Amount to cluster elements (geometric ratio).


def writeMesh( domain_start, domain_end, Nel, N, cluster, order, save_name ):

    f = open(save_name,'w')

    domain = domain_end - domain_start

    for ix in range(0,N):
    
        x = [0]*100

        # Swaps cluster direction for each sub-domain.
        if (ix == 0):
            ratio = cluster
        elif (ix == 1):
            ratio = 1/cluster
        elif (ix == 2):
            ratio = cluster
        else:
            ratio = 1/cluster
    
        # Initialises sub-domain.
        nelx = int(Nel/N)
        x0 = ix*domain/N
        x1 = (ix+1)*domain/N
    
        # Computes node positions without scalings. 
        dx = 1.0
        x[0] = x0
        for e in range(1,nelx+1):
            x[e] = x[e-1] + dx
            dx = ratio*dx
     
        # Computes scale/geometric ratio.
        xlength = x[nelx] - x[0]
        scale = (x1-x0)/xlength
    
        # Scales node positions.
        for e in range(0,nelx+1):
            x[e] = x0 + (x[e]-x0)*scale + domain_start
      
        # Formats data in scientific form.
        x = [ '%.7e' % elem for elem in x ]
    
        # Orders data for outputting into file.
        
        order1 = order - 1
    
        for i in range(0,int(nelx/order1)+1):
            fir = order1*i
            sec = order1*(i + 1)
            if (ix > 0):
                fir = fir + 1
                sec = sec + 1
            if (sec > nelx):
                sec = nelx + 1
    
            # Writes data to file, removing unwanted characters.
	    # Data formatted for reading into gengeom.
            for k in range(fir,sec):
                f.write(str(x[k]).replace('[','').replace(']','').replace(',',' ').replace("'",'') + '\n')
	    # Data formatted for pasting in .box file.
#	    f.write(str(x[fir:sec]).replace('[','').replace(']','').replace(',',' ').replace("'",'') + '\n')
    
    f.close()
    
    return

writeMesh( domain_start_x, domain_end_x, Nel_x, N_x, cluster_x, order, 'box_x.txt' )
writeMesh( domain_start_y, domain_end_y, Nel_y, N_y, cluster_y, order, 'box_z.txt' )

# Re-opens and reads the file so as to plot the mesh lines.
if (meshplot == 1):

    import matplotlib.pyplot as plt
    plt.switch_backend('agg')

    f = open('box_x.txt','r')
    g = open('box_z.txt','r')

    # Reads in data.
    x = f.readlines()
    y = g.readlines()
    
    # Rewrites x-data to be Python-readable.
    counter = 0
    x_vals = [0]*(Nel_x + 1)
    for line in x:
        Type = line.split()
        length = len(Type)
        counter2 = 0

        for i in range(0,length):
            x_vals[counter] = float(Type[counter2])
            counter = counter + 1
            counter2 = counter2 + 1

    # Rewrites y-data to be Python-readable.
    counter = 0
    y_vals = [0]*(Nel_y + 1)
    for line in y:
        Type = line.split()
        length = len(Type)
        counter2 = 0

        for i in range(0,length):
            y_vals[counter] = float(Type[counter2])
            counter = counter + 1
            counter2 = counter2 + 1

    # Finds lengths of axes.
    height_x = [0]*2
    height_x[0] = y_vals[0]
    height_x[1] = y_vals[-1]

    height_y = [0]*2
    height_y[0] = x_vals[0]
    height_y[1] = x_vals[-1]
   
    # Plots.
    scale = (height_y[1] - height_y[0])/10 
    plt.figure(figsize=((height_y[1] - height_y[0])/scale, (height_x[1] - height_x[0])/scale))
 
    for i in range(0,Nel_x + 1):
        plt.plot([x_vals[i],x_vals[i]],height_x,color='black',linewidth=0.5)

    for i in range(0,Nel_y + 1):
        plt.plot(height_y,[y_vals[i],y_vals[i]],color='black',linewidth=0.5)

    axes = plt.gca()
    axes.set_xlim([height_y[0],height_y[1]])
    axes.set_ylim([height_x[0],height_x[1]])

    plt.savefig('mesh.jpg',bbox_inches='tight')

    f.close()

