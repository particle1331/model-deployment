import os
import glob


GEMFURY_PUSH_URL = os.environ['GEMFURY_PUSH_URL']

for p in glob.glob('dist/*.whl'):
    try:
        os.system(f'curl -F package=@{p} {GEMFURY_PUSH_URL}')
    except:
        raise Exception("Uploading package failed on file dist/{p}")
