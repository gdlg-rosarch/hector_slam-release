# Script generated with Bloom
pkgdesc="ROS - hector_compressed_map_transport provides means for transporting compressed map data through the use of image_transport."
url='http://ros.org/wiki/hector_compressed_map_transport'

pkgname='ros-kinetic-hector-compressed-map-transport'
pkgver='0.3.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hector-map-tools'
'ros-kinetic-image-transport'
'ros-kinetic-nav-msgs'
'ros-kinetic-sensor-msgs'
)

depends=('eigen3'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hector-map-tools'
'ros-kinetic-image-transport'
'ros-kinetic-nav-msgs'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=hector_compressed_map_transport
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_compressed_map_transport $srcdir/hector_compressed_map_transport
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

