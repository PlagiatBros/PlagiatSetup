ls | grep .py$ | while read line; do echo $line; rgrep ProgramFilter $line; echo ""; done 
