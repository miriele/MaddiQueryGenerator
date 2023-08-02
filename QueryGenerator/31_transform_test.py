import pyproj

def transform_coordinates_epsg2097_to_wgs84(x, y):
    # EPSG 2097 좌표계를 정의합니다.
    epsg_2097 = pyproj.Proj(init='epsg:2097')

    # WGS84 좌표계를 정의합니다.
    wgs84 = pyproj.Proj(init='epsg:4326')

    # 좌표를 변환합니다.
    lon, lat = pyproj.transform(epsg_2097, wgs84, x, y)
    return lon, lat

# EPSG 2097 좌표계에서 (x, y) 좌표를 WGS84 좌표계로 변환합니다.
x = 202086.14
y = 444484.6
lon, lat = transform_coordinates_epsg2097_to_wgs84(x, y)

print(f"WGS84 좌표계: 경도={lon}, 위도={lat}")


from pyproj import Transformer
transformer = Transformer.from_crs("EPSG:2097", "EPSG:4326")
# transformer = Transformer.from_crs(2097, 4326)
print(transformer.transform(y, x))