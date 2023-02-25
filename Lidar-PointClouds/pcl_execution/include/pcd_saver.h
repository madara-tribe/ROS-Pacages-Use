#include <stdio.h>
#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

class Saver{
public:
	void save(const std::string &filename, const pcl::PointCloud<pcl::PointXYZ> &cloud){
	    pcl::io::savePCDFileBinary(filename, cloud);
        }	    
};
