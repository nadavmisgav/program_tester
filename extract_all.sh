cd src_files
tar_files=`find . -name '*.tar.gz'`

for tar_file in $tar_files;
do
    tar xzf $tar_file
    rm -f $tar_file
done;
