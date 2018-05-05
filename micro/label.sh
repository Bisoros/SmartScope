for x in tf_files/to_label/*
do
	printf "$x:\n"
	python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image="$x"
	printf "________________________________\n"
done