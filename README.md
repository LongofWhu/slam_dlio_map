# **说明**  
1. 本项目基于dlio:https://github.com/vectr-ucla/direct_lidar_inertial_odometry项目开发，项目所需配置见dlio；  
2. 该分支通过添加权重计算函数，并将权重加入到GICP算法迭代过程中，使得算法能够针对反射率高的物体（反光板）进行更好的匹配；  
3. 该分支在Param.yaml文件中添加超参数接口，通过weight_max, weight_min, intensityThreshold分别设置不同反射率物体的权重占比和反射率赋权阈值。
