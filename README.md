# popTextureDS
Generating synthetic drip Textures using frequency sweep

# User instructions

  >> git clone https://github.com/prashanthtr/dripTextureDS.git

  >> cd dripTextureDS/

  >> conda create -n dripTextureDS python=3.6 ipykernel

  >> conda activate dripTextureDS

  >> pip install -r requirements.txt --src '.' (please run twice - due to numba dependency error)

# Setup and run jupyter notebook

>> pip install jupyter

>> python -m ipykernel install --user --name dripTextureDS

>> jupyter notebook

>> Select *popTexture-notebook.ipynb* in the browser interface

# Generate files from commandline

>> python generate.py config_file.json
