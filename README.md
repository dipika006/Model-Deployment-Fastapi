# FastAPI

FastAPI example project to test routes and specific endpoint `/predict` to verify notes fake or original.

## Data Exploration

This data is taken from UCI Machine Learning Repository. Data were extracted from images that were taken from genuine and forged banknote-like specimens.

Attribute Information:
* variance of Wavelet Transformed image (continuous)
* skewness of Wavelet Transformed image (continuous)
* curtosis of Wavelet Transformed image (continuous)
* entropy of image (continuous)
* class (integer)

The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images. The attributes are extracted attributes of each image.

Owner of database: Volker Lohweg (University of Applied Sciences, Ostwestfalen-Lippe, volker.lohweg '@' hs-owl.de)

## Setup

Make sure python3.9 or above is installed
Install requirements `pip install -r requirements-dev.txt`

## Model Generation

> $ python model/model_creation.py

This will generate a `classifier.pkl` file in model directory

## Start API

> $ python src/app.py

OR
> $ sh run.sh

OR
> $ PYTHONPATH=`pwd`/src && uvicorn src.app:app --reload

## Predict

1. Visit http://localhost:8000/docs
2. Try POST on `/predict`
3. Provide any data from the dataset as request body in below format and execute
```json
{
  "variance": 0.2,
  "skewness": 0.1,
  "curtosis": 0.5,
  "entropy": 0.001
}
```
4. Check the response -> will be like below
```json
{
  "prediction": "Fake note"
}
```

## Run Tests, validate imports, check black and flake8 standard

> $ tox

## Re-arrange sorting

> $ tox -e isort

## Autoformat as per black standard

> $ tox -e autoformat


