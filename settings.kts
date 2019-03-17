package _Self.buildTypes

import jetbrains.buildServer.configs.kotlin.v2018_2.*
import jetbrains.buildServer.configs.kotlin.v2018_2.buildSteps.script
import jetbrains.buildServer.configs.kotlin.v2018_2.triggers.vcs

object Build : BuildType({
    name = "Thesis-Example-Pipeline"

    vcs {
        root(Git172208193thesisExamplesThesisCicdPocGitRefsHeadsMaster)
    }
steps {
    script {
        name = "Build"
        scriptContent = """
            echo 'Building..'
            docker build -t teamcity-cicd-container-${'$'}BUILD_VCS_NUMBER .
        """.trimIndent()
    }
    script {
        name = "Run"
        scriptContent = """
            echo 'Running..'
            docker kill ${'$'}(docker ps -q) || true
            docker rm ${'$'}(docker ps -a -q) || true
            docker run -dt -p 8282:80 -v ${'$'}PWD:/tmp/ --name teamcityCICDContainer teamcity-cicd-container-${'$'}BUILD_VCS_NUMBER
        """.trimIndent()
    }
    script {
        name = "Test"
        scriptContent = """
            echo 'Testing...'
            sudo apt-get update -qy
            sudo apt-get install -y python3-dev python3-pip
            sudo pip3 install pytest pytest-cov teamcity-messages
            pytest --teamcity --cov-branch --cov=example/ tests/
        """.trimIndent()
    }
    script {
        name = "Clean"
        scriptContent = """
            echo 'Cleaning up...'
            docker kill ${'$'}(docker ps -q) || true
            docker rm ${'$'}(docker ps -a -q) || true
        """.trimIndent()
    }
}
    triggers {
        vcs {
        }
    }
})
