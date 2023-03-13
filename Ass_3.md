rsync -arl * jdtalley@hpc-portal2.hpc.uark.edu:/storage/jdtalley/mt_genomes
rsync 'unknown.fa'
module purge 
#!/bin/bash

#SBATCH --job-name=assignment 3
#SBATCH --partition comp72
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --time=72:00:00
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jdtalley@uark.edu

cd $mt_genomes

# job command here
module load blast
cat unknown.fa > genomes.fas
makeblastdb -in genomes.fas -dbtype nucl
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn
rsync 'mt_genomes'