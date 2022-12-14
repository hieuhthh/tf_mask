import zipfile

from utils import *

settings = get_settings()
globals().update(settings)

from_dir = path_join(route, 'download')
des = path_join(route, 'unzip')
mkdir(des)

filename = 'AFDB_masked_face_dataset'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

filename = 'final'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

filename = 'masked_ms1m'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

filename = 'RWMFD_part_2_pro'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

# zip_file = '/home/lap14880/face_bucket_huy/glint360k_224_copy.zip'
# with zipfile.ZipFile(zip_file, 'r') as zip_ref:
#     zip_ref.extractall(des)