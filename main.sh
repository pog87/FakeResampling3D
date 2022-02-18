
function resample {
  # resample image, requires ANTs installed
  $ANTSPATH/antsApplyTransforms -d 3 -i ${1} -r ${2} -o ${3} -t identity

}

function job {

    resample data/SL_lq.nii.gz data/SL_hq.nii.gz results/SL_hq_reg.nii.gz
    # resamples SL_lq to the same size of SL_hq, creates the file SL_hq_reg, the ususal way
    python mean_per_segment.py results/SL_hq_reg.nii.gz data/SL_hq_seg.nii.gz
    # prints the mean value per segment
}


function job_fake {
    #same as job, but with Fake Nodes
    python fake_it.py data/SL_lq.nii.gz data/SL_lq_seg.nii.gz #creates the file SL_lq_fake
    python fake_it.py data/SL_hq.nii.gz data/SL_hq_seg.nii.gz #creates the file SL_hq_fake
    resample data/SL_lq_fake.nii.gz data/SL_hq_fake.nii.gz results/SL_hq_reg_fake.nii.gz
    # resamples SL_lq_fake to the same size of SL_hq_fake, creates the file SL_hq_reg_fake
    python unfake_it.py results/SL_hq_reg_fake.nii.gz data/SL_hq_seg.nii.gz #creates the file SL_hq_reg_fake_unfake

    python mean_per_segment.py results/SL_hq_reg_fake_unfake.nii.gz data/SL_hq_seg.nii.gz
    # prints the mean value per segment of the result
}


job

job_fake
