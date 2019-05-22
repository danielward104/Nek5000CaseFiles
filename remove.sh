echo -n "This will remove ALL simulation data, are you sure you wish to continue (y/n)? "
read answer
    if echo "$answer" | grep -iq "^y";then
        rm makefile
        rm nek5000
        rm -r obj
        rm *.f
        rm *.log*
        rm logfile
        rm *.ma2
        rm *.nek5000
        rm *.tmp
        rm *0.f*
        rm *.err
	rm *.out
	rm mesh.jpg
	rm run_python.sh.*
	rm SESSION.NAME
	rm scriptNEK_compile.sh.*
	rm scriptNEK_run.sh.*
	rm libnek5000.a
        rm *.png
        rm *.3D
    else
        echo "Deletion aborted."
    fi
