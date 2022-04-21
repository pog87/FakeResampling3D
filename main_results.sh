echo "mean value per segment"
echo "gold standard"
python mean_per_segment.py data/SL_hq.nii.gz data/SL_hq_seg.nii.gz

echo "resampling"
python mean_per_segment.py results/SL_hq_reg.nii.gz data/SL_hq_seg.nii.gz

echo "Fake Nodes resampling"
python mean_per_segment.py results/SL_hq_reg_fake_unfake.nii.gz data/SL_hq_seg.nii.gz

echo "global error measures"
echo "gold standard Vs goal standard"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq.nii.gz

echo "gold standard Vs resampling"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq_reg.nii.gz

echo "gold standard Vs Fake Nodes resampling"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq_reg_fake_unfake.nii.gz
