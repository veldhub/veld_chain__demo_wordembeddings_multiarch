# veld_chain__demo_wordembeddings_multiarch

## TL;DR

run it all with:

**note: older versions of docker require the `docker-compose` instead of `docker compose`**

```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__demo_wordembeddings_multiarch.git
cd veld_chain__demo_wordembeddings_multiarch
docker compose -f veld_step_all.yaml up
```

## about

This repo contains [chain velds](https://zenodo.org/records/13322913) encapsulating training of 
word embedding models from scratch.

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

Clone this repo with all its submodules
```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__demo_wordembeddings_multiarch.git
```

## how to reproduce

The following chain velds were used. Open the respective veld yaml file for more information.

**[./veld_step_all.yaml](./veld_step_all.yaml)** 

Runs all chains sequentially

```
docker compose -f veld_step_all.yaml up
```

