git clone https://github.com/intel/isa-l.git
cd isa-l
./autogen.sh
./configure --prefix=/usr --libdir=/usr/lib64
make
sudo make install

git clone https://github.com/ebiggers/libdeflate.git
cd libdeflate
make
sudo make install

# get source (you can also use browser to download from master or releases)
git clone https://github.com/OpenGene/fastp.git

# build
cd fastp
make

# Install
sudo make install
