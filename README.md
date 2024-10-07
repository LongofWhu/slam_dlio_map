# **说明**
1.本项目配置基于dlio：https://github.com/vectr-ucla/direct_lidar_inertial_odometry；  
2.通过取消重新建立关键帧和子地图实现针对已有地图的定位算法；  
3.超参数设置在param.yaml文件中，通过设置loadFile=true可以读取到mapFile路径下的pcd文件，实现定位；  
4.通过设置loadFile=false，可以还原原本的dlio功能，对其建图没有任何影响；  
5.在param.yaml文件中，通过给定p_prior和q_prior可以给定小车初始位姿；  
6.打开rviz，通过2D Poze Estimate工具，可以给定初始位姿，当定位发生偏移时，也可通过该方法实现重新定位。
