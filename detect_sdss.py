import os
import pandas as pd
from fits_operator import SDSS_photo_download_process
# from fits_operator import reproject_process
from astropy.coordinates import SkyCoord
import astropy.units as u


def download_SDSS_images_from_csv(csv_file: str, base_url: str, save_dir: str, band: list[str] = None) -> None:
    data = pd.read_csv(csv_file)
    download_results = {b: [] for b in band}
    for index, row in data.iterrows():
        unique_id = str(int(row['index']))  
        rerun = str(int(row['rerun']))        
        run = str(int(row['run']))     
        camcol = str(int(row['camcol']) )    
        field = str(int(row['field']))       

        band_success = {b: False for b in band}

        SDSS_photo_download_process(
            unique_id=unique_id,
            base_url=base_url,
            run=run,
            rerun=rerun,
            camcol=camcol,
            field=field,
            save_dir=save_dir,
            band=band
        )
        for b in band:
            file_path = os.path.join(save_dir,
                    f"{unique_id}_{rerun}_{run}_{camcol}_{field}/frame-{b}-{run.zfill(6)}-{camcol}-{field.zfill(4)}.fits.bz2")
            if os.path.exists(file_path):  
                download_results[b].append(unique_id)
    download_df = pd.DataFrame(dict([(b, pd.Series(download_results[b])) for b in band]))
    download_df.to_csv('detect.csv', index=False)

# Example call
csv_file = 'Replace with your CSV file path'  
base_url = 'https://data.sdss.org/sas/dr17/eboss/photoObj/frames'  # The basic URL of SDSS
save_dir = 'Your download and save directory'  # Download and Save Directory
band = ['u', 'g', 'r', 'i', 'z']  # The required download bands

# Call the function to process the CSV file and download the images
download_SDSS_images_from_csv(csv_file, base_url, save_dir, band)

