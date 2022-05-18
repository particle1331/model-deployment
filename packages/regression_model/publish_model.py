import os
import glob
import regression_model


for p in glob.glob('dist/*.whl'):
    try:
        os.system(f'curl -F package=@{p} {os.environ["GEMFURY_PUSH_URL"]}')
    except:
        raise Exception("Uploading package failed on file {p}")
