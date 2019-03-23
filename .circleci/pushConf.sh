# Full Build Creation (Needed with workflow orchestration)
curl --user ${CIRCLE_TOKEN}: \
     --request POST \
     --form revision=93227bb5d358f49f4764cc4e0341e602e2fefc5f \
       https://circleci.com/api/v1.1/project/github/Korving-F/thesis-cicd-examples/build


# Simple job trigger
#curl --user ${CIRCLE_TOKEN}: \
#     --request POST \
#     --form config=@config.yml \
#     --form notify=false \
#     --form revision=93227bb5d358f49f4764cc4e0341e602e2fefc5f \
#       https://circleci.com/api/v1.1/project/github/Korving-F/thesis-cicd-examples/tree/master

