import os
import glob


for p in glob.glob('dist/*.whl'):
    try:
        os.system(f'curl -F package=@{p} {os.environ["GEMFURY_PUSH_URL"]}')
    except:
        raise Exception("Uploading package failed on file {p}")

# CircleCI API trigger
request = f"""curl --request POST \
  'https://circleci.com/api/v2/project/github/particle1331/model-deployment/pipeline' \
  -H f'Circle-Token: {os.environ["CIRCLE_TOKEN"]}' \
  -H 'Content-Type: application/json' \
  -d '{{
    "parameters": {{
      "run_regression_model": false,
      "run_deploy_app": true
    }}
}}'
"""
os.system(request)
