import os
from os.path import exists, join, expanduser
# import git
from git import Repo
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Repo.clone_from("https://github.com/r9y9/deepvoice3_pytorch", "deepvoice3_pytorch")
# Clone
name = "deepvoice3_pytorch"
# if not exists(name):
# #   git.Git().clone('https://github.com/r9y9/$name')
#   git clone https://github.com/r9y9/$name
#   import git
# git.Git("./deepvoice3_pytorch").clone("https://github.com/r9y9/deepvoice3_pytorch")
arr = os.listdir()
print(arr)
retval = os.getcwd()
print(retval)
# install('torch==1.7.0')
# pip install -q torch==1.7.0
# os.chdir(join(os.getcwd(), name))
# os.chdir(name)
# ! ls -la

# ! git checkout master --quiet

# preset = "./presets/deepvoice3_vctk.json"
# ! ls -la
# ! cp -v $preset .
preset = "./deepvoice3_vctk.json"

# And then git checkout to the working commit
# This is due to the model was trained a few months ago and it's not compatible
# with the current master. python3 --version

# ! git checkout 0421749 --quiet
# Nov 10th 9:55pm - Aruneesh // Removing the -q (quiet option) to look at what pip install is really doing
# ! pip install  -e '.[train]'

import hparams
import json

# Newly added params. Need to inject dummy values
for dummy, v in [("fmin", 0), ("fmax", 0), ("rescaling", False),
                 ("rescaling_max", 0.999), 
                 ("allow_clipping_in_normalization", False)]:
  if hparams.hparams.get(dummy) is None:
    hparams.hparams.add_hparam(dummy, v)
    
# Load parameters from preset
with open(preset) as f:
  hparams.hparams.parse_json(f.read())

# Tell we are using multi-speaker DeepVoice3
hparams.hparams.builder = "deepvoice3_multispeaker"
  
# Inject frontend text processor
import synthesis
import train
from deepvoice3_pytorch import frontend
synthesis._frontend = getattr(frontend, "en")
train._frontend =  getattr(frontend, "en")

# alises
fs = hparams.hparams.sample_rate
hop_length = hparams.hparams.hop_size


def tts(model, text, p=0, speaker_id=0, fast=False, figures=True):
  from synthesis import tts as _tts
  waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
  if figures:
      visualize(alignment, spectrogram)
  IPython.display.display(Audio(waveform, rate=fs))
  
def visualize(alignment, spectrogram):
  label_fontsize = 16
  figure(figsize=(16,16))

  subplot(2,1,1)
  imshow(alignment.T, aspect="auto", origin="lower", interpolation=None)
  xlabel("Decoder timestamp", fontsize=label_fontsize)
  ylabel("Encoder timestamp", fontsize=label_fontsize)
  colorbar()

  subplot(2,1,2)
  librosa.display.specshow(spectrogram.T, sr=fs, 
                           hop_length=hop_length, x_axis="time", y_axis="linear")
  xlabel("Time", fontsize=label_fontsize)
  ylabel("Hz", fontsize=label_fontsize)
  tight_layout()
  colorbar()

from train import build_model
from train import restore_parts, load_checkpoint
import importlib
importlib.reload(train)

from deepvoice3_pytorch import frontend
synthesis._frontend = getattr(frontend, "en")
train._frontend =  getattr(frontend, "en")

print("HERE - 1")
print("HERE - 2")
model = build_model()
model = load_checkpoint(checkpoint_path, model, None, True)
print("HERE - 3")
print(model)

text = "Hi Aditya good morning, this is the progress with a sample data set and sample trained model.Generative adversarial network or variational auto-encoder.Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child. A text-to-speech synthesis system typically consists of multiple stages, such as a text analysis frontend, an acoustic model and an audio synthesis module."

N = 2
# Nov 10th 11pm - Aruneesh / testing with only 1 speaker to start with
# N= 108
print("Synthesizing \"{}\" with {} different speakers".format(text, N))
for speaker_id in range(N):
  print(speaker_id)
  tts(model, text, speaker_id=speaker_id, figures=False)

import importlib
importlib.reload(synthesis)

def tts(model, text, p=0, speaker_id=0, fast=False, figures=True):
  from synthesis import tts as _tts

  waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
  if figures:
      visualize(alignment, spectrogram)
  IPython.display.display(Audio(waveform, rate=fs))


tts(model, text, speaker_id=0, figures=True)