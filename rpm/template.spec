Name:           ros-kinetic-hector-slam
Version:        0.3.5
Release:        0%{?dist}
Summary:        ROS hector_slam package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_slam
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-hector-compressed-map-transport
Requires:       ros-kinetic-hector-geotiff
Requires:       ros-kinetic-hector-geotiff-plugins
Requires:       ros-kinetic-hector-imu-attitude-to-tf
Requires:       ros-kinetic-hector-map-server
Requires:       ros-kinetic-hector-map-tools
Requires:       ros-kinetic-hector-mapping
Requires:       ros-kinetic-hector-marker-drawing
Requires:       ros-kinetic-hector-nav-msgs
Requires:       ros-kinetic-hector-slam-launch
Requires:       ros-kinetic-hector-trajectory-server
BuildRequires:  ros-kinetic-catkin

%description
The hector_slam metapackage that installs hector_mapping and related packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jun 24 2016 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

