export PYTHONPATH=$PYTHONPATH:./models/


#Test command
python3 test_aecrnet.py --testset "NH_test" --trainset "NH_train" --resume True --pre_model "NH_train.pk.best" --eval_dataset True --model_name "NH_train" --root "/home/sk5057/AECR-Net/"


#python3 train_aecrnet.py --resume True --trainset "NH_train" --testset "NH_test" --pre_model "NH_train.pk" --model_name "NH_train" --root "/home/sk5057/AECR-Net/" --eval_step 30 --bs 1 --lr 0.0001

