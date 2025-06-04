# ![veld chain](https://raw.githubusercontent.com/veldhub/.github/refs/heads/main/images/symbol_V_letter.png) veld_chain__demo_wordembeddings_multiarch

## TL;DR

run it all with:

**note: older versions of docker require the `docker-compose` instead of `docker compose`**

```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__demo_wordembeddings_multiarch.git
cd veld_chain__demo_wordembeddings_multiarch
docker compose -f veld_step_all.yaml up
```

## about

This is a [VELD](https://zenodo.org/records/13322913) demonstration. For more real-world applications, see https://github.com/veldhub .

It contains several chain velds, based on different isolated code stacks, which train word
embeddings from scratch. As training data, the bible is used and preproccessed, and the underlying
word embeddings architectures used are [fastText](https://fasttext.cc/), 
[GloVe](https://nlp.stanford.edu/projects/glove/), and 
[word2vec](https://radimrehurek.com/gensim/models/word2vec.html) . After training, a jupyter 
notebook is launched to compare the differently trained vectors on a few sample words. 

The outcome of this training setup on such a small training data set is meant to be illustrative of 
the reproducibility of the workflows, rather than claiming any deeper insight into the word 
contexts of the bible itself.

The very final step, an analysis of the entire training, is encapsulated in
[./code/analyse_vectors/notebooks/analyse_vectors.ipynb](./code/analyse_vectors/notebooks/analyse_vectors.ipynb) .

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

Clone this repo with all its submodules
```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__demo_wordembeddings_multiarch.git
```

## how to reproduce

The entirety of the veldified workflows in this repo can be executed in two ways:
- all together in one [multi chain](#multi-chain)
- sequentially by executing each [chain individually](#individual-chains)

See each respective veld yaml file for more details.

### multi chain

**[./veld_step_all.yaml](./veld_step_all.yaml)** 

Runs all chains in one multi chain. It simply references the individual chains with docker compose's
`extends` functionality.

```
docker compose -f veld_step_all.yaml up
```

### individual chains

**[./veld_step_1_download.yaml](./veld_step_1_download.yaml)** 

Downloads the bible from https://raw.githubusercontent.com/mxw/grmr/master/src/finaltests/bible.txt
.

```
docker compose -f veld_step_1_download.yaml up
```

**[./veld_step_2_preprocess.yaml](./veld_step_2_preprocess.yaml)** 

Cleans the downloaded bible and transforms it into a format compatible for training by the three 
word embeddings architectures.

```
docker compose -f veld_step_2_preprocess.yaml up
```

**[./veld_step_3_train_fasttext.yaml](./veld_step_3_train_fasttext.yaml)** 

Trains a fastText model. Also exports its vectors into a pickle as a python dict, with keys
being the word and values being the multidimensional word vector.

```
docker compose -f veld_step_3_train_fasttext.yaml up
```

**[./veld_step_4_train_glove.yaml](./veld_step_4_train_glove.yaml)** 

Trains a GloVe model. Also exports its vectors into a pickle as a python dict, with keys
being the word and values being the multidimensional word vector.

```
docker compose -f veld_step_4_train_glove.yaml up
```

**[./veld_step_5_train_word2vec.yaml](./veld_step_5_train_word2vec.yaml)** 

Trains a word2vec model. Also exports its vectors into a pickle as a python dict, with keys
being the word and values being the multidimensional word vector.

```
docker compose -f veld_step_5_train_word2vec.yaml up
```

**[./veld_step_6_analyse_vectors.yaml](./veld_step_6_analyse_vectors.yaml)** 

Launches a jupyter notebook at http://localhost:8888/ which loads the previously exported word 
vectors and compares them numerically and visually on some sample words. The notebook is persisted 
at: 
[./code/analyse_vectors/notebooks/analyse_vectors.ipynb](./code/analyse_vectors/notebooks/analyse_vectors.ipynb) .

After reproducing the entire previous sequences yourself and execution of the notebook, feel free to
save the notebook and compare the resulting differences with `git diff
./code/analyse_vectors/notebooks/analyse_vectors.ipynb`, where the reproduced vector similarities
will have only slight differences to the record of previously trained ones. This difference is due
to randomization within the training, but should be small enough to indicate approximate
reproduction.

```
docker compose -f veld_step_6_analyse_vectors.yaml up
```

