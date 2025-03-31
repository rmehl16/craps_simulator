
CONDA_BASE=$(conda info --base) ;

source $CONDA_BASE/etc/profile.d/conda.sh

conda activate craps_sim

python --version

cd ../src/craps_simulator

python craps_simulator.py 1
