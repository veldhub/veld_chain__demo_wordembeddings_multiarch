# veld_chain__demo_wordembeddings_multiarch

### about

This a demo repo of the VELD design that trains word embedding models from scratch.

It integrates three processes: 
- [veld_preprocess](./veld_preprocess.yaml): downloads the bible and transforms it to training data
- [veld_train](./veld_train.yaml): trains a word2vec model based on this data
- [veld_infer](./veld_infer.yaml): uses the model to run a jupyter notebook for inference.

### how to run

clone this repo, recursively with all submodules :
```
git clone --recurse-submodules https://github.com/acdh-oeaw/veld_chain__demo__word2vec.git
```

enter it :
```
cd veld_chain__demo__word2vec # or `dir` on windows
```

Do preprocessing, which saves the data into `./veld_data__demo__training_data/bible.txt` :
```
docker compose -f veld_preprocess.yaml up
```
(note: if you have an older docker version, you might need to call `docker-compose` instead)

Do training (this will take 5-15 minutes, depending on hardware), which saves a model into
`./veld_data__demo__word2vec_model/bible.word2vec` :
```
docker compose -f veld_train.yaml up
```

Do inference, by running a jupyter notebook, which can be opened at http://localhost:8888/ , there
simply execute all cells and have a look at the results :
```
docker compose -f veld_infer.yaml up
```

