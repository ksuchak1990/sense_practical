input_frames:
	cd ./data/inputs/ && tar -xzf frames.tar.gz -C ./frames

env:
	conda env export --from-history > environment.yml

clean:
	cd ./data/inputs/frames/ && rm -rf *.dat
