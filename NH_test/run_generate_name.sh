rm -rf *.h5
rm -rf *.jpg

cp hazy_images_cropped_padded/* .

python3 generate_data.py


ls *.h5 | shuf -n 157 | xargs -i mv {} ../NH_train

num=0; for i in *.h5; do mv "$i" "$(printf 'foo_%d' $num).${i#*.}"; ((num++)); done

num=0; for i in *.h5; do mv "$i" "$(printf '%d' $num).${i#*.}"; ((num++)); done

rm -rf *.jpg

cd ../NH_train

num=0; for i in *.h5; do mv "$i" "$(printf 'foo_%d' $num).${i#*.}"; ((num++)); done

num=0; for i in *.h5; do mv "$i" "$(printf '%d' $num).${i#*.}"; ((num++)); done

