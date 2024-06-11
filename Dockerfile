FROM ubuntu:20.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
git \
python3-pip \
ffmpeg \
libsm6 \
libxext6 \
curl \
unzip \
wget \
&& rm -rf /var/lib/apt/lists/*

# Install basic dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    gnupg \
    build-essential 

# Add NVIDIA package repositories
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin && \
    mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    wget https://developer.download.nvidia.com/compute/cuda/11.4.2/local_installers/cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb && \
    dpkg -i cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb && \
    apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub && \
    apt-get update

# Install CUDA
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    cuda 

# Set environment variables
ENV PATH=/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}

# installing gdown for downloading files from google drive
RUN pip install gdown --upgrade

# cloning repository
RUN git clone https://github.com/stefanopini/simple-HRNet.git
WORKDIR /simple-HRNet
RUN pip install -r requirements.txt
# RUN apt update && ap install -y vlc

# adding yolov3
RUN git submodule update --init --recursive && \ 
cd /simple-HRNet/models_/detectors/yolo && \
pip install -q -r requirements.txt

# adding yolov3 weights
RUN cd /simple-HRNet/models_/detectors/yolo/weights && \
wget -c https://pjreddie.com/media/files/yolov3.weights && \
wget -c https://pjreddie.com/media/files/yolov3-tiny.weights && \
wget -c https://pjreddie.com/media/files/darknet53.conv.74

# downloading weights for hrnet pre-trained weights
RUN cd /simple-HRNet && \
pip install --upgrade --no-cache-dir gdown && \
mkdir weights && cd weights && \
gdown 1UoJhTtjHNByZSm96W3yFTfU5upJnsKiS && \
gdown 1zYC7go9EV0XaSlSBjMaiyE_4TcHc_S38 && \
gdown 1_wn2ifmoQprBrFvUCDedjPON4Y6jsN-v

# downloading testing video
RUN cd /simple-HRNet && \
wget https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4

# making output dir for csv 
RUN mkdir output

RUN apt update && apt install -y python3.8-dev

# building nms module for running the training script
RUN cd misc/nms; python3 setup_linux.py build_ext --inplace

# adding the ./misc/nms directory in the PYTHONPATH variable
RUN export PYTHONPATH="/simple-HRNet/misc/nms:$PYTHONPATH"

RUN cd /simple-HRNet && \
pip install json_tricks && \
pip install pycocotools