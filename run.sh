export PYTHONPATH=$PYTHONPATH:./models/


python3 train_aecrnet.py --testset "NH_test" --resume True --pre_model "NH_train.pk" --eval_dataset True