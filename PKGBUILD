# Script generated with Bloom
pkgdesc="ROS - The hector_slam metapackage that installs hector_mapping and related packages."
url='http://ros.org/wiki/hector_slam'

pkgname='ros-kinetic-hector-slam'
pkgver='0.3.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-hector-compressed-map-transport'
'ros-kinetic-hector-geotiff'
'ros-kinetic-hector-geotiff-plugins'
'ros-kinetic-hector-imu-attitude-to-tf'
'ros-kinetic-hector-map-server'
'ros-kinetic-hector-map-tools'
'ros-kinetic-hector-mapping'
'ros-kinetic-hector-marker-drawing'
'ros-kinetic-hector-nav-msgs'
'ros-kinetic-hector-slam-launch'
'ros-kinetic-hector-trajectory-server'
)

conflicts=()
replaces=()

_dir=hector_slam
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_slam $srcdir/hector_slam
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

