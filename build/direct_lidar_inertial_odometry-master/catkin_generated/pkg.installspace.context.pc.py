# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs;sensor_msgs;geometry_msgs;pcl_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-ldirect_lidar_inertial_odometry;-lnano_gicp;-lnanoflann".split(';') if "-ldirect_lidar_inertial_odometry;-lnano_gicp;-lnanoflann" != "" else []
PROJECT_NAME = "direct_lidar_inertial_odometry"
PROJECT_SPACE_DIR = "/home/long/Project/dlio/install"
PROJECT_VERSION = "1.1.1"
