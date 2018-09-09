# ITU Racing Ekibi Çalışmalarım #

## LiDAR

#### Hedef
* Visual odometry elde etmek
* Real-time mapping

#### Çalışmalar
* loam (LiDAR Odometry and Mapping) için ilgilendiğimiz kod: ```https://github.com/laboshinl/loam_velodyne```
* OctoMap ile haritalama: ```https://github.com/OctoMap/octomap_mapping```
* PCL ile filtreleme çalışmalarım: ```https://github.com/enesdemirag/point-cloud-filters```

## Lane Detection

#### Hedef
* Yoldaki şeritleri algılayarak ikisini ortalamak için açı ve yön çıktısı verecek bir kod yazmak.
    * Işık yoğınluğu, açısı, ortamın aydınlığı zemindeki şeritlerin tonunu değiştiriyor ve algılamak zorlaşıyor. Belki de adaptif bir filtre kodu yazılabilir.

#### Çalışmalar
* OpenCV ile ilgili çalışmalarım: ```https://github.com/enesdemirag/opencv_lectures```
* Üzerinde çalışıp optimize etmeye çalıştığımız kod: ```https://github.com/shawpan/lane-detector```

![alt text](https://github.com/ituracingteam/lane_detection/src/test_files/flowchart.png "flowchart")

1. Kamera görüntüsünü almak
2. OpenCV ile şerit renginin filtrelenmesi
3. Kalan pixellerin orta noktasının hesaplanması
4. Elde edilen noktayı ekranın tam ortasında tutmaya çalışan kodun yazılması.
