from face_bbox import *
from pylearn2.utils.iteration import SequentialSubsetIterator

def test1():
    which_set = "train"
    path = "/data/lisatmp/data/faces_bbox/test_face.h5"
    start = 0
    stop = 2100
    size_of_receptive_field = [128, 128]
    stride = 8
    use_output_map = True

    batch_size = 100
    num_batches = 5
    mode = SequentialSubsetIterator
    targets1 = []
    targets2 = []

    dataset1 = FaceBBox(which_set=which_set,
                        start=start,
                        stop=stop,
                        use_output_map=use_output_map,
                        stride=stride,
                        size_of_receptive_field=size_of_receptive_field,
                        path=path)


    print "Dataset 1"
    for data in dataset1.iterator(batch_size=batch_size, num_batches=num_batches, mode=mode,
            targets=True):
        targets1.append(data[1])
    del dataset1

    dataset2 = FaceBBox(which_set=which_set,
                        start=start,
                        stop=stop,
                        bbox_conversion_type="Exhaustive",
                        use_output_map=use_output_map,
                        stride=stride,
                        size_of_receptive_field=size_of_receptive_field,
                        path=path)


    print "Dataset 2"
    for data in dataset2.iterator(batch_size=batch_size, num_batches=num_batches, mode=mode,
            targets=True):
        targets2.append(data[1])


    import ipdb; ipdb.set_trace()

if __name__=="__main__":
    test1()
