export PYTHONPATH=$PYTHONPATH:./models/


python3 train_aecrnet.py --testset "NH_test" --resume True --pre_model "NH_train.pk" --eval_dataset True --model_name "NH_train" --root "/home/sk5057/AECR-Net/"
