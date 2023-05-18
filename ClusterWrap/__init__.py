from shutil import which
import os
from .clusters import janelia_lsf_cluster, local_cluster, cwru_slurm_cluster

cluster = local_cluster

if which('bsub') is not None:
    if os.system('bsub -V') != 32512:
        cluster = janelia_lsf_cluster

if which('sbatch') is not None:
    cluster = cwru_slurm_cluster
