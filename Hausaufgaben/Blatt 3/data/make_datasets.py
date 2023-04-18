import os, shutil
# Pathing
INPUT_DATASET = 'train'
OUTPUT_DATASET = 'cats_and_dogs_6k'
# Split Sizes
TRAIN = 3000
VAL = 1500
TEST = 1500
# make base directory for new Dataset
os.mkdir(OUTPUT_DATASET)

# train, val, test
train_dir = os.path.join(OUTPUT_DATASET, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(OUTPUT_DATASET, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(OUTPUT_DATASET, 'test')
os.mkdir(test_dir)

# train
train_cats_dir = os.path.join(train_dir, 'cats')
os.mkdir(train_cats_dir)
train_dogs_dir = os.path.join(train_dir, 'dogs')
os.mkdir(train_dogs_dir)

# val
validation_cats_dir = os.path.join(validation_dir, 'cats')
os.mkdir(validation_cats_dir)
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
os.mkdir(validation_dogs_dir)

# test
test_cats_dir = os.path.join(test_dir, 'cats')
os.mkdir(test_cats_dir)
test_dogs_dir = os.path.join(test_dir, 'dogs')
os.mkdir(test_dogs_dir)

fnames = ['cat.{}.jpg'.format(i) for i in range(TRAIN)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['cat.{}.jpg'.format(i) for i in range(TRAIN,TRAIN+VAL)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['cat.{}.jpg'.format(i) for i in range(TRAIN+VAL,TRAIN+VAL+TEST)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)


fnames = ['dog.{}.jpg'.format(i) for i in range(TRAIN)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET,fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src,dst)

fnames = ['dog.{}.jpg'.format(i) for i in range(TRAIN,TRAIN+VAL)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET,fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src,dst)

fnames = ['dog.{}.jpg'.format(i) for i in range(TRAIN+VAL,TRAIN+VAL+TEST)]
for fname in fnames:
    src = os.path.join(INPUT_DATASET,fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src,dst)