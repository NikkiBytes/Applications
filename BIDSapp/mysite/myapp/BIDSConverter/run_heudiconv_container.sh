
# Get required input from command line
while getopts "u:p:s:i:o:d:h:m:" opt; do
  case $opt in
    u) username="$OPTARG";;
    p) password="$OPTARG";;
    s) subject_name="$OPTARG";;
    i) input_dir="$OPTARG";;
    o) output_dir="$OPTARG";;
    d) dicom_dir="$OPTARG";;
    c) converterfile_path="$OPTARG";;
    h) hpc_address="$OPTARG";;
    m) multiple_sessions="$OTARG";;
  esac
done


# log on to the HPC Cluster
# will need an HPC address and a password from the username
## IF CODE statement below
yes | ssh -XY $hpc_address
sshpass -p $password



# pull container from singularity hub
#singularity pull --name heudiconv.simg shub://NikkiBytes/NIBL_containers/
# run singularity container
singularity shell -B $input_dir:/input_data -B $converterfile_path:/etc heudiconv.simg

# change to the data directory
cd /input_data

# grab folder names to iterate over
# -- Q: if only subj directorys in folder
files=(*)
# ELSE might have to make this customizable w/ regex/ subject tag


# assign counter for filename purposes
# -- possible customization in the future
num=0

# iterate over folders and convert dicoms to bids
for f in ${files[@]};do
num=$(($num+1))
value=$(printf "%02d" $num)
export value
heudiconv -b -d $dicom_dir -s $f -f etc -c dcm2niix -b  -o $HOME/output/{subject}/sub-${value} 
done
