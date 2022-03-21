export PYTHONPATH=$PYTHONPATH:./models/


#Test command
#python3 train_aecrnet.py --testset "NH_test" --resume True --pre_model "NH_train.pk" --eval_dataset True --model_name "NH_train" --root "/home/sk5057/AECR-Net/"


python3 train_aecrnet.py --resume True --trainset "NH_train" --testset "NH_test" --pre_model "NH_train.pk" --model_name "NH_train" --root "/home/sk5057/AECR-Net/" --eval_step 30 --bs 2
