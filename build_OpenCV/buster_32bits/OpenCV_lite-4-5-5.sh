#!/bin/bash
set -e
echo "Installing OpenCV 4.5.5 on your Raspberry Pi 32-bit OS"
echo "It will take minimal 2.0 hour !"
cd ~
# install the dependencies
echo "Installing dependancies"

# check for updates
sudo apt-get -y update
sudo apt-get -y upgrade
# general tools (35.8 MB)
sudo apt-get install -y build-essential cmake git pkg-config
# if you want to get OpenCV working in python or python3 (208 MB)
sudo apt-get install -y python3-dev python3-numpy
# The latest Debian 11, Bullseye don't support python2 full
# don't try to install if you're having a Raspberry Bullseye OS
sudo apt-get install -y python-dev  python-numpy
# image formats (0.9 MB)
sudo apt-get install -y libjpeg-dev libpng-dev
# video formats (32.1 MB)
sudo apt-get install -y libavcodec-dev libavformat-dev
sudo apt-get install -y libswscale-dev libdc1394-22-dev
# video back engine (0.6 MB)
sudo apt-get install -y libv4l-dev v4l-utils
# the GTK+2 GUI (175 MB)
sudo apt-get install -y libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
# parallel framework (2.7 MB)
# don't install if your having a 1 core CPU (like RPi zero)
sudo apt-get install -y libtbb2 libtbb-dev


# download the latest version
cd ~ 
sudo rm -rf opencv*
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.5.zip 
# unpack
unzip opencv.zip 
# some administration to make life easier later on
mv opencv-4.5.5 opencv
# clean up the zip files
rm opencv.zip

# set install dir
cd ~/opencv
mkdir build
cd build

# run cmake
echo "Run cmake"
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D BUILD_ZLIB=ON \
-D BUILD_OPENMP=ON \
-D BUILD_TIFF=OFF \
-D BUILD_OPENJPEG=OFF \
-D BUILD_JASPER=OFF \
-D BUILD_OPENEXR=OFF \
-D BUILD_WEBP=OFF \
-D BUILD_TBB=ON \
-D BUILD_IPP_IW=OFF \
-D BUILD_ITT=OFF \
-D WITH_OPENMP=ON \
-D WITH_OPENCL=OFF \
-D WITH_AVFOUNDATION=OFF \
-D WITH_CAP_IOS=OFF \
-D WITH_CAROTENE=OFF \
-D WITH_CPUFEATURES=OFF \
-D WITH_EIGEN=OFF \
-D WITH_GSTREAMER=ON \
-D WITH_GTK=ON \
-D WITH_IPP=OFF \
-D WITH_HALIDE=OFF \
-D WITH_VULKAN=OFF \
-D WITH_INF_ENGINE=OFF \
-D WITH_NGRAPH=OFF \
-D WITH_JASPER=OFF \
-D WITH_OPENJPEG=OFF \
-D WITH_WEBP=OFF \
-D WITH_OPENEXR=OFF \
-D WITH_TIFF=OFF \
-D WITH_OPENVX=OFF \
-D WITH_GDCM=OFF \
-D WITH_TBB=ON \
-D WITH_HPX=OFF \
-D WITH_EIGEN=OFF \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_VTK=OFF \
-D WITH_QT=OFF \
-D BUILD_opencv_python3=ON \
-D BUILD_opencv_java=OFF \
-D BUILD_opencv_gapi=OFF \
-D BUILD_opencv_objc=OFF \
-D BUILD_opencv_js=OFF \
-D BUILD_opencv_ts=OFF \
-D BUILD_opencv_dnn=OFF \
-D BUILD_opencv_calib3d=OFF \
-D BUILD_opencv_objdetect=OFF \
-D BUILD_opencv_stitching=OFF \
-D BUILD_opencv_ml=OFF \
-D BUILD_opencv_world=OFF \
-D BUILD_EXAMPLES=OFF \
-D OPENCV_ENABLE_NONFREE=OFF \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF ..

# run make
echo "Run make using 2 CPUs"
make -j4
sudo make install
sudo ldconfig

# cleaning (frees 300 MB)
echo "Cleaning"
make clean
sudo apt-get update

echo "Congratulations!"
echo "You've successfully installed last OpenCV on your Raspberry Pi 32-bit OS"
