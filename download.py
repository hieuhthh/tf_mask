import gdown

from utils import *

settings = get_settings()
globals().update(settings)

des = path_join(route, 'download')
mkdir(des)

url = "https://drive.google.com/file/d/1H2aN-CHRoU6W4NsOzxAKdO-FI4QK0Du-/view?usp=share_link"
output = f"{des}/AFDB_masked_face_dataset.zip"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

url = "https://drive.google.com/file/d/1Em2UzFHNmygV8POVg7SeAkN6oW6657mT/view?usp=sharing"
output = f"{des}/final.zip"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

url = "https://drive.google.com/file/d/1UR33CAMEz21QqtDL2QXqSo0HdvO0AoTL/view?usp=share_link"
output =  f"{des}/masked_ms1m.zip"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

url = "https://drive.google.com/file/d/1sf4-dGjqlowGt_rlSMiHCRLo_wwXqeG4/view?usp=share_link"
output =  f"{des}/RWMFD_part_2_pro.zip"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)