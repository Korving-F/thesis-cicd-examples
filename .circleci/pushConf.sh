curl --user ${CIRCLE_TOKEN}: \
     --request POST \
     --form revision=c35b2c8ee90cda4755810391add9d08085d734b1 \
     --form config=@config.yml \
     --form notify=false \
       https://circleci.com/api/v1.1/project/github/Korving-F/thesis-cicd-examples/tree/master
