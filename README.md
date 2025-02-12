## Project Workflow

1. update config.yaml/yml
2. update schema.yaml/yml
3. update params.yaml/yml
4. update the entity
5. update the configuration manager in src config 
6. update the component
7. update the pipeline
8. update the main.py
9. update the app.py



##### If finish the folder structuring then create new conda enviroment

>- create 

```bash
conda create -n mlproj python=3.8 -y
```

>- activate 

```bash
conda conda activate mlproj
```

>- deactivate

```bash
conda conda deactivate
```

##### After exicute requirements.txt file
```bash
pip install -r requirements.txt
```
##### If you dont't have dataset then download it
>- Dataset link 
```bash
https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009/data
```

##### Next, compleinting data ingestion, data validation, data transformation, model training and model evaluation stages and also related pipelines create user UIs. After that modify ```app.py``` and run it

```bash
python app.py
```