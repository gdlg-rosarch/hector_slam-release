# Script generated with Bloom
pkgdesc="ROS - hector_mapping is a SLAM approach that can be used without odometry as well as on platforms that exhibit roll/pitch motion (of the sensor, the platform or both). It leverages the high update rate of modern LIDAR systems like the Hokuyo UTM-30LX and provides 2D pose estimates at scan rate of the sensors (40Hz for the UTM-30LX). While the system does not provide explicit loop closing ability, it is sufficiently accurate for many real world scenarios. The system has successfully been used on Unmanned Ground Robots, Unmanned Surface Vehicles, Handheld Mapping Devices and logged data from quadrotor UAVs."
url='http://ros.org/wiki/hector_mapping'

pkgname='ros-kinetic-hector-mapping'
pkgver='0.3.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'eigen3'
'ros-kinetic-catkin'
'ros-kinetic-laser-geometry'
'ros-kinetic-message-filters'
'ros-kinetic-message-generation'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-visualization-msgs'
)

depends=('boost'
'eigen3'
'ros-kinetic-laser-geometry'
'ros-kinetic-message-filters'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=hector_mapping
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_mapping $srcdir/hector_mapping
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

