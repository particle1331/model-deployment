import os
import glob


for p in glob.glob('dist/*.whl'):
    try:
        os.system(f'curl -F package=@{p} {os.environ["GEMFURY_PUSH_URL"]}')
    except:
        raise Exception("Uploading package failed on file {p}")

os.system(f"""curl --request POST \
	--url https://circleci.com/api/v2/project/vcs-slug/org-name/repo-name/pipeline \
	--header 'Circle-Token: {os.environ["CIRCLE_TOKEN"]}' \
	--header 'content-type: application/json' \
	--data '{"parameters":{"run_regression_model":false, "run_deploy_app":true}}'
""")
