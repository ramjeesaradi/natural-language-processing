gcr.io/alert-maker-188312/nlp

docker tag fce67b2d9d37 gcr.io/alert-maker-188312/nlp
docker push gcr.io/alert-maker-188312/nlp

docker tag fce67b2d9d37 ramjeesaradi/mooc_exercises:firsttry
docker push ramjeesaradi/mooc_exercises

docker run -it -p 8080:80 --name coursera-aml-nlp -v $PWD:/root/coursera gcr.io/alert-maker-188312/nlp

gcloud compute --project "alert-maker-188312" ssh --zone "europe-west1-b" "nlp-docker-deployment"

docker exec -it nlp-docker-deployment bash

http://35.210.122.124:8080/

docker run -it -p 8080:8080 --name coursera-aml-nlp -v $PWD:/root/coursera gcr.io/alert-maker-188312/nlp
