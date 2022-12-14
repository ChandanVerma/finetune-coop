# Tutorial to Fine-tune CoOp

# Steps to take
1) Follow installation instructions in: https://github.com/KaiyangZhou/CoOp.
    - Install `dassl`
    - Run `pip install -r requirements.txt` under `CoOp/`
2) The following steps has been done in this repo so you don't need to do it
    - Clone repo https://github.com/KaiyangZhou/CoOp
    - Create a folder `./CoOp/data/tagging`
    - Added the files:
        -  `./CoOp/configs/datasets/tagging.yaml`
        - `./CoOp/datasets/tagging.py`
    - Updated scripts:
        - `./CoOp/scripts/coop/eval.sh`
        - `./CoOp/scripts/coop/main.sh`
        - `./CoOp/train.py`
3) Prepare CoOp dataset following example in `001_prepare_coop_dataset.ipynb`.
4) Finetune CoOp:
```
cd CoOp/scripts/coop
bash main.sh tagging vit_b16_ep50 end 16 16 False
```

# Performing evaluation/inference
Update model file in https://gitlab.com/lomotif/datascience/poc/integrated-content-moderation-tagging/-/blob/feat_add_documentation/src/tag_and_moderate.py:
```
self.model_filename = "model.pth.tar-50"
```
And run CoOp-CLIP inference.