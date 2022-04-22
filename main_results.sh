echo "Mean value per segment"
echo "gold standard"
python mean_per_segment.py data/SL_hq.nii.gz data/SL_hq_seg.nii.gz

echo "Trilinear upsampling"
python mean_per_segment.py results/SL_hq_reg.nii.gz data/SL_hq_seg.nii.gz

echo "Fake Nodes + Trilinear upsampling"
python mean_per_segment.py results/SL_hq_reg_fake_unfake.nii.gz data/SL_hq_seg.nii.gz

echo "Downscaling the segments"
python mean_per_segment.py data/SL_lq.nii.gz results/SL_lq_seg.nii.gz

echo "------------"

echo "Global error measures"
echo "gold standard Vs goal standard"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq.nii.gz

echo "gold standard Vs resampling"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq_reg.nii.gz

echo "gold standard Vs Fake Nodes resampling"
python global_error_measures.py data/SL_hq.nii.gz data/SL_hq_reg_fake_unfake.nii.gz
