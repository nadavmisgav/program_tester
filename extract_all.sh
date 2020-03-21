cd src_files
tar_files=`find . -name '*.tar'`

for tar_file in $tar_files;
do
    tar xf $tar_file
    rm -f $tar_file
done;
