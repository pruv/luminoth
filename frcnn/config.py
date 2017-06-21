
class Config:
    ANCHOR_SCALES = [8, 16, 32]
    ANCHOR_RATIOS = [0.5, 1, 2]
    ANCHOR_BASE_SIZE = 16
    ANCHOR_STRIDE = 16

    # Dataset
    NUM_CLASSES = 20
    DATASET_DIR = 'datasets/voc/tf'
    NUM_EPOCHS = 10
    BATCH_SIZE = 1
    TRAIN_SUBSET = 'train'