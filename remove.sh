echo -n "This will remove ALL simulation data, are you sure you wish to continue (y/n)?"
read answer
    if echo "$answer" | grep -iq "^y";then
	rm compiler.out
	rm makefile
	rm nek5000
	rm -r obj
	rm *.f
	rm *.log.*
	rm logfile
	rm *.ma2
	rm *.nek5000
	rm *.re2
	rm *.tmp
	rm *0.f*
    else	
	echo "Deletion aborted."
    fi
