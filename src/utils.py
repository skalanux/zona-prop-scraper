import datetime
import os
import re
from shapely.geometry import Point, Polygon

POLYGON_ESCALADA = Polygon(
    [
        [-58.39343546661492, -34.715612010771],
        [-58.40030594911242, -34.714573222689225],
        [-58.405913185686785, -34.73867496235531],
        [-58.398256767263696, -34.73901939872937],
        [-58.39495817980681, -34.73836518651938],
        [-58.39420360587066, -34.73232654783052],
        [-58.39468148616238, -34.73424693444988],
        [-58.39343546661492, -34.715612010771],
    ]
)


def remove_host_from_url(url):
    host_regex = r"(^https?://)(.*/)"
    return re.sub(host_regex, "", url)


def get_filename_from_datetime(base_url, extension):
    base_url_without_host = remove_host_from_url(base_url)
    return f'data/{base_url_without_host}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.{extension}'


def save_df_to_csv(df, filename):
    create_root_directory(filename)
    df.to_csv(filename, index=False)


def check_poligon(lat, long):
    """Check if a point is inside a defined polygon."""
    if POLYGON_ESCALADA.contains(Point(long, lat)):
        return True
    else:
        return False


def parse_zonaprop_url(url):
    return url.replace(".html", "")


def create_root_directory(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
