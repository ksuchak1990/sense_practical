frames: input_frames output_frames

input_frames:
	cd ./data/inputs/ && tar -xzf frames.tar.gz -C ./frames

output_frames:
	python ./src/utils/data_manipulation.py

env:
	conda env export --from-history > environment.yml

clean:
	cd ./data/inputs/frames/ && rm -rf *.dat
	cd ./data/outputs/frames/ && rm -rf *.dat
	cd ./data/outputs/frames/ && rm -rf *.csv
	cd ./data/outputs/ && rm *.csv
