Name:           ros-indigo-fetch-gazebo-demo
Version:        0.5.1
Release:        0%{?dist}
Summary:        ROS fetch_gazebo_demo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/fetch_gazebo_demo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-fetch-gazebo
Requires:       ros-indigo-fetch-moveit-config
Requires:       ros-indigo-fetch-navigation
Requires:       ros-indigo-moveit-python
Requires:       ros-indigo-simple-grasping
Requires:       ros-indigo-teleop-twist-keyboard
BuildRequires:  ros-indigo-catkin

%description
Demos for fetch_gazebo package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jun 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.1-0
- Autogenerated by Bloom

* Sat Jun 13 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.0-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.4-0
- Autogenerated by Bloom

* Wed Jun 10 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.3-0
- Autogenerated by Bloom

* Sat Jun 06 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.2-0
- Autogenerated by Bloom

* Fri Jun 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.1-0
- Autogenerated by Bloom

* Fri Jun 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.0-0
- Autogenerated by Bloom

