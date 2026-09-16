train_name = 'Train'
val_name = 'Val'
test_name = 'Test'

model = dict(type='UIEC2Net', get_parameter=True)
dataset_type = 'AlignedDataset'

data_root_train = './DATA/Train/'
data_root_test = './DATA/Test/'
train_ann_file_path = 'train.txt'
val_ann_file_path = 'test_time.txt'
test_ann_file_path = 'test_time.txt'

img_norm_cfg = dict(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
train_pipeline = [
    dict(type='LoadImageFromFile', gt_type='color', get_gt=True),
    dict(type='RandomFlip', flip_ratio=0.0),
    dict(type='ImageToTensor')
]
test_pipeling = [
    dict(type='LoadImageFromFile', gt_type='color', get_gt=False),
    dict(type='ImageToTensor')
]

usebytescale = False

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=0,
    val_samples_per_gpu=1,
    val_workers_per_gpu=0,
    train=dict(
        type=dataset_type,
        ann_file=data_root_train + train_ann_file_path,
        img_prefix=data_root_train + 'train/',
        gt_prefix=data_root_train + 'gt/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root_test + test_ann_file_path,
        img_prefix=data_root_test + 'test_time/',
        gt_prefix=data_root_test + 'gt/',
        pipeline=test_pipeling),
    test=dict(
        type=dataset_type,
        ann_file=data_root_test + test_ann_file_path,
        img_prefix=data_root_test + 'test_time/',
        gt_prefix=data_root_test + 'gt/',
        pipeline=test_pipeling,
        test_mode=True))

train_cfg = dict(train_backbone=True)
test_cfg = dict(metrics=['SSIM', 'MSE', 'PSNR'])

loss_ssim = dict(type='SSIMLoss', window_size=11, size_average=True, loss_weight=1.0)
loss_l1 = dict(type='L1Loss', loss_weight=2.0)
loss_perc = dict(type='PerceptualLoss', loss_weight=0,
                 no_vgg_instance=False, vgg_mean=False,
                 vgg_choose='conv4_3', vgg_maxpooling=False)

optimizer = dict(type='Adam', lr=1e-3, betas=[0.9, 0.999])
lr_config = dict(type='Epoch',
                 warmup='linear',
                 step=[1, 1],
                 liner_end=0.00001,
                 step_gamma=0.1,
                 exp_gamma=0.9)

log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook'),
        dict(type='VisdomLoggerHook')
    ])

total_epoch = 1
total_iters = None
work_dir = './checkpoints/UIEC2Net/smoke'
load_from = None
resume_from = None
save_freq_iters = 1
save_freq_epoch = 1
log_level = 'INFO'

savepath = 'results/UIEC2Net'
