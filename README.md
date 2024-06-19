# veld_chain__demo__word2vec

self-link shortened: https://t.ly/VZyke

### about

This a demo repo of the VELD design, that trains a word2vec model from scratch.

It integrates three processes: 
- veld_preprocess: downloads the bible and transforms it to training data
- veld_train: trains a word2vec model based on this data
- veld_infer: uses the model to run a jupyter notebook for inference.

### how to run

clone this repo, recursively with all submodules
```
git clone --recurse-submodules https://github.com/acdh-oeaw/veld_chain__demo__word2vec.git
```

Do preprocessing, which saves the data into `./veld_data__demo__training_data/bible.txt`
```
docker compose -f veld_preprocess.yaml up
```

Do training (this will take 5-15 minutes, depending on hardware), which saves a model into
`./veld_data__demo__word2vec_model/bible.word2vec`.
```
docker compose -f veld_train.yaml up
```

Do inference, by running a jupyter notebook, which can be opened at http://localhost:8888/ , there
simply execute all cells and have a look at the results.
```
docker compose -f veld_infer.yaml up
```

